from application import db
from application.models import Tops, Bottoms

db.drop_all()
db.create_all()
