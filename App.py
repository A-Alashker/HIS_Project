from flask import Flask, jsonify, render_template, request

app = Flask(__name__ , template_folder='Templates', static_folder='CSS_Java')

@app.route('/')
def index():
    return render_template('General_Dash.html')

# @app.route('/Login')
# def Login():
#     return render_template('login.html')

@app.route('/sign')
def SignUP():
    return render_template('sign up page.html')

@app.route('/patients')
def patients_Info():
    return render_template('Patient_Info1.html')

@app.route('/add_patient')
def add_patient():
    return render_template('AdPatient.html')

@app.route('/Patient_Dashboard')
def Patient_Dash():
    return render_template('Patient_Dash.html')

@app.route('/Schedule')
def Schedule():
    return render_template('Schedule_Dash.html')

@app.route('/Appointment')
def Appointment():
    return render_template('addappointment.html')





if __name__ == '__main__':
    app.run(debug=True)