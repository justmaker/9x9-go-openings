import requests
import os

url = "https://katagobooks.org/downloads/book9x9tt-20260226.tar.gz"
output_filename = "book9x9tt-20260226.tar.gz"

print(f"Downloading {url} to {output_filename}...")
try:
    response = requests.get(url, stream=True)
    response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

    with open(output_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Successfully downloaded {output_filename}")
except requests.exceptions.RequestException as e:
    print(f"Error downloading the file: {e}")
    exit(1)
