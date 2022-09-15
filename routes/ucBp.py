from flask import Blueprint
from..extensions import db
from..models.uc import uc

#instanciar blueprint
ucBp = Blueprint('ucBp',__name__)

#declarar rota para blueprint
@ucBp.route('/uc')
def uc_list():
    db.create_all()