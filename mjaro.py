from flask import Flask
import os


app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))


@app.route('/')
def index():
    return '<h1>Hello</h1>'

@app.route('/about')
def about():
    return '<h1>About</h1>'

if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port, debug=True)
