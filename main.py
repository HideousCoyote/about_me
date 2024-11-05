from flask import Flask, render_template, url_for
# from flask_bootstrap import Bootstrap5
from jobdict import jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lkasjdflkjasdflkjasdflkj'
# Bootstrap5(app)


@app.route('/')
def index():
    return render_template("index.html", jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")