from joblib import load
import pandas as pd
from flask import Flask, request


MODEL_PICKLE = 'churn_model.pkl'
FEATURES = ['is_male', 'num_inters', 'late_on_payment',	'age',	'years_in_contract']
PRED = 0


app = Flask('Predicting cellular churn in Greece')


@app.route('/predict_churn')
def predict_churn():
    """Predicts a single prediction"""
    features = FEATURES
    arg_feats = pd.DataFrame({feat: [request.args.get(f'{feat}')] for feat in features})

    x = pd.DataFrame(arg_feats)
    prediction = clf.predict(x)
    return str(prediction[PRED])


if __name__ == '__main__':
    # loading the model from Pickle file:
    clf = load(MODEL_PICKLE)

    app.run(host='0.0.0.0', port=8080)
