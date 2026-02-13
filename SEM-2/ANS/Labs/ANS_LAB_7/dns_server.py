import socket

# DNS Server Configuration
DNS_SERVER_IP = '127.0.0.1'  # Localhost for testing
DNS_SERVER_PORT = 53  # Standard DNS port

# Function to simulate DNS resolution
def resolve_domain(domain_name):
    # For simplicity, we map domain names to IPs
    # In a real DNS server, this would query a database or perform a more complex resolution process
    dns_records = {
        "example.com": "93.184.216.34",  # Hardcoded example
        "google.com": "8.8.8.8",  # Google's public DNS server
        "yahoo.com": "98.137.246.8"
    }
    
    # Return IP if domain exists, otherwise return a default error message
    return dns_records.get(domain_name, "0.0.0.0")

def start_dns_server():
    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the DNS server address and port
    server_socket.bind((DNS_SERVER_IP, DNS_SERVER_PORT))
    print(f"DNS Server listening on {DNS_SERVER_IP}:{DNS_SERVER_PORT}")
    
    while True:
        # Receive the query from the client
        query, client_address = server_socket.recvfrom(512)  # 512 bytes for DNS query
        
        print(f"Received query from {client_address}")
        
        # Parse the query (for simplicity, let's assume it's a domain name in the query)
        domain_name = query.decode().strip()  # A real DNS would decode it properly
        
        # Resolve the domain name
        ip_address = resolve_domain(domain_name)
        
        # Send the response back to the client
        server_socket.sendto(ip_address.encode(), client_address)
        print(f"Sent response: {ip_address} to {client_address}")

if __name__ == "__main__":
    start_dns_server()
