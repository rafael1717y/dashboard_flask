from model import *


def reportByState(state, disease):
    patients = db.session.query(db.func.count(Patient.estadoSaude), Patient.last_state, Patient.state).group_by(Patient.last_state).group_by(Patient.state)

    if state:
        patients = patients.filter(Patient.state==state)
    if disease:
        patients = patients.filter(Patient.diseases.any(Disease.id.in_(disease)))

    patients = patients.all()
    return [{
        'total': patient[0],
        'data': patient[1],
        'state': State.query.filter_by(id=patient[2]).first().name,
    } for patient in patients]