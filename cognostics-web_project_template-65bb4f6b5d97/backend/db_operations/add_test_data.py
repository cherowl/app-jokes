import src.models as models
from src.app import create_minimal_app
from src.database import db

app = create_minimal_app()
test_user = {
    'username': 'test',
    'password': 'test',
    'first_name': 'Jim',
    'last_name': 'Johnson'
}

with app.app_context():
    db.drop_all()
    db.create_all()

    user = models.User(**test_user)
    db.session.add(user)
    db.session.commit()
