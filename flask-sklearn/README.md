# Overview

This project includes a Python flask app with ML predictions. It is build and deployed in Azure Pipelines as an Azure App Service.

## Project Plan

* Here you can find the Trello board https://trello.com/b/incF6VdI/udacity. The board is currently set on private, but it looks like ![grafik](https://user-images.githubusercontent.com/121881667/211019880-342773a7-c680-4e39-89e0-b5690218a89f.png)

* Here you can find the spreadsheet used for the planning [project-management-template.xlsx](https://github.com/technik-matrose/flask-ml-app/files/10360367/project-management-template.xlsx)

## Instructions

In the architectural diagram below you can see, that the project is made out of 4 main components:
![grafik](https://user-images.githubusercontent.com/121881667/211026170-cd09f1fb-d6ec-42ba-b6e3-2d86a81097d9.png)

Instructions for running the Python project:

Project running on Azure App Service
* Launch Azure Cloud Shell environment and create ssh-keys
* Upload keys to your GitHub account and clone the repo ![Git_clone_Screenshort](https://user-images.githubusercontent.com/121881667/211028330-0509cb90-c7a9-4aa6-98a6-9d5ada0d095a.png)
* Create the Python Virtual Environment
* Run following commands 'make install' and 'az webapp up --name <Your_unique_app_name> --resource-group <resource-group> --runtime "PYTHON:3.7"'

Passing tests that are displayed after running the `make all` command from the `Makefile`
* Output of a test run
  ![make_all_Screenshot](https://user-images.githubusercontent.com/121881667/211028525-d169b239-a46a-4f25-8cee-0915b905445b.png)

Successful deploy of the project in Azure Pipelines
* Create a project in Azure DevOps
* Add a new service connection "Azure Resource Manager" like ![grafik](https://user-images.githubusercontent.com/121881667/211029493-e9dfc1a3-5c91-4535-b917-14415049f8f9.png)
* Create a new pipeline and select the 'Python to Linux Web App on Azure' configuration ![grafik](https://user-images.githubusercontent.com/121881667/211029804-53a10cbd-40eb-4d13-998f-5bb61aa0fb79.png)
* Select your recently created App service

Running Azure App Service from Azure Pipelines automatic deployment
* Go to the Pipelines section in Azure DevOps
* Select your created pipeline and press on the 'Run' button

Successful prediction from deployed flask app in Azure Cloud Shell
* Go to your Azure Cloud Shell environment
* Navigate to the directory of the project directory
* Run command './make_predict_azure_app.sh'

Output of streamed log files from deployed application
* The output can be found in the log of the deployment job
* Here is a snippet of the log files
![grafik](https://user-images.githubusercontent.com/121881667/212567615-66da8286-ed8a-4d8c-92b3-bb749c07a805.png)


## Enhancements

In future an improvement can be to deploy the App directly here from GitHub in Actions.

## Demo 

You can find a video with a demo here: https://vimeo.com/789611820


