from application import db
from application.models import outfit

db.drop_all()
db.create_all()
