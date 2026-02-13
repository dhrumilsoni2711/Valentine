import socket

def download_webpage(host, port=80):
    # Create a socket object (IPv4 and TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the host on port 80
        client_socket.connect((host, port))
        print(f"Connected to {host} on port {port}")

        # Create the HTTP GET request
        request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

        # Send the HTTP request
        client_socket.sendall(request.encode())

        # Receive and print the response
        response = b""
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data

        # Decode and save the response
        page_content = response.decode(errors='ignore')
        print(page_content)

        # Optionally, save to a file
        with open("downloaded_page.html", "w", encoding="utf-8") as f:
            f.write(page_content)

        print("\nWeb page downloaded and saved as 'downloaded_page.html'.")

    except Exception as e:
        print("Error:", e)

    finally:
        client_socket.close()

# Replace 'example.com' with any desired website
download_webpage("www.google.com")
