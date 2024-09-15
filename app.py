from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Simulate localStorage using a dictionary
local_storage = {}

# Initialize with some sample data
local_storage['faqs'] = json.dumps([
    {"id": 1, "question": "What is Fruit.ai?", "answer": "Fruit.ai is an AI-powered platform that provides information about fruits."},
    {"id": 2, "question": "How does the fruit chatbot work?", "answer": "Our fruit chatbot uses natural language processing to answer questions about fruits."}
])

def get_next_id():
    faqs = json.loads(local_storage.get('faqs', '[]'))
    return max([faq['id'] for faq in faqs], default=0) + 1

@app.route('/faqs', methods=['GET'])
def get_faqs():
    faqs = json.loads(local_storage.get('faqs', '[]'))
    return jsonify(faqs)

@app.route('/faqs/<int:faq_id>', methods=['GET'])
def get_faq(faq_id):
    faqs = json.loads(local_storage.get('faqs', '[]'))
    faq = next((faq for faq in faqs if faq['id'] == faq_id), None)
    if faq is None:
        return jsonify({"error": "FAQ not found"}), 404
    return jsonify(faq)

@app.route('/faqs', methods=['POST'])
def create_faq():
    data = request.json
    faqs = json.loads(local_storage.get('faqs', '[]'))
    new_faq = {
        "id": get_next_id(),
        "question": data['question'],
        "answer": data['answer']
    }
    faqs.append(new_faq)
    local_storage['faqs'] = json.dumps(faqs)
    return jsonify(new_faq), 201

@app.route('/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    data = request.json
    faqs = json.loads(local_storage.get('faqs', '[]'))
    faq = next((faq for faq in faqs if faq['id'] == faq_id), None)
    if faq is None:
        return jsonify({"error": "FAQ not found"}), 404
    faq['question'] = data['question']
    faq['answer'] = data['answer']
    local_storage['faqs'] = json.dumps(faqs)
    return jsonify(faq)

@app.route('/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    faqs = json.loads(local_storage.get('faqs', '[]'))
    faqs = [faq for faq in faqs if faq['id'] != faq_id]
    local_storage['faqs'] = json.dumps(faqs)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)