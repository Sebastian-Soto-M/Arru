from flask import Blueprint, render_template, url_for, request, flash

r_base = Blueprint('r_base', __name__,
                   template_folder='templates', static_folder='static')


@r_base.route('/')
def index():
    return render_template('views/index/core.html', title='Home')
