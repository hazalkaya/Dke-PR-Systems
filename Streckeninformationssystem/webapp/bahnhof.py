from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user

from . import db, abschnitt
from .forms import bahnhofFormBearbeiten, bahnhofFormLöschen, abschnittFormBearbeiten
from .modelsDatabase import Bahnhof, Abschnitt

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/edit_Bahnhöfe/<int:trainstations_id>', methods=['GET', 'POST'])
def edit_Bahnhöfe(trainstations_id):
    form = bahnhofFormBearbeiten()
    bahnhofBearbeiten = Bahnhof.query.get(trainstations_id)
    if form.validate_on_submit():
        bahnhofBearbeiten.name = form.name.data
        bahnhofBearbeiten.address = form.address.data
        db.session.commit()
        flash('Änderung gespeichert')
        return redirect('/bahnhöfe')
    elif request.method == 'GET':
        form.name.data = bahnhofBearbeiten.name
        form.address.data = bahnhofBearbeiten.address
    return render_template('bearbeiten_bahnhof.html', title='Bahnhof bearbeiten', user=current_user, form=form)

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

@views.route('/delete_b/<int:trainstations_id>', methods=['GET', 'POST'])
def delete_b(trainstations_id):
    bahnhofBearbeiten2 = Bahnhof.query.get(trainstations_id)
    db.session.delete(bahnhofBearbeiten2)
    db.session.commit()
    bahnhöfe = Bahnhof.query.all()
    return render_template("bahnhof.html", user=current_user, bahnhöfe=bahnhöfe)

@views.route('/edit_Abschnitt/<int:abschnitt_id>', methods=['GET', 'POST'])
def edit_Abschnitt(abschnitt_id):
    form =abschnittFormBearbeiten()
    abschnittBearbeiten = abschnitt.query.get(abschnitt_id)
    if form.validate_on_submit():
        abschnittBearbeiten.name = form.name.data
        abschnittBearbeiten.länge = form.länge.data
        abschnittBearbeiten.spurweite = form.spurweite.data
        abschnittBearbeiten.maxGeschwind = form.maxGeschwindigkeit.data
        db.session.commit()
        flash('Änderung gespeichert')
        return redirect('/abschnitte')
    elif request.method == 'GET':
        form.name.data = abschnittBearbeiten.name
        form.address.data = abschnittBearbeiten.address
    return render_template('bearbeiten_abschnitt.html', title='Abschnitt bearbeiten', user=current_user, form=form)

@views.route('/abschnitte', methods=['GET', 'POST'])
def get_abschnitte():
    if request.method == 'POST':
        a_name = request.form.get('a_name')
        a_länge = request.form.get('a_länge')

        abschnitt = Abschnitt.query.filter_by(name=a_name).first()
        if abschnitt:
            flash('Abschnitt existiert bereits', category='error')
        else:
            new_abschnitt = Abschnitt(name=a_name, länge=a_länge)
            db.session.add(new_abschnitt)
            db.session.commit()
            flash('Abschnitt HINZUGEFÜGT', category='success')

    abschnitt = Abschnitt.query.all()
    return render_template("abschnitt.html", user=current_user, abschnitt=abschnitt)

@views.route('/delete_a/<int:abschnitt_id>', methods=['GET', 'POST'])
def delete_a(abschnitt_id):
    abschnittBearbeiten2 = Abschnitt.query.get(abschnitt_id)
    db.session.delete(abschnittBearbeiten2)
    db.session.commit()
    abschnitt = Abschnitt.query.all()
    return render_template("abschnitt.html", user=current_user, abschnitt=abschnitt)