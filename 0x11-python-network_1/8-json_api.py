#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    
    response = requests.post(url, data=payload)
    
    try:
        json_response = response.json()
        
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
