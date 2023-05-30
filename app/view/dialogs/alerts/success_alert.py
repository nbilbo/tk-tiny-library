from .default_alert import DefaultAlert


class SuccessAlert(DefaultAlert):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
