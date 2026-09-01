from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


# Default route introducing the car company
@app.route('/')
def home():
    return 'Welcome to Flatiron Cars'


# Route for checking if a specific car model is in the fleet
@app.route('/<model>')
def car_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(port=5555, debug=True)