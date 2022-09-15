from flask import Blueprint, render_template
from..extensions import db
from..models.uc import uc

#instanciar blueprint
ucBp = Blueprint('ucBp',__name__)

#declarar rota para blueprint
@ucBp.route('/uc')
def uc_list():
    # db.create_all() #- descomentar para criar o DB
    ucs_query= uc.query.all()
    return render_template('uc_list.html',ucs = ucs_query)