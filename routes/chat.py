from flask import Blueprint, request, jsonify, current_app
import os
from openai import OpenAI
from models.ChatSchema import ChatSchema
from bson import ObjectId
from datetime import datetime
api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=api_key)

chat_schema = ChatSchema()

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    user_id = request.json.get('id')
    #print(user_id)
    
    mongo_client = current_app.config['MONGO_CLIENT']
    mongo_db = current_app.config['MONGO_DB']


    try:
         
        user_chats = mongo_db.chats.find({'user_id': user_id}).sort('_id', -1).limit(10)
        user = mongo_db.users.find_one({'_id': ObjectId(user_id)})
        print(user)

        if user:
            user_name = str(user['name'])
            user_occupation = str(user['occupation'])
            print(user_name, user_occupation)
        else:
          
            user_name = 'Unknown'
            user_occupation = 'Bio-tech specialist'

        system_message = f"You are a helpful assistant specialized in Bio-tech always answer in a professional but yet human like manner, the users job is  {user_occupation}, and users name is {user_name} ,use this to personalize response. If asked any questions out of this field, respond with something like (i am a specialized ai model for bio-tech)"
        messages = [
            {"role": "system", "content": system_message}
        ]
        for chat in reversed(list(user_chats)):
            messages.append({"role": "user", "content": chat['user_message']})
            messages.append({"role": "system", "content": chat['model_reply']})

        messages.append({"role": "user", "content": user_input})   


        completion = client.chat.completions.create(
            model=os.getenv('MODEL'),
           messages=messages
        )

       
        print(completion.choices[0].message)
        message_content = completion.choices[0].message.content if completion.choices[0].message.content else "No response generated."
        chat_data = {
                'user_message': user_input,
                'model_reply': message_content,
                'timestamp': datetime.utcnow(),
                'user_id': user_id  
            }
        mongo_db.chats.insert_one(chat_data)
        return jsonify({'response': message_content})

    except Exception as e:
        print("Error generating", e)
        return jsonify({"error": f"Failed to initiate chat: {str(e)}"}), 500
