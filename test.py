from app import app
from app import db, models

if __name__ == '__main__':
    # print('See environment: ', os.environ['FLASK_APP'])
    # app.run() 
    db.create_all()
    u = models.User(id='357970')
    db.session.add(u)
    db.session.commit()

    users = models.User.query.all()
    print(users)
    for u in users:
        print(u.id)