def is_string(value):
    return isinstance(value, str)


def is_integer(value):
    return isinstance(value, int)


def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    return False