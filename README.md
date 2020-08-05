# Tortoise Community: Website 
[![Discord](https://img.shields.io/static/v1?label=Tortoise%20Community&logo=discord&message=%3E2k%20members&color=%23FFB101&logoColor=7289da)](https://discord.gg/GQdZjmW)
![Python-Versions](https://img.shields.io/badge/python-3.8.3-blue?style=flat-square)
![Django-Version](https://img.shields.io/badge/django-3.0.7-%23042e24)
![Django-Rest-Framwork-Version](https://img.shields.io/badge/django%20rest%20framework-3.11.0-darkred)
[![Status](https://img.shields.io/website?url=https%3A%2F%2Ftortoisecommunity.com)][1]

#### Website powered by Django for the Tortoise Community Discord Server

This is the code for our website coded in python with the Django Framework. 
Code here serves for educational purposes and for transparency of data collection, handling and security.

####Features

* Discord Oauth2 verification system for preventing spam and detecting alt-accounts.
* Real time Top member ranking based on perk system.
* Markdown compatible pages for hosting events and showcasing projects.
* Rest API Backend for the bot to interact with the database.
* Admin dashboard for easily managing the bot from withing the Website.

####Contributing

We encourage everyone to contribute to the code. All updates are welcome. 
While contributing to the code please make sure that you push only to the `dev` branch of the repository
Also note that all contributions to the code should follow the pep8 standards. 
To ease out this process follow the project setup instruction for developers.

####Project Setup Instruction

**Python 3.8 reqiuired**
```git
# Begin by forking the repo to your github account (make managing conflicts easier)

# Your global Python installation needs to have pipenv
pip install pipenv

# Clone the repository from your profile 
https://github.com/<Your-Github-Username>/Website.git

# [development installation] If you are developer/looking to contribute you need to install dependencies for dev
pipenv install --dev

# [production installation] If you are setting up site for production just install required dependencies like this
pipenv install

# Activate the Pipenv shell (aka tell your terminal/whatever to use dependencies from the env in this project)
pipenv shell

# The site should now be setup, You won't be able to run the test server because of the missing credentials.


```
[1]: https://tortoisecommunity.com

