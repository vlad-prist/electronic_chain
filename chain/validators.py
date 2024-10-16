from rest_framework.serializers import ValidationError


def validate_debt(value):
    """ Нельзя изменять сумму задолженности при обновлении эксземпляра. """
    if value is not None:
        raise ValidationError("Нельзя изменять сумму задолженности.")
