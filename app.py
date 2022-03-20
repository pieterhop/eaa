from flask import Flask, render_template, request, url_for, flash, redirect
from engine import Route

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        number = int(request.form['numberValue'])
        addresses = []
        for i in range(0, number):
            address = str(request.form[f'address{i}'])
            if len(address) > 0:
                addresses.append(address)
        res = Route(addresses).addresses
        return render_template('index.html', res=res)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
