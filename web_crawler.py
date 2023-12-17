#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import json

class AdvancedWebCrawler:
    def __init__(self, base_url, max_threads=5):
        self.base_url = base_url
        self.max_threads = max_threads
        self.visited_links = set()
        self.results = []

    def crawl(self, url, depth=2):
        if depth == 0 or url in self.visited_links:
            return

        try:
            response = requests.get(url)
            content_type = response.headers.get('content-type', '')
            soup = BeautifulSoup(response.text, 'html.parser')

            if 'text/html' in content_type:
                # Extract and print the links on the current HTML page
                links = soup.find_all('a', href=True)
                for link in links:
                    absolute_url = self.get_absolute_url(link['href'])
                    self.visited_links.add(absolute_url)
                    self.results.append({'url': absolute_url, 'content_type': 'html'})

                # Extract other relevant information from the page (customize as needed)
                title = soup.title.text.strip()
                self.results[-1]['title'] = title

            elif 'application/json' in content_type:
                # If the content is JSON, extract and print relevant information
                data = response.json()
                self.results.append({'url': url, 'content_type': 'json', 'data': data})

            # Add more content types and extraction logic as needed

            # Recursively crawl links found on the current page
            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                futures = [executor.submit(self.crawl, absolute_url, depth - 1) for absolute_url in self.get_links(soup)]
                for future in futures:
                    future.result()

        except Exception as e:
            print(f"Error crawling {url}: {e}")

    def get_absolute_url(self, relative_url):
        if relative_url.startswith("http://") or relative_url.startswith("https://"):
            return relative_url
        else:
            return f"{self.base_url.rstrip('/')}/{relative_url.lstrip('/')}"

    def get_links(self, soup):
        links = soup.find_all('a', href=True)
        return [self.get_absolute_url(link['href']) for link in links]

    def save_results(self, filename="crawler_results.json"):
        with open(filename, 'w') as file:
            json.dump(self.results, file, indent=2)
        print(f"Results saved to {filename}")

# Example usage
crawler = AdvancedWebCrawler("https://funquiz.online/")
start_url = "https://funquiz.online/"
crawler.crawl(start_url)
crawler.save_results()
