
import requests

try:
    response = requests.get("https://api.ipify.org", timeout=10)
    response.raise_for_status()

    print("Public IP Address:", response.text)

except requests.RequestException as e:
    print("Error:", e)
