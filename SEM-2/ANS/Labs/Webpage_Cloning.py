import requests

def download_webpage(url, save_as):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Save the content to a file
        with open(save_as, 'w', encoding=response.encoding) as file:
            file.write(response.text)

        print(f"Webpage downloaded successfully and saved as '{save_as}'")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download the webpage: {e}")

# Usage
url = "https://youtube.com"  # Replace with the desired webpage URL
save_as = "webpage.html"     # Replace with the desired file name
download_webpage(url, save_as)