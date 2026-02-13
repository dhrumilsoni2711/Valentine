import socket

# DNS Client Configuration
DNS_SERVER_IP = '127.0.0.1'
DNS_SERVER_PORT = 53

def send_dns_query(domain_name):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Send the domain name as a query to the DNS server
    client_socket.sendto(domain_name.encode(), (DNS_SERVER_IP, DNS_SERVER_PORT))
    
    # Wait for the response
    response, _ = client_socket.recvfrom(512)
    
    # Print the resolved IP address
    print(f"Resolved IP address for {domain_name}: {response.decode()}")
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    # Example DNS queries
    send_dns_query("example.com")
    send_dns_query("google.com")
    send_dns_query("yahoo.com")
