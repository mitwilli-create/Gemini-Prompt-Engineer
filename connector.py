# connector.py
import os
import requests
import json

def fetch_prompt_engineering_trends():
    """
    Connects to the GitHub API to fetch repositories
    related to 'prompt engineering'.
    """
    api_key = os.getenv("GITHUB_API_KEY")
    if not api_key:
        raise ValueError("Error: GITHUB_API_KEY environment variable not set.")

    search_url = "https://api.github.com/search/repositories"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {api_key}"
    }
    params = {
        "q": "prompt engineering",
        "sort": "stars",
        "order": "desc"
    }

    print("Fetching data from GitHub...")
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status() 

    return response.json()

if __name__ == "__main__":
    try:
        data = fetch_prompt_engineering_trends()
        print("Successfully fetched data!")
        print(f"Found {len(data['items'])} total results.")
        
        # Print the full name and star count of the top 5 repositories
        for item in data['items'][:5]:
            print(f"  - {item['full_name']} (Stars: {item['stargazers_count']})")
    except Exception as e:
        print(f"An error occurred: {e}")