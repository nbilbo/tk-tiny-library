from pathlib import Path

from app.view import Application
from app.controller import Controller
from app.model import Model


if __name__ == '__main__':
    db_path = Path('./db.json')
    model = Model(db_path)
    application = Application()
    controller = Controller(application, model)
    application.mainloop()
