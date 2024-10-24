from flask import Flask, render_template, request, redirect, url_for
from utils import ageCalculate, bmi

from utils.machine_learning import predict

app = Flask(__name__)

name = None
surname = None
email = None
mobile= None

result = None

# Route for the first page
@app.route('/', methods=['GET', 'POST'])
def personal_info():
    if request.method == 'POST':
        # Retrieve form data
        global name
        name = request.form['name']
        global surname
        surname = request.form['surname']
        global email
        email = request.form['email']
        global mobile
        mobile = request.form['mobile']
        # Save data or process as needed
        # For now, we simply redirect to the next page with form data
        return redirect(url_for('additional_info'))
    return render_template('personal_info.html')

# Route for the second page
@app.route('/additional_info', methods=['GET', 'POST'])
def additional_info():
    if request.method == 'POST':
        # Retrieve form data
        # name = request.form['name'] # name
        # surname = request.form['surname'] # surname
        # email = request.form['email'] # email
        # mobile = request.form['mobile']  # mobile
        dob = request.form['dob'] # age 
        print("Hello {0} {1}".format(name, surname))
        age = ageCalculate.calculate_age(dob)
        print("your age is {0}".format(age))

        gender = request.form['gender'] # gender
        weight = request.form['weight'] # weight
        height = request.form['height'] # height
        chest_pain = request.form['chest_pain_type'] # chest pain type
        heart_rate = request.form['heart_rate'] # heart rate
        sys_bp = request.form['systolic_bp'] # Systolic Blood Pressure
        dia_bp = request.form['diastolic_bp'] # Diastolic Blood Pressure
        smoking = request.form['smoking'] # Smoking
        cygrets_per_day = request.form['cigarettes_per_day'] # Number of Cigarettes Per Day 
        diabetes = request.form['diabetes'] # Diabetes
        anaemia = request.form['anaemia'] # Anaemia
        past_heart_failure = request.form['past_heart_failure'] # Any Past Heart Failures
        spo2 = request.form['spo2_level'] # SpO2 Level 
        bpm = request.form['bpm'] # BPM (Heart Rate Classification)
        trop = request.form['Troponin_level'] # get troponin level
        
        bmi_val, status= bmi.calculate_bmi(weight, height) 
        print("your Body mass index is {0} and Status is {1}".format(int(bmi_val), status))
        print(chest_pain, heart_rate, sys_bp, dia_bp, cygrets_per_day, anaemia, past_heart_failure, spo2, bpm)

        result = predict(age, gender, weight, height, chest_pain, heart_rate, sys_bp, dia_bp, smoking, cygrets_per_day, diabetes, anaemia, past_heart_failure, spo2, bpm)

        print(result)
        # Process or save the data as needed
        # return f"Hello :{name}\n, Surname:{surname}\n, Results: {result}"
        return redirect(url_for('show_result', trop=trop, gen=gender, name=name, surname=surname, result=result[0], h_score = result[1], d_score = result[2], age=age, bmi_val=bmi_val, bmi_status=status))
    return render_template('additional_info.html')

@app.route('/result', methods=['GET', 'POST'])
def show_result():
    gen = request.args.get('gen')
    if gen == '1':
        gen = "Male"
    else:
        gen = "Female"

    age = request.args.get('age')
    bmi_val = request.args.get('bmi_val')
    # bmi_val = int(bmi_val)

    bmi_status = request.args.get('bmi_status')
    name = request.args.get('name').title()
    surname = request.args.get('surname').title()
    h_score = request.args.get('h_score')
    d_score = request.args.get('d_score')
    result = request.args.get('result')
    trop = request.args.get('trop')
    trop = int(trop)*10
    return render_template('result.html', troponin_level=trop, u_name=name, u_surname=surname, gen=gen, age=age, bmi_val=bmi_val, bmi_status=bmi_status, h_score=h_score, d_score=d_score,result_status=result)

if __name__ == '__main__':
    app.run(debug=True)
