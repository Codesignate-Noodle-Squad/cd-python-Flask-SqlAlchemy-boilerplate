# manage.py
from flask.ext.script import Manager, Shell, Server
from app import app

manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())

@manager.command
def createdb():
    from models import db
    db.create_all()

if __name__ == "__main__":
	manager.run()