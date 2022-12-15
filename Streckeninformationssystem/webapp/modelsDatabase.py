from flask_login import UserMixin
from . import db, marsh

class Benutzer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    admin = db.Column(db.Boolean, default=False)

class Bahnhof(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Bahnhof(name {self.name}, address {self.address})"

#Schemas für API
class BahnhofSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = Benutzer
        ordered = True
        fields = (
            "id",
            "email",
        )

user_schema = BahnhofSchema()
users_schema = BahnhofSchema(many=True)

class TrainstationSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = Bahnhof
        ordered = True
        fields = (
            "id",
            "name",
            "address"
        )

bahnhofSchema = TrainstationSchema()
bahnhöfeSchema = TrainstationSchema(many=True)

class Abschnitt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    spurweite = db.Column(db.Integer, nullable=False)
    maxGeschwindigkeit = db.Column(db.Integer, nullable=False)
    länge = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Abschnitt(name {self.name}, spurweite {self.spurweite}, maxGeschwindigkeit {self.maxGeschwindigkeit}, länge {self.länge})"


class AbschnittSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = Bahnhof
        ordered = True
        fields = (
            "id",
            "name",
            "spurweite",
            "maxGeschwindigkeit",
            "länge"
        )