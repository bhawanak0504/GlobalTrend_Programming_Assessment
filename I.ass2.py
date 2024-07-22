import requests
import logging
from urllib3.exceptions import MaxRetryError, NewConnectionError  # Import specific exceptions

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_urls_with_retry(urls, max_retries=3):
    results = {}
    for url in urls:
        for attempt in range(max_retries + 1):
            try:
                response = requests.get(url, timeout=10)  # Adding timeout for requests
                response.raise_for_status()
                results[url] = response.content
                logging.info(f"Downloaded content from {url} (attempt {attempt+1}/{max_retries + 1})")
                break
            except requests.exceptions.RequestException as e:
                logging.warning(f"Error downloading {url} (attempt {attempt+1}/{max_retries + 1}): {e}")
                continue
            except NewConnectionError as e:
                logging.error(f"Failed to resolve host for {url}: {e}")
                results[url] = None
                break
            except MaxRetryError as e:
                if "NameResolutionError" in str(e):
                    logging.error(f"DNS resolution failed for {url}: {e}")
                else:
                    logging.error(f"Max retries exceeded for {url}: {e}")
                results[url] = None
                break
            except Exception as e:
                logging.error(f"Unexpected error downloading {url}: {e}")
                results[url] = None
                break
        
        if url not in results:  # If all retries failed
            logging.warning(f"Failed to download content from {url} after {max_retries + 1} attempts.")

    return results

# Example usage
urls = [
    "https://www.example.com",
    "https://www.nonexistentwebsite.com",  # This URL intentionally does not exist
    "https://www.example.org"
]
downloaded_content = download_urls_with_retry(urls)

for url, content in downloaded_content.items():
    if content:
        print(f"Content for {url}:")
        print(content[:300])  # Print first 300 characters of content for demonstration
    else:
        print(f"Failed to download content from {url}")