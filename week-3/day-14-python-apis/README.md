# Day 14: Python APIs

## API Selected
**Dog CEO API** (https://dog.ceo/dog-api/), a free public API from PublicAPIs.io that returns JSON data about dog breeds and images. It does not require an API key or a paid subscription.

## What the Program Does
`main.py` sends a GET request to the API using the `requests` library, checks the response, converts it to JSON, extracts useful information, and prints it in a clear, readable format. It also handles network failures and unsuccessful responses without crashing.

## Endpoint and Parameters Used
- **Endpoint:** `https://dog.ceo/api/breed/{breed}/images/random`
- **Parameter:** `breed` (for example `husky`, `beagle`, `poodle`), which is changed in the URL to test different responses.
- **Authentication:** None required.

## JSON Response Structure
The response is a dictionary with two keys:
- `message`: the image URL
- `status`: the request status (`success` or `error`)

## Useful Information Extracted
1. **Breed searched**: the breed name used in the request
2. **Image URL**: link to a random image of that breed
3. **API status**: whether the request was successful

## How the Program Works
1. A function `get_dog_data(breed)` sends the GET request and returns the JSON data.
2. `try` and `except` with `requests.exceptions.RequestException` handle network failures.
3. `response.status_code` is checked to handle unsuccessful responses.
4. The extracted information is printed with clear labels.

## How to Run
```
python -m venv .venv
.venv\Scripts\activate
python -m pip install requests
python main.py
```

## Testing
The program was run successfully with the breed `husky`, then tested again with `beagle` to confirm it processes a new response correctly.