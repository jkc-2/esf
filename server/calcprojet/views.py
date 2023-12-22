from django.contrib.auth import get_user_model

# import view sets from the REST framework
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    UserChangePasswordErrorSerializer,
    UserChangePasswordSerializer,
    UserCreateErrorSerializer,
    UserCreateSerializer,
    UserCurrentErrorSerializer,
    UserCurrentSerializer,
    ProjectSerializer,
    NeedRessourceSerializer,
    NeedTypeSerializer,
    NeedSerializer,
    NeedValueSerializer,
    MaterialTypeSerializer,
    MaterialCustomFieldSerializer,
    MaterialCustomFieldValueSerializer,
)
from .models import (
    Project,
    NeedRessource,
    NeedType,
    Need,
    NeedValue,
    MaterialType,
    MaterialCustomField,
    MaterialCustomFieldValue,
    )
 
User = get_user_model()

class UserView(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserCurrentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(pk=self.request.user.pk)

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        elif self.action == "me":
            return UserCurrentSerializer
        elif self.action == "change_password":
            return UserChangePasswordSerializer

        return super().get_serializer_class()

    @extend_schema(
        responses={
            200: UserCreateSerializer,
            400: UserCreateErrorSerializer,
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        responses={
            200: UserCurrentSerializer,
            400: UserCurrentErrorSerializer,
        }
    )
    @action(["get", "put", "patch"], detail=False)
    def me(self, request, *args, **kwargs):
        if request.method == "GET":
            serializer = self.get_serializer(self.request.user)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = self.get_serializer(
                self.request.user, data=request.data, partial=False
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == "PATCH":
            serializer = self.get_serializer(
                self.request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    @extend_schema(
        responses={
            204: None,
            400: UserChangePasswordErrorSerializer,
        }
    )
    @action(["post"], url_path="change-password", detail=False)
    def change_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.request.user.set_password(serializer.data["password_new"])
        self.request.user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(["delete"], url_path="delete-account", detail=False)
    def delete_account(self, request, *args, **kwargs):
        self.request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
 
    queryset = Project.objects.all()

# Write viewsets for the other models

class NeedRessourceView(viewsets.ModelViewSet):
    serializer_class = NeedRessourceSerializer

    queryset = NeedRessource.objects.all()


class NeedTypeView(viewsets.ModelViewSet):
    serializer_class = NeedTypeSerializer

    queryset = NeedType.objects.all()

class NeedView(viewsets.ModelViewSet):
    serializer_class = NeedSerializer

    queryset = Need.objects.all()

class NeedValueView(viewsets.ModelViewSet):
    serializer_class = NeedValueSerializer

    queryset = NeedValue.objects.all()

class MaterialTypeView(viewsets.ModelViewSet):
    serializer_class = MaterialTypeSerializer

    queryset = MaterialType.objects.all()

class MaterialCustomFieldView(viewsets.ModelViewSet):
    serializer_class = MaterialCustomFieldSerializer

    queryset = MaterialCustomField.objects.all()

class MaterialCustomFieldValueView(viewsets.ModelViewSet):
    serializer_class = MaterialCustomFieldValueSerializer

    queryset = MaterialCustomFieldValue.objects.all()