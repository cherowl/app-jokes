from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

from src import models


class SchedulerManager:
    def __init__(self, app, sio):
        self.sio = sio
        self.app = app

        self.scheduler = BackgroundScheduler(timezone=utc)
        # example of broadcasting job which accesses db
        self.scheduler.add_job(self.broadcast_example, "interval",
                               name="Broadcast example", seconds=5)
        self.scheduler.start()

    def broadcast_example(self):
        # execute a db query under app_context
        with self.app.app_context():
            usernames = models.User.query.with_entities(models.User.username).all()
            # emit event "broadcast_example" to all users
            self.sio.emit("broadcast_example", usernames)
