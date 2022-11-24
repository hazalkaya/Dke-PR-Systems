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