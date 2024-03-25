from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

# http://localhost:8000/fill/food/bread/france
@app.route('/fill/<type>/<category>/<brand>')
def fill(type, category, brand):
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=8000)