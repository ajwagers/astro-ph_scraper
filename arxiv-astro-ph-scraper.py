import urllib.request
import time
import random
from datetime import datetime

search_terms = [
    "21-cm","21cm",
    "Type Ia", "SNe Ia", "SN~Ia"
    "inflation",
    "JWST",
    "BAO",
    "Hubble tension",
    "Crisis in Cosmology",
    "Habitable",
    "redshift",
    "chiral",
    "missing mass",
    "WIMPs",
    "Hubble Constant",
    "supernova remnant",
    "large scale structure", "large-scale structure",
    "mature",
    "selection effects",
    "cosmological"
]

def fetch_and_save_data(url, filename, max_retries=5, initial_delay=1):
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()
                with open(filename, 'wb') as f:
                    f.write(data)
                print(f"Data successfully saved to {filename}")
                return
        except (urllib.error.URLError, ConnectionResetError) as e:
            if attempt == max_retries - 1:
                print(f"Failed to fetch data after {max_retries} attempts: {e}")
                return
            print(f"Error occurred: {e}. Retrying in {initial_delay} seconds...")
            time.sleep(initial_delay)
            initial_delay *= 2  # Exponential backoff
            initial_delay += random.uniform(0, 1)  # Add jitter

# Construct the API query URL
base_url = 'http://export.arxiv.org/api/query?'
search_query = 'cat:astro-ph'
start = 0
max_results = 10
sort_by = 'submittedDate'
sort_order = 'descending'

query_params = {
    'search_query': search_query,
    'start': start,
    'max_results': max_results,
    'sortBy': sort_by,
    'sortOrder': sort_order
}

url = base_url + urllib.parse.urlencode(query_params)

print(f"Query URL: {url}")

# Generate a filename with the current timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"arxiv_response_{timestamp}.xml"

# Fetch the data and save it to a file
fetch_and_save_data(url, filename)

print("Script execution completed.")
