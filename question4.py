from google.colab import auth
from oauth2client.client import GoogleCredentials
import requests
import hashlib

# Authenticate
auth.authenticate_user()
creds = GoogleCredentials.get_application_default()

# Get access token
token = creds.get_access_token().access_token

# Request email from user info endpoint
response = requests.get(
    "https://www.googleapis.com/oauth2/v1/userinfo",
    params={"alt": "json"},
    headers={"Authorization": f"Bearer {token}"}
)

# Extract email
email = response.json()["email"]
print("Email:", email)
