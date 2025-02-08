import requests
import re

def find_m3u_links(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Use regex to find all .m3u links in the response text
        m3u_links = re.findall(r'https?://[^\s]+\.m3u', response.text)

        return m3u_links

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    url = input("Enter the URL to search for .m3u links: ")
    m3u_links = find_m3u_links(url)

    if m3u_links:
        print("Found .m3u links:")
        for link in m3u_links:
            print(link)
    else:
        print("No .m3u links found.")
