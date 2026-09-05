from flask import Flask, render_template
import json
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


def load_json(filename):
    with open(f"data/{filename}", "r") as file:
        return json.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/alumni")
def alumni():
    alumni_data = load_json("alumni.json")
    return render_template("alumni.html", alumni=alumni_data)


@app.route("/jobs")
def jobs():
    jobs_data = load_json("jobs.json")
    return render_template("jobs.html", jobs=jobs_data)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
