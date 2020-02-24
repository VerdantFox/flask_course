# Set up your imports here!
from flask import Flask, request

app = Flask(__name__)


@app.route("/")  # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    page = "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin</h1>"
    return page


@app.route("/puppy_latin/<name>")  # Fill this in!
def puppy_latin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    if name.endswith('y'):
        new_name = name[:-1] + 'iful'
    else:
        new_name = name + 'y'
    page = f"<h1>Hi {name}! Your puppylatin name is {new_name}</h1>"
    return page


if __name__ == "__main__":
    # Fill me in!
    app.run(debug=True)
