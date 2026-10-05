# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests


def get_dog_data(breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    try:
        response = requests.get(url, timeout=10)
        print("Status code:", response.status_code)
        print("Request URL:", response.url)

        if response.status_code == 200:
            return response.json()
        else:
            print("Request failed. Breed may not exist.")
            return None
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None


def show_data(breed, data):
    if data is None:
        return
    print("\n--- Dog Info ---")
    print("Breed searched:", breed)
    print("Image URL:", data["message"])
    print("API status:", data["status"])


for breed in ["husky", "beagle"]:
    data = get_dog_data(breed)
    show_data(breed, data)