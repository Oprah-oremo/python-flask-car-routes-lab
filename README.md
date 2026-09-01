# Flatiron Cars — Flask Car Routes

## Description

This project is a simple Flask application that demonstrates how to create routes for a car company database.

The application provides a default route for introducing the company and a dynamic route for checking whether a specific car model is part of the company's fleet.

## Features

* Default `/` route
* Dynamic `/<model>` route
* Checks car models against the existing fleet
* Returns an appropriate message for existing and unavailable models
* Flask development server
* Automated tests using pytest

## Available Routes

### Home Route

**URL:**

`/`

**Response:**

`Welcome to Flatiron Cars`

### Car Model Route

**URL:**

`/<model>`

If the model exists in the fleet, the application returns:

`Flatiron {model} is in our fleet!`

If the model does not exist, the application returns:

`No models called {model} exists in our catalog`

### Existing Models

The application currently checks the following models:

* Beedle
* Crossroads
* M2
* Panique

## Running the Application

Activate the Pipenv environment:

```bash
pipenv shell
```

Start the Flask server:

```bash
python3 server/app.py
```

The application runs at:

`http://127.0.0.1:5555`

## Testing

Run the test suite with:

```bash
pytest
```

All tests pass successfully.

## Technologies Used

* Python
* Flask
* pytest
* Pipenv
* Git and GitHub

## Project Status

The required Flask routes have been implemented, tested, and merged into the `main` branch.
