from flask import Flask, render_template, redirect, request
from message import Message, db

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    messages = db.query(Message).all()
    return render_template("index.html", messages=messages)


@app.route("/message-handler", methods=["POST"])
def message_handler():
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    email = request.form.get("email")
    message = request.form.get("message")

    contact_message = Message(first_name=first_name, last_name=last_name,
                              email=email, message=message)
    contact_message.save()

    return redirect("/")


if __name__ == "__main__":
    app.run(port=5002, use_reloader=True)
