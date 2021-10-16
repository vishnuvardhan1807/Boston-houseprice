from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

# initializing a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')

# route to show predictions in web ui
@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == "POST":
        try:
            # reading the inputs given by user
            # CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT
            CRIM = float(request.form["CRIM"])
            ZN = float(request.form["ZN"])
            INDUS = float(request.form["INDUS"])
            CHAS = float(request.form["CHAS"])
            NOX = float(request.form["NOX"])
            RM = float(request.form["RM"])
            AGE = float(request.form["AGE"])
            DIS = float(request.form["DIS"])
            RAD = float(request.form["RAD"])
            TAX = float(request.form["TAX"])
            PTRATIO = float(request.form["PTRATIO"])
            B = float(request.form["B"])
            LSTAT = float(request.form["LSTAT"])
            
            # open and load the saved model
            filename = 'lr_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))

            # make predictions using the loaded model
            prediction = loaded_model.predict([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS,
             RAD, TAX, PTRATIO, B, LSTAT]])
            print('prediction is', prediction)

            # show the predictions in web page
            return render_template('result.html', prediction=prediction[0])
        
        except  Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
        
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)