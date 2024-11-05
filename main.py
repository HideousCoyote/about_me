from flask import Flask, render_template
from jobdict import jobs
from dotenv import load_dotenv
import os

load_dotenv()

SUPER_SECRET_KEY = os.getenv("SUPER_SECRET_KEY")


app = Flask(__name__)
app.config['SECRET_KEY'] = SUPER_SECRET_KEY



@app.route('/')
def index():
    return render_template("index.html", jobs=jobs)


if __name__ == "__main__":
    app.run(debug=False)