from http.server import BaseHTTPRequestHandler

# Ensure this matches the ID the grader is looking for
EMAIL = "23f3001889@ds.study.iitm.ac.in" 

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # The tags are mandatory to stop Cloudflare from scrambling the text
        response_html = f"<html><body><h1>{EMAIL}</h1></body></html>"
        
        self.wfile.write(response_html.encode('utf-8'))
        return