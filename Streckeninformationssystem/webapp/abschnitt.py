from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user

from . import db
from .forms import abschnittFormBearbeiten
from .modelsDatabase import Abschnitt

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/edit_abschnitt/<int:abschnitt_id>', methods=['GET', 'POST'])
def edit_Abschnitt(abschnitt_id):
    form = abschnittFormBearbeiten()
    abschnittBearbeiten = abschnitt_id.query.get(abschnitt_id)
    if form.validate_on_submit():
        abschnittBearbeiten.name = form.name.data
        abschnittBearbeiten.address = form.address.data
        db.session.commit()
        flash('Änderung gespeichert')
        return redirect('/bahnhöfe')
    elif request.method == 'GET':
        form.name.data = abschnittBearbeiten.name
        form.address.data = abschnittBearbeiten.address
    return render_template('bearbeiten_abschnitt.html', title='Abschnitt bearbeiten', user=current_user, form=form)

@views.route('/bahnhöfe', methods=['GET', 'POST'])
def get_Bahnhöfe():
    if request.method == 'POST':
        ts_name = request.form.get('ts_name')
        ts_address = request.form.get('ts_address')

        trainstation = Bahnhof.query.filter_by(name=ts_name).first()
        if trainstation:
            flash('Bahnhof existiert bereits', category='error')
        else:
            new_trainstation = Bahnhof(name=ts_name, address=ts_address)
            db.session.add(new_trainstation)
            db.session.commit()
            flash('Bahnhof HINZUGEFÜGT', category='success')

    bahnhöfe = Bahnhof.query.all()
    return render_template("bahnhof.html", user=current_user, bahnhöfe=bahnhöfe)

@views.route('/delete_Bahnhöfe', methods=['GET', 'POST'])
def delete_Bahnhöfe(bahnhofID):
    form2 = bahnhofFormLöschen()
    bahnhofBearbeiten2 = Bahnhof.query.get(bahnhofID)
    if form2.validate_on_submit():
        db.session.delete(bahnhofBearbeiten2)
        db.session.commit()
    bahnhöfe = Bahnhof.query.all()
    return render_template("bahnhof.html", user=current_user, bahnhöfe=bahnhöfe)

@views.route('/abschnitt', methods=['GET', 'POST'])
def get_Abschnitte():
    if request.method == 'POST':
        abschnitte_name = request.form.get('abschnitte_name')
        ts_address = request.form.get('ts_address')

        trainstation = Bahnhof.query.filter_by(name=ts_name).first()
        if trainstation:
            flash('Bahnhof existiert bereits', category='error')
        else:
            new_trainstation = Bahnhof(name=ts_name, address=ts_address)
            db.session.add(new_trainstation)
            db.session.commit()
            flash('Bahnhof HINZUGEFÜGT', category='success')

    bahnhöfe = Bahnhof.query.all()
    return render_template("bahnhof.html", user=current_user, bahnhöfe=bahnhöfe)