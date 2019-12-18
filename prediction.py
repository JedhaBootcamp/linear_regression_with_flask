import requests
BASE_URL = "http://127.0.0.1:5000"
years_exp = {"YearsExperience": 8}
response = requests.post("{}/predict".format(BASE_URL), json = years_exp)

print(response.json())
