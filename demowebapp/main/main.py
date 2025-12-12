import os
from flask import Flask, redirect , request

app = Flask(__name__)
domain = "theantechs.com"
localhost = '127.0.0.1'

# Define role-based access control based on path
@app.route('/')
def index():
    return """
        <h1>Welcome to your company page!</h1>
        <p><a href="/it">IT admin</a> space </p>
        <p><a href="/hr">HR admin</a> space</p>
        <p><a href="/gamers">Gamers</a> space</p>
        <p><a href="/headers">This is the requst headers</a> space</p>
    """

@app.route('/it')
def page_it():
    # Redirect to a different URL, e.g., http://it.yourdomain.com:8080
    #return redirect(f"http://{localhost}:5600", code=302)
    return redirect(f"http://it.{domain}", code=302)

@app.route('/hr')
def page_hr():
    # Redirect to a different URL for HR, e.g., another service or page
    #return redirect(f"http://{localhost}:5700", code=302)
    return redirect(f"http://hr.{domain}", code=302)

@app.route('/gamers')
def page_gamers():
    # Redirect to a different URL for HR, e.g., another service or page
    #return redirect(f"http://{localhost}:5700", code=302)
    return redirect(f"http://gamers.{domain}", code=302)

@app.route('/headers')
def headers():
    headers = request.headers
    headers_html = "<h1>HTTP Request Headers</h1><ul>"
    for key, value in headers.items():
        headers_html += f"<li><strong>{key}:</strong> {value}</li>"
    headers_html += "</ul>"
    
    return headers_html, 200, {"Content-Type": "text/html"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
