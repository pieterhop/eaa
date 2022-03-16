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
        print(addresses)
        data = Route(addresses).addresses
        return render_template('index.html', data=data)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


# TODO
# Zorgen dat alle print statements in de pretty print functie in Route() niet printen maar returnen zodat het in de index.html kan worden laten zien