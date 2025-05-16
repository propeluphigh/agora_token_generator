# Agora Token Server

A Python-based token server for Agora.io that can be easily deployed to Render.

## Features

- Generate RTC tokens for video/audio streaming
- Health check endpoint
- CORS enabled
- Easy deployment to Render

## Local Setup

1. Clone the repository
2. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```
3. Add your Agora credentials to the `.env` file:
   ```
   APP_ID=your_app_id_here
   APP_CERTIFICATE=your_app_certificate_here
   PORT=8080
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the server:
   ```bash
   python app.py
   ```

## API Endpoints

### Health Check
```
GET /ping
Response: {"message": "pong"}
```

### Generate Token
```
POST /getToken
Content-Type: application/json

Request Body:
{
    "tokenType": "rtc",
    "channel": "your_channel_name",
    "role": "publisher",  // or "subscriber"
    "uid": "user_id",     // optional, defaults to 0
    "expire": 3600       // optional, defaults to 3600 seconds (1 hour)
}

Response:
{
    "token": "007eJxTYBBbq...",
    "uid": "user_id"
}
```

## Deployment to Render

1. Fork/Clone this repository
2. Create a new Web Service on Render
3. Connect your repository
4. Add your environment variables (APP_ID and APP_CERTIFICATE)
5. Deploy!

The `render.yaml` file is already configured for deployment.

## Environment Variables

- `APP_ID`: Your Agora App ID
- `APP_CERTIFICATE`: Your Agora App Certificate
- `PORT`: Server port (defaults to 8080)

## Error Handling

The server returns appropriate HTTP status codes and error messages:
- 200: Success
- 400: Bad Request (invalid parameters)
- 500: Server Error

## Security Notes

- Never expose your App Certificate in client-side code
- Use environment variables for sensitive data
- Token expiration is configurable through the API 