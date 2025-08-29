from flask import Flask, jsonify, request

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def home():
    return "Hello From Flask Application!"


@app.route("/hello", methods=['GET'])
def hello():
    return "Hello World!"


app.add_url_rule('/hello2', 'hello2', hello)


def user_profile(username):
    return f"User: {username.capitalize()}"


app.add_url_rule('/user/<username>', 'profile', user_profile)


@app.route("/celsius/<celsius>", methods=["GET"])
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return (f"Your temperature in Fahrenheit: {str(fahrenheit)}." + "\n" +
                "Normal human body temperature is 97 degree Fahrenheit." + "\n"*4)
    except ValueError:
        return f"Invalid Input:  {celsius}" + "\n"*4


@app.route("/fahrenheit/<fahrenheit>", methods=["GET"])
def celsius_from(fahrenheit):
    """Convert Fahrenheit to Celsius degrees."""
    try:
        celsius = (float(fahrenheit) - 32.0) * 5/9
        celsius = round(celsius, 2)  # Round to three decimal places
        return (f"Your temperature in Celsius: {str(celsius)}." + "\n" +
                f"Normal human body temperature is 37 degree Celsius." + "\n"*4)
    except ValueError:
        return f"Invalid Input:  {fahrenheit}" + "\n"*4


@app.route("/hello/<name>", methods=['GET'])
def hello_user(name):
    return "Hello %s" % name.capitalize()


if __name__ == '__main__':
    app.run(port=5010, host="0.0.0.0", debug=True)


