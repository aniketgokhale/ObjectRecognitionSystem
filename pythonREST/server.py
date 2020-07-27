import base64
from flask import Flask, request, jsonify ,send_file
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    return send_file('input.png',mimetype='image/jpg',
    as_attachment=False,)


@app.route('/predict', methods=['POST'])
def predict():
    # if lr:
        try:
            json_ = request.json
            # print(json_)
            image_data = json_.get('image')
            # print(base64.b64decode(image_data))
            with open("input.jpg", "wb") as fh:
                fh.write(base64.b64decode(image_data))
            # data =request.files['file']
            # data.save('car.jpg');
            # query = pd.get_dummies(pd.DataFrame(json_))
            # query = query.reindex(columns=model_columns, fill_value=0)

            # prediction = list(lr.predict(query))

            return jsonify({'trace': "Successful upload"})

        except:

            return jsonify({'trace': traceback.format_exc()})
    # else:
    #     print ('Train the model first')
    #     return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 1234 # If you don't provide any port the port will be set to 12345

    # lr = joblib.load("model.pkl") # Load "model.pkl"
    # print ('Model loaded')
    # model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    # print ('Model columns loaded')

    app.run(host='0.0.0.0')