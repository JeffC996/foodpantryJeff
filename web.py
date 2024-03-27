from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

# http://localhost:8000/fill/food/bread/france
@app.route('/fill/<type>/<category>/<brand>')
def fill(type, category, brand):
    return app.send_static_file('index.html')

#if __name__ == '__main__':
    #app.run(port=8000) the default port for app.run in Flask is 127.0.0.1, which doesn't allow external access.
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8000)