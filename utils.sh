#!/bin/bash
PS3="Please choose an option: "
options=("Update client API" "Escape")
select opt in "${options[@]}"
do 
   case $opt in
      "Update client API")
        echo "Updating API Client"
        python server/manage.py spectacular --file api_schema.yml
        openapi-generator-cli generate -i api_schema.yml -g typescript-fetch -o ./client/api/
        break
        ;;
      "Escape")
         break
         ;;
   esac
done