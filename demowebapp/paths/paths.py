import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Get the role from environment variables to customize the page content
    role = os.getenv('ROLE', 'default')

    if role == 'IT':
        return """
            <h1>Welcome to the IT page!</h1>
            <p>Hello World!</p>
            <p>你好!</p>
            <p>こんにちは!</p>
            <p>สวัสดี!</p>
        """
    elif role == 'HR':
        return """
            <h1>Welcome to the HR page!</h1>
            <p>Hello HR team!</p>
            <p>¡Hola!</p>
            <p>Bonjour!</p>
            <p>Guten Tag!</p>
        """
    else:
        return """
            <h1>Welcome to the default page!</h1>
            <p>Content not available!</p>
        """

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5600))
    app.run(host='0.0.0.0', port=port)
