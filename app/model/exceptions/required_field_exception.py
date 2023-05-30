class RequiredFieldException(Exception):
    def __init__(self, field: str) -> None:
        self.field = field
        super().__init__(f'The field {self.field} is required.')
