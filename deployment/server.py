from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app) 


# Load the trained model
model = tf.keras.models.load_model('my_model.h5')

# Load the tokenizer
with open('tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_text = data['inputText']

    # Tokenize and preprocess the input text
    sequence = tokenizer.texts_to_sequences([input_text])

    padded_sequence = pad_sequences(sequence, maxlen=100, padding='post', truncating='post')

    # Make the prediction
    score = model.predict(padded_sequence)[0][0]

    return jsonify({'score': score})

if __name__ == '__main__':
    app.run()
