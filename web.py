from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
<title>My Laptop Specifications</title>
<style>
  body { font-family: Arial, sans-serif; background: #f4f6f8; margin: 0; padding: 40px; }
  .card { max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.15); }
  h1 { text-align: center; color: #222; }
  table { width: 100%; border-collapse: collapse; margin-top: 20px; }
  td { padding: 12px; border-bottom: 1px solid #ddd; }
  td:first-child { font-weight: bold; width: 35%; color: #444; }
</style>
</head>
<body>
<div class="card">
<h1>Student Details</h1>
<table>
<tr><td>Name</td><td>Sharif Ahamed. S</td></tr>
<tr><td>Register Number</td><td>26019459</td></tr>
</table>
<h1>My Laptop Specifications</h1>
<table>
<tr><td>Name</td><td>Acer (TL15-53M-G2)</td></tr>
<tr><td>Processor</td><td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td></tr>
<tr><td>RAM</td><td>16 GB</td></tr>
<tr><td>Storage</td><td>477 GB</td></tr>
<tr><td>Operating System</td><td>Windows 11 Home Single Language</td></tr>
</table>
</div>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()