from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the HTTP request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)  # HTTP status code 200 OK
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the HTML response
        self.wfile.write(b"<html><body><h1>Welcome to the app!</h1></body></html>")

# Define the main function to run the server
def run():
    # Specify the server address and port
    server_address = ('', 8000)  # Use an empty string for the host to listen on all available interfaces
    # Create an instance of HTTPServer with the specified handler class
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Server is running...')
    # Start the HTTP server
    httpd.serve_forever()

# Run the server
if __name__ == '__main__':
    run()