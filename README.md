# README [![CI](https://github.com/nogibjj/Individual_Proj_4_Gavin_Li/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Individual_Proj_4_Gavin_Li/actions/workflows/cicd.yml)


## Website link

https://plantripforyou.azurewebsites.net

## Overview

The purpose of this individual project is to build and deploy a scaleable web-hosted app that will allow me to apply my Flask knowledge from previous lessons. Within the web app, we call the API for a Large Language Model (LLM) to implement our functionality. This project allows user to enter the destination, Number of Travelers, Travel Duration(days) and receive a travel plan. 

## Flask

A flask app is developed to handle requests from the user. The app is in `main.py`.

There are two routings in the app: 

1. `/`

    The homepage is routed to the `index()` function, which returns the `index.html` titled "Plan For Your Trip". This page features a form for planning a trip. It includes fields for entering the destination, number of travelers, and travel duration in days. There are two buttons - "Submit" to process the form data, and "Clear" to reset the form fields. The page uses JavaScript for form submission and clearing the input fields.

<img width="286" alt="截屏2023-12-09 上午12 03 51" src="https://github.com/nogibjj/Individual4_Vivian/assets/143654445/7aa11cb3-8743-46c6-8032-42dc5768f61e">


2. `/`
    
    The result page displays the result returned by the LLM to the user. This webpage, titled "Here is your plan", displays a user's plan details. It includes a heading "Here is your plan:" and a division (<div>) where the plan details, indicated by {{ intro }}, presumably filled by some server-side template, are displayed. There's also a "Return" button which, when clicked, takes the user back to the previous page using JavaScript's window.history.back(); function.

<img width="1331" alt="截屏2023-12-09 上午12 04 11" src="https://github.com/nogibjj/Individual4_Vivian/assets/143654445/41697bd6-b587-417b-85fa-9a774b8db753">


## LLM Integration

In this project, the API of OpenAI is integrated in the app. A token was generated for the app to use.

## Result of `make lint`, `make format`, `make test`

<img width="964" alt="截屏2023-12-09 上午9 02 42" src="https://github.com/nogibjj/Individual4_Vivian/assets/143654445/d9fcfa5d-7592-48fb-a13f-bf93215f21dc">

## Containerization

To make the project easy to deploy, it is containerized with docker. I uploaded a docker image in docker hub. Here is what this project's repository looks like after the push.

<img width="1275" alt="截屏2023-12-09 上午9 06 52" src="https://github.com/nogibjj/Individual4_Vivian/assets/143654445/0d978402-5b0e-4e1e-938d-e5c93fe83032">

The steps of creating a image: 
- login to Docker Hub in terminal `docker login --username <username>`

- Then the files in the project directory is packed into a docker image: `docker docker build -t <username>/<repo name> .`

- Push the image to Docker Hub: `docker push <username>/<repo name>`

## Deployment

The website is then deployed to Azure. Make sure to add the LLM API key, and the website port `WEBSITES_PORT` to the configuration.
Below is my Azure web application: 

<img width="1312" alt="截屏2023-12-09 上午9 10 09" src="https://github.com/nogibjj/Individual4_Vivian/assets/143654445/7e7df3c9-a638-43a6-83bc-27d31c45e5d0">


## Reference
[ruff template](https://github.com/nogibjj/python-ruff-template)







