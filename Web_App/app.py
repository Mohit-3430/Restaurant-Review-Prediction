from datetime import date
from flask import Flask, redirect, render_template, request, url_for
import numpy as np
import joblib


model = joblib.load(open("./model/final_model.joblib", "rb"))
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    title = "Forecasting eatary returns"
    if request.method == "GET":
        return render_template("index.html", title=title, result=False)
    else:
        return redirect(url_for("predict"))


@app.route("/predict", methods=["GET", "POST"])
def predict():
    title = "Forecasting eatary returns"
    if request.method == "GET":
        return render_template("index.html", title=title, result=False)
    elif request.method == "POST":
        post_city = request.form["city"]
        post_res = request.form["restaurant"]

        # ({'MB':0,'DT':1, 'IL':2,'FC':3})
        # ({'Big Cities':1, 'Other':0})

        # CITY
        if post_city == "İstanbul" or post_city == "Ankara" or post_city == "İzmir":
            citygroup = 1
        else:
            citygroup = 0
        # Type
        if post_res == "Mobile":
            res = 0
        elif post_res == "Drive Thru":
            res = 1
        elif post_res == "In line":
            res = 2
        elif post_res == "Food Court":
            res = 3
        # Date
        curr_date = date.today()
        curr_date = int(curr_date.strftime("%Y%#m%#d"))

        pred_array = np.zeros(32)
        pred_array[0] = curr_date
        pred_array[1] = citygroup
        pred_array[2] = res

        data = model.predict([pred_array])[0]
        data = round(data)
        return render_template("index.html", title=title, result=True, data=data)


@app.route("/about-us")
def aboutUs():
    title = "About-Us"
    return render_template("AboutUs.html", title=title)


@app.route("/contact-us")
def contactUs():
    title = "Contact-Us"
    return render_template("ContactUs.html", title=title)


if __name__ == "__main__":
    app.run(debug=False)
