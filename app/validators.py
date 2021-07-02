from django.forms import ValidationError

class TamanoMaximoValidator:

    def __init__(self, maxfile=3):
        self.maxfile = maxfile

    def __call__(self, value):
        tamano = value.size
        maxfiletamano = self.maxfile * 1048576

        if tamano > maxfiletamano:
            raise ValidationError(f"El tamano maximo del archivo debe ser de {self.maxfile}MB")

        return value