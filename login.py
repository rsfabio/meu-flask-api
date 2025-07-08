from flask import Blueprint, render_template, request

bp_login = Blueprint('login', __name__, template_folder='templates')


@bp_login.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html')
