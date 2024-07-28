from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Charger le modèle
model = pickle.load(open('house.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    final_features = final_features.append(1)
    prediction = model.predict(final_features)
    prediction = np.exp(prediction[0])

    output = prediction

    return render_template('index.html', prediction_text=f'Predicted Price: ${output}')

if __name__ == "__main__":
    app.run(debug=True)
