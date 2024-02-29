import string
import random

chars = string.digits + string.ascii_letters


def code_generator(size, elements=chars):
    return "".join(random.choice(elements) for _ in range(size))


def create_code_shortcode(size, model_, elements=chars):
    new_code = code_generator(size=size, elements=elements)
    qs_exists = model_.objects.filter(code=new_code).exists()
    return create_code_shortcode(size, model_, elements=elements) if qs_exists else new_code