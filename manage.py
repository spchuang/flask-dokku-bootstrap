from flask.ext.script import Manager
from flask import url_for, current_app
from app import create_app
from app.extensions import db
from app.config import DefaultConfig
import os

def create_my_app(config):
   app = create_app(config=DefaultConfig)
   return app

manager = Manager(create_my_app)

manager.add_option('-c', '--config',
                   dest="config",
                   required=False,
                   help="config [local, dev, prod]")


@manager.command
def run():
    """Run in local machine."""
    port = int(os.environ.get("PORT", 5000))
    current_app.run(host='0.0.0.0', port=port, debug=True)


@manager.command
def initdb():
    """Init/reset database."""
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    manager.run()