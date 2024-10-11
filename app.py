import numpy as np
from flask import Flask,render_template,jsonify,request
import pickle


app=Flask(__name__)
model=pickle.load(open("iris_model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    float_features=[float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    prediction=model.predict(features)

    return render_template('index.html',prediction_text="the flower species is {}".format(prediction))

if __name__=="__main__":
    app.run(debug=True)