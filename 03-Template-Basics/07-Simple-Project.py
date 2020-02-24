# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # This home page should have the form.
    return render_template("7-index.html")


# This page will be the page after the form
@app.route("/report")
def report():
    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    username = request.args.get("username")
    has_upper = False
    has_lower = False
    ends_number = False
    if username:
        for letter in username:
            if letter.islower():
                has_lower = True
            if letter.isupper():
                has_upper = True
        if bool(username) and username[-1].isdigit():
            ends_number = True
    all_true = all((has_upper, has_lower, ends_number))

    return render_template(
        "7-report.html",
        all_true=all_true,
        has_lower=has_lower,
        has_upper=has_upper,
        ends_number=ends_number,
    )


if __name__ == "__main__":
    # Fill this in!
    app.run(debug=True)
