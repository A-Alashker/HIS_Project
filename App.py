from flask import Flask, jsonify, render_template, request
from flask import Flask  
from datetime import datetime
from flask import session
from flask_migrate import Migrate
from models import clinic_db , Practitioner  , Patient , PractitionerRole , Appointment , UserAction  , DocumentReference

app = Flask(__name__ , template_folder='Templates', static_folder='CSS_Java')
app.secret_key = 'mypro'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ahmed5medo4/8@localhost/clinic_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
clinic_db.init_app(app) 

migrate = Migrate(app, clinic_db)

with app.app_context():
    clinic_db.create_all()  # Creates the tables in the database

# @app.route('/signn', methods=['GET', 'POST'])
# def Sign_up():
#     if request.method == 'POST':
#         # 1. Get form data
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']  #  In production, hash this!
#         role_code = request.form.get('role_code', 'physiotherapist')
#         organization = request.form.get('organization', '')
#         specialty = request.form.get('specialty', '')

#         # 2. Check if user already exists
#         existing_user = Practitioner.query.filter_by(email=email).first()
#         if existing_user:
#             return "Practitioner already exists", 400

#         # 3. Create new practitioner
#         new_practitioner = Practitioner(name=name, email=email, password=password)
#         clinic_db.session.add(new_practitioner)
#         clinic_db.session.commit()  # Commit to get ID

#         # 4. Assign role
#         new_role = PractitionerRole(
#             practitioner_id=new_practitioner.id,
#             role_code=role_code,
#             organization=organization,
#             specialty=specialty,
#             active=True,
#             start_date=datetime.utcnow()
#         )
#         clinic_db.session.add(new_role)

#         # 5. Log the action
#         action = UserAction(
#             user_id=new_practitioner.id,
#             action_type='create',
#             resource_type='Practitioner',
#             resource_id=str(new_practitioner.id),
#             description=f"Registered new practitioner with role '{role_code}'"
#         )
#         clinic_db.session.add(action)

#         clinic_db.session.commit()  # Commit both role and action

#         # 6. Start user session
#         session['user_id'] = new_practitioner.id
#         session['user_name'] = new_practitioner.name
#         session['user_email'] = new_practitioner.email
#         session['user_role'] = role_code

#         return "Sign-up successful and session started!", 200

#     return render_template('login.html')


@app.route('/')
def index():
    return render_template('sign up page.html')

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