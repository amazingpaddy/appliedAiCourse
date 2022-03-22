from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
path = "/home/paddy/python_ws/appliedAiCourse/ml-docker-kubernets-learnings/"
pickle_in = open(path + 'classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All!!"

@app.route("/predict")
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return f"The predicted value is : {str(prediction[0])}"

@app.route("/predict_file", methods=["POST"])
def predict_note_authentication_from_file():
    test_df = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(test_df)
    return f"The predicted value is : {str(list(prediction))}"


if __name__ == '__main__':
    app.run()