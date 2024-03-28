import os
import smtplib
from os.path import join, dirname
from flask import Flask, render_template, request, flash, redirect
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
Bootstrap5(app)

EMAIL_LOGIN = os.environ.get("EMAIL_LOGIN")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        data = request.form
        try:
            send_email(data["name"], data["email"], data["phone"], data["message"])
            flash('Message successfully sent.')
        except:
            flash('There was an error in sending message.')
        return redirect("#contact")
    return render_template('index.html')


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        connection.sendmail(EMAIL_LOGIN, 'slliver@icloud.com', email_message)


if __name__ == '__main__':
    app.run(debug=True, port=5050)
