from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__, template_folder='template1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['name']
    dob = request.form['dob']
    age = int(request.form['age'])
    phone_no = int(request.form['phone_no'])
    p_lefteye = eval(request.form['p_lefteye'])
    r_righteye = eval(request.form['r_righteye'])
    cost = eval(request.form['cost'])
    type_spectials = request.form['type_spectials']
    spectials = {"tommy": 1450, "frameless": 1500, "frame": 1400}
    total_cost = cost + spectials[type_spectials]

    with open("b1.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, dob, age, phone_no, p_lefteye, r_righteye, spectials[type_spectials]])

    # Redirect to the receipt route with details as query parameters
    return redirect(url_for('receipt', name=name, dob=dob, age=age, phone_no=phone_no,
                            p_lefteye=p_lefteye, r_righteye=r_righteye, cost=cost,
                            spectials=spectials[type_spectials], total_cost=total_cost))

@app.route('/receipt')
def receipt():
    # Retrieve details from query parameters
    name = request.args.get('name')
    dob = request.args.get('dob')
    age = request.args.get('age')
    phone_no = request.args.get('phone_no')
    p_lefteye = request.args.get('p_lefteye')
    r_righteye = request.args.get('r_righteye')
    cost = request.args.get('cost')
    spectials = request.args.get('spectials')
    total_cost = request.args.get('total_cost')

    return render_template('receipt.html', name=name, dob=dob, age=age, phone_no=phone_no,
                           p_lefteye=p_lefteye, r_righteye=r_righteye, cost=cost,
                           spectials=spectials, total_cost=total_cost)

if __name__ == '__main__':
    app.run(debug=True)
