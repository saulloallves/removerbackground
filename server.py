#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.request
import urllib.error
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class ProxyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        # Servir arquivos estáticos
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

    def do_POST(self):
        if self.path.startswith('/api'):
            # Proxy para rembg
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            
            # URL fixa - parâmetros já estão no form data
            rembg_url = 'http://localhost:5000/api/remove'
            
            try:
                req = urllib.request.Request(
                    rembg_url,
                    data=body,
                    headers={'Content-Type': self.headers['Content-Type']},
                    method='POST'
                )
                
                with urllib.request.urlopen(req, timeout=300) as response:
                    result = response.read()
                    self.send_response(200)
                    self.send_header('Content-Type', 'image/png')
                    self.end_headers()
                    self.wfile.write(result)
                    
            except urllib.error.URLError as e:
                self.send_response(502)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(f'Erro ao conectar com rembg: {e}'.encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(f'Erro: {e}'.encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    port = 8091
    server = HTTPServer(('0.0.0.0', port), ProxyHandler)
    print(f'Servidor rodando em http://0.0.0.0:{port}')
    server.serve_forever()
