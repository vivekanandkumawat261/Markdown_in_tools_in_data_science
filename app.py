import requests

url = "https://my-vercel-5dp6tuz10-vivekanandkumawat261s-projects.vercel.app/api"
params = {"name": ["Alice", "Bob"]}
response = requests.get(url, params=params)
print(response.json())