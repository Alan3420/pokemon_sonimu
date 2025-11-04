from flask import Blueprint, render_template, request
from app.forms.trainer_form import TrainerForm
home_pb = Blueprint('home_route',__name__,template_folder='templates')

@home_pb.route('/')
def Bienvenido():
    # form = TrainerForm()

    # if form.validate_on_submit():
    #     trainer = form.trainer.data
    #     error = False

    if request.method == "GET":
        render_template('index.html')

    if request.method == "POST":
        user = request.form.get("nombre")

    return render_template('index.html')