from .default_alert import DefaultAlert


class DangerAlert(DefaultAlert):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
