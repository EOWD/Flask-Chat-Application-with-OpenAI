
# Flask Chat Application

This is a Flask-based chat application that utilizes the OpenAI GPT-3 model to provide interactive responses to users. The application allows users to engage in chat conversations and receive intelligent responses based on the context of the conversation.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone 
   ```

2. Install dependencies:
   ```bash
   cd BreadcrumbsFlask-Chat-Application-with-OpenAI

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
4. Start a chat conversation using the `/chat` endpoint by providing the user ID and input message.
```

You can copy the above Markdown content and paste it into a `README.md` file in your project directory. Make sure to replace placeholders like `<repository_url>`, `<your_openai_api_key>`, `<your_openai_model_name>`, and `<your_mongodb_uri>` with the actual values relevant to your application. This Markdown file will provide clear instructions and examples for using and interacting with your Flask chat application.
