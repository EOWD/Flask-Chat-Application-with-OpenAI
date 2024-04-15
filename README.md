
# Flask Chat Application

This Flask-based chat application combines MongoDB, OpenAI's GPT-3 model, and secure authentication features to deliver an interactive and intelligent chat experience. It is configured with JWT token verification, basic authentication using bcrypt, and supports fine-tuning of AI models using JSON files.

## Key Components

Flask Server: Utilizes Flask, a Python microframework, to handle HTTP requests and responses.
OpenAI Integration: Integrates OpenAI's powerful GPT-3 model for generating intelligent chat responses .
MongoDB Database: Uses MongoDB as the database backend for storing user information and chat history.
Authentication Middleware: Implements JWT token verification and bcrypt for secure user authentication.
Fine-Tuning Capabilities: Supports fine-tuning of AI models by leveraging JSON files for custom model configurations.

## Installation
To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone 
   ```

2. Install dependencies:
   ```bash
   cd Flask-Chat-Application-with-OpenAI

   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   OPENAI_API_KEY=<your_openai_api_key>
   MODEL=<your_openai_model_name>
   MONGO_URI=<your_mongodb_uri>
   ORIGIN=<front-ennd Client>
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

## Endpoints

### Signup (POST /signup)

Create a new user account.

**Request:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "message": "User created successfully",
  "user": {
    "id": "123456",
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### Login (POST /auth/login)

Authenticate a user and retrieve an access token.

**Request:**
```json
{
  "email": "john@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "access_token": "<jwt_access_token>",
  "user_id": "123456"
}
```

### Chat (POST /chat)

Initiate a chat conversation with the AI model.

**Request:**
```json
{
  "id": "123456",
  "input": "Hello, how are you?"
}
```

**Response:**
```json
{
  "response": "I'm doing well, thank you! How can I assist you today?"
}
```

## Usage

1. Use Postman or any API client to interact with the endpoints.
2. Register a new user using the `/signup` endpoint.
3. Authenticate and obtain an access token using the `/auth/login` endpoint.
4. JWT TOKEN Verification `/auth/verify`
5. Start a chat conversation using the `/chat` endpoint by providing the user ID and input message.
```


