from flask import Flask, render_template, request, flash
from jobdict import jobs
from dotenv import load_dotenv
import os
import smtplib


load_dotenv()

OWN_EMAIL = os.getenv("OWN_EMAIL")
OWN_PASSWORD = os.getenv("OWN_PASSWORD")
SEND_TO_EMAIL = os.getenv("SEND_TO_EMAIL")
SUPER_SECRET_KEY = os.getenv("SUPER_SECRET_KEY")


app = Flask(__name__)
app.config['SECRET_KEY'] = SUPER_SECRET_KEY



@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html", jobs=jobs)

@app.route('/sent', methods=["GET", "POST"])
def recieve_data():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)
        return render_template("index.html")
    return render_template("index.html")

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            connection.sendmail(OWN_EMAIL, SEND_TO_EMAIL, email_message)
            connection.quit()
            flash("Your Message has been sent.", "success")
    except Exception as e:
        flash("There was an error, Please try again later.", "error")

if __name__ == "__main__":
    # app.run(debug=False)
    app.run(debug=True, host="0.0.0.0", port="5001")