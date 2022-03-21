from flask import Flask, render_template, request, url_for, flash, redirect
from scipy.fftpack import shift
from engine import Route

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        number = int(request.form['numberValue'])
        addresses = []
        shifts = []
        for i in range(0, number):
            address = str(request.form[f'address{i}'])
            if len(address) > 0:
                addresses.append(address)
            start = int(request.form[f'start{i}'])
            end = int(request.form[f'end{i}'])
            shift_range = (start, end)
            shifts.append(shift_range)
        data = {
            'vehicles': int(request.form['vehicles']),
            'waitingtime': int(request.form['waitingtime']),
            'maxshifttime': int(request.form['maxshifttime'])
        }
        res = Route(addresses, shifts, data).addresses
        return render_template('index.html', res=res)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
