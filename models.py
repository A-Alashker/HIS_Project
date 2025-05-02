from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, time
import enum

clinic_db = SQLAlchemy()

# ENUM DEFINITIONS
class GenderEnum(enum.Enum):
    male = "male"
    female = "female"

class AppointmentStatusEnum(enum.Enum):
    booked = "booked"
    fulfilled = "fulfilled"
    cancelled = "cancelled"

class PractitionerRoleEnum(enum.Enum):
    doctor = "doctor"
    receptionist = "receptionist"
    physiotherapist = "physiotherapist"

# -------------------------------
# FHIR RESOURCES AS SQL MODELS
# -------------------------------

# PATIENT
class Patient(clinic_db.Model):
    __tablename__ = 'patients'
    id = clinic_db.Column(clinic_db.Integer, primary_key=True)
    identifier = clinic_db.Column(clinic_db.String(64), unique=True)  # FHIR id
    name = clinic_db.Column(clinic_db.String(100), nullable=False)
    gender = clinic_db.Column(clinic_db.Enum(GenderEnum))
    birthDate = clinic_db.Column(clinic_db.Date)
    phone = clinic_db.Column(clinic_db.String(20))
    email = clinic_db.Column(clinic_db.String(100))
    address = clinic_db.Column(clinic_db.String(255))
    occupation = clinic_db.Column(clinic_db.String(100))  

  # Relationships
    appointments = clinic_db.relationship("Appointment", back_populates="patient")
    document_references = clinic_db.relationship("DocumentReference", back_populates="patient")


# PRACTITIONER
class Practitioner(clinic_db.Model):
    __tablename__ = 'practitioners'
    id = clinic_db.Column(clinic_db.Integer, primary_key=True)
    name = clinic_db.Column(clinic_db.String(100), nullable=False)
    email = clinic_db.Column(clinic_db.String(100), unique=True)
    contact_number = clinic_db.Column(clinic_db.String(11), unique=True)
    password = clinic_db.Column(clinic_db.String(255), nullable=False)  # Should be hashed

    # Roles relationship
    roles = clinic_db.relationship("PractitionerRole", back_populates="practitioner")
    appointments = clinic_db.relationship("Appointment", back_populates="practitioner")

# PRACTITIONER_Role
class PractitionerRole(clinic_db.Model):
    __tablename__ = 'practitioner_roles'
    id = clinic_db.Column(clinic_db.Integer, primary_key=True)

    practitioner_id = clinic_db.Column(clinic_db.Integer, clinic_db.ForeignKey('practitioners.id'), nullable=False)
    role_code = clinic_db.Column(clinic_db.String(100), nullable=False)  # e.g., 'physiotherapist'
    active = clinic_db.Column(clinic_db.Boolean, default=True)
    start_date = clinic_db.Column(clinic_db.Date)
    end_date = clinic_db.Column(clinic_db.Date)

    practitioner = clinic_db.relationship("Practitioner", back_populates="roles")


# USERACTION

class UserAction(clinic_db.Model):
    __tablename__ = 'user_actions'
    id = clinic_db.Column(clinic_db.Integer, primary_key=True)
    
    user_id = clinic_db.Column(clinic_db.Integer, clinic_db.ForeignKey('practitioners.id'), nullable=False)
    action_type = clinic_db.Column(clinic_db.String(50), nullable=False)  # e.g., 'create', 'update', 'read', 'login'
    resource_type = clinic_db.Column(clinic_db.String(50))  # e.g., 'Patient', 'Appointment'
    resource_id = clinic_db.Column(clinic_db.String(64))  # ID of the affected resource
    timestamp = clinic_db.Column(clinic_db.DateTime, default=datetime.utcnow, nullable=False)
    description = clinic_db.Column(clinic_db.String(255))  # Optional human-readable action summary

    user = clinic_db.relationship("Practitioner")  # Assuming 'Practitioner' represents the user



# APPOINTMENT
class Appointment(clinic_db.Model):
    __tablename__ = 'appointments'
    id = clinic_db.Column(clinic_db.Integer, primary_key=True)

    status = clinic_db.Column(clinic_db.Enum(AppointmentStatusEnum), default=AppointmentStatusEnum.booked, nullable=False)
    start = clinic_db.Column(clinic_db.Time, nullable=False)
    end = clinic_db.Column(clinic_db.Time , nullable=False)  # FHIR: end
    cancellation_date = clinic_db.Column(clinic_db.DateTime)  # FHIR: cancellationDate
    created = clinic_db.Column(clinic_db.DateTime, default=datetime.utcnow)  # FHIR: created

    reason = clinic_db.Column(clinic_db.String(500))

    patient_id = clinic_db.Column(clinic_db.Integer, clinic_db.ForeignKey('patients.id'), nullable=False)
    practitioner_id = clinic_db.Column(clinic_db.Integer, clinic_db.ForeignKey('practitioners.id'), nullable=False)

    patient = clinic_db.relationship("Patient", back_populates="appointments")
    practitioner = clinic_db.relationship("Practitioner", back_populates="appointments")



class DocumentReference(clinic_db.Model):
    __tablename__ = 'document_references'
    id = clinic_db.Column(clinic_db.Integer, primary_key=True)
    type = clinic_db.Column(clinic_db.String(100))  # e.g., "SOAP Note", "Referral Letter"
    
    content_type = clinic_db.Column(clinic_db.String(50), default='text/plain')  # <-- Default is plain text

    content = clinic_db.Column(clinic_db.Text, nullable=False)  # <-- Changed to clinic_db.Text for plain text
    description = clinic_db.Column(clinic_db.String(255))  # Short summary or title
    date = clinic_db.Column(clinic_db.DateTime, default=datetime.utcnow)

    patient_id = clinic_db.Column(clinic_db.Integer, clinic_db.ForeignKey('patients.id'), nullable=False)
    patient = clinic_db.relationship("Patient", back_populates="document_references")
