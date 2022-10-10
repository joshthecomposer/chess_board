from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html', x = 8 // 2 , _color1 = 'lightgray', _color2 = 'black')

@app.route('/<int:x>')
def one_input(x):
    return render_template('index.html',y = x // 2, x = x // 2,  _color1 = 'lightgray', _color2 = 'black')

@app.route('/<int:x>/<int:y>')
def two_input(x, y):
    return render_template('index.html', x = x // 2, y = y // 2, _color1 = 'lightgray', _color2 = 'black')

@app.route('/<int:x>/<int:y>/<string:_color1>/<string:_color2>')
def four_input(x, y, _color1, _color2):
    return render_template('index.html', x = x // 2, y = y // 2, _color1 = _color1, _color2 = _color2)

if __name__ == '__main__':
    app.run(debug=True)