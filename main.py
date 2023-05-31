from pathlib import Path

from app.view import Application
from app.controller import Controller
from app.model import Model


if __name__ == '__main__':
    db_path = Path('./db.json')
    model = Model(db_path)
    application = Application()
    application.set_database_label_text(model.db_path.name)
    controller = Controller(application, model)
    application.mainloop()
