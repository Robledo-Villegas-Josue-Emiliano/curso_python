from flask import Flask

app = Flask(__name__)

@app.route('/') # Home or root of site
def index():
    return 'Hello World'

@app.route('/about') 
def about():
    return 'About Page'

if __name__ == '__main__':
    app.run(debug=True)


