# from http.server import BaseHTTPRequestHandler

# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         message = 'Ayan Mullick'
#         self.wfile.write(message.encode())
#         return

from flask import Flask, Response, render_template
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
    return render_template('hello.html')