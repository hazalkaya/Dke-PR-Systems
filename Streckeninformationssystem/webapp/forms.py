from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class bahnhofFormBearbeiten(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Adresse', validators=[Length(min=1, max=150)])
    submit = SubmitField('ok')

class bahnhofFormLöschen(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Adresse', validators=[Length(min=1, max=150)])
    submit = SubmitField('löschen')

class abschnittFormBearbeiten(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    spurweite = StringField('Spurweite', validators=[Length(min=1, max=150)])
    maxGeschwindigkeit = StringField('maximale Geschwindigkeit', validators=[Length(min=1, max=150)])
    länge = StringField('Länge', validators=[Length(min=1, max=150)])
    submit = SubmitField('ok')

class bahnhofFormLöschen(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Adresse', validators=[Length(min=1, max=150)])
    submit = SubmitField('löschen')