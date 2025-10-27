from flask import Blueprint, render_template, request

home_pb = Blueprint('home_route',__name__,template_folder='templates')

@home_pb.route('/')
def Bienvenido():

    if request.method == "GET":
        render_template('index.html')

    if request.method == "POST":
        user = request.form.get("nombre")

    return render_template('index.html')