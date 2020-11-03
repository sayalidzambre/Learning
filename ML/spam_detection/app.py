from flask import Flask, render_template, url_for, request, jsonify
from sklearn.pipeline import Pipeline
import joblib

app = Flask(__name__)
global pipeline

pipeline = joblib.load('spam_detection_pipeline.pkl')
print('Pipeline loaded')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    result = None
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            message = data.get('message', '')
            if len(message) > 0:
                result = pipeline.predict([message])[0]
                if result == 1:
                    result = True
                else:
                    result = False
        except Exception as e:
            print(str(e))
    return jsonify({"spam": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, use_reloader=True)