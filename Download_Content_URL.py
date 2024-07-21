# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:52:40 2024

@author: prasa
"""

import requests
from time import sleep

def download_content(urls):
    results = {}
    
    for url in urls:
        attempts = 0
        while attempts < 3:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
                results[url] = response.text
                print(f"Successfully downloaded content from {url}")
                break  # Exit the retry loop if the request was successful
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred for {url}: {http_err}")
            except requests.exceptions.ConnectionError as conn_err:
                print(f"Connection error occurred for {url}: {conn_err}")
            except requests.exceptions.Timeout as timeout_err:
                print(f"Timeout occurred for {url}: {timeout_err}")
            except requests.exceptions.RequestException as req_err:
                print(f"Request error occurred for {url}: {req_err}")
            
            attempts += 1
            if attempts < 3:
                print(f"Retrying {url} ({attempts}/3)...")
                sleep(2)  # Wait for 2 seconds before retrying
    
        if attempts == 3:
            results[url] = None
            print(f"Failed to download content from {url} after 3 attempts")
    
    return results

# Example usage:
urls = [
    "https://www.example.com",
    "https://www.nonexistentwebsite.com",  # This will likely cause an error
    "https://www.python.org"
]

content = download_content(urls)
for url, data in content.items():
    if data:
        print(f"Content from {url}:\n{data[:100]}...")  # Print the first 100 characters of the content
    else:
        print(f"No content retrieved from {url}")
