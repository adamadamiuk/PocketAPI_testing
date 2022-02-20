# Description of the project:

The purpose of the code is to create a client for getpocket.com and running tets that verify correctness of requests.

**Client** package includes methods used for sending requests to the API.
It includes **security** package that encodes and decodes user data using JWT.
This API requires authorization, which has been automated with Selenium. 
User can pass the username and password using **user_config.py**

In **Tests** you can find implementation of tests with use of **unittest** framework.

# Project has been created and run with:

- Python 3.9
- Selenium 3.141
- PyJWT 2.1.0
- Requests 2.25.1
- PyCharm 2021.1.2
- Chromedriver v.98
