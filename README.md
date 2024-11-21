# login_page_microservice

# Description
This microservice allows users to sign up and log in using POST requests. It validates user credentials and provides success or error messages.

# How to use:
To start using the microservice, first, ensure that you have Python installed on your machine. Start by running the Flask app with the command python3 microservice.py. By default, the service will run locally at http://127.0.0.1:5000/.

The microservice has two primary endpoints: /signup for creating a new account and /login for logging in. Both endpoints accept JSON requests and return JSON responses.

- Sign Up Endpoint:
The /signup endpoint allows users to create a new account. To use this, it send a POST request with the username and password fields in the JSON body. If the username is unique, the service will return a success message welcoming the new user. If the username already exists, it will return an error message.

Example request:
{
    "username": "new_user",
    "password": "password123"
}

For successful response: { "status": "success", "message": "Welcome new user!" }

For error response: { "status": "error", "message": "Username already exists. Please choose another." }

- Login Endpoint:
The /login endpoint allows users to log in with their existing username and password. To use this, it send a POST request with the username and password fields in the JSON body. If the inputs are valid, the service will return a success message welcoming the user back. But if they are incorrect, it will return an error message.

Example request:
{
    "username": "existing_user",
    "password": "password123"
}

For successful response: { "status": "success", "message": "Welcome back!" }

For error response: { "status": "error", "message": "Invalid login input, please try again." }
