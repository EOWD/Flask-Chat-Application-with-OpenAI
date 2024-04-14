from openai import OpenAI
import os
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)


from flask import Blueprint, jsonify

lm_bp = Blueprint('lm_bp', __name__)

@lm_bp.route('/fine-tune', methods=['POST'])
def fine_tune():
    # Ensure your API key is set as an environment variable

    # Hardcoded file path to your dataset
    file_path = 'FineTunning_file1.jsonl'  

    # Check if the file exists
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    # Upload the file to OpenAI
    try:
        response = client.files.create(file=open(file_path, 'rb'), purpose='fine-tune')
        file_id = response.id
    except Exception as e:
        return jsonify({"error": f"Failed to upload file: {str(e)}"}), 500

    # Initiate fine-tuning with the uploaded file
    try:
        fine_tuning_response = client.fine_tuning.jobs.create(training_file=file_id,
        model='ft:gpt-3.5') # update your base model for fine-tuning
        model_id = fine_tuning_response.id
        return jsonify({"message": "Fine-tuning initiated", "model_id": model_id}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to initiate fine-tuning: {str(e)}"}), 500
