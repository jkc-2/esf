# import serializers from the REST framework
from rest_framework import serializers
 
# import the todo data model
from .models import Project
 
class ProjectSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'created_at', 'created_by_email']

# create a serializer class
# class TodoSerializer(serializers.ModelSerializer):
 
#     # create a meta class
#     class Meta:
#         model = Todo
#         fields = ('id', 'title','description','completed')
