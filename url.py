#!/usr/bin/env python3

import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        short_url = self.generate_short_url()
        self.url_mapping[short_url] = original_url
        return short_url

    def expand_url(self, short_url):
        return self.url_mapping.get(short_url, "URL not found")

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

def shorten_url(url_shortener):
    original_url = input("Enter the URL to shorten: ")
    short_url = url_shortener.shorten_url(original_url)
    print(f"Shortened URL: {short_url}")

def expand_url(url_shortener):
    short_url = input("Enter the short URL to expand: ")
    original_url = url_shortener.expand_url(short_url)
    print(f"Original URL: {original_url}")

def main():
    url_shortener = URLShortener()

    while True:
        print("\n1. Shorten URL")
        print("2. Expand URL")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            shorten_url(url_shortener)
        elif choice == '2':
            expand_url(url_shortener)
        elif choice == '3':
            print("Exiting the URL shortener. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
