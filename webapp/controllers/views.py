from flask import *

views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def main_route():
    return render_template('index.html')


@views.route('/user')
def user_route():
    return render_template('user.html')
