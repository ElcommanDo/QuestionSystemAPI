import random
import string

ALPHA_LENGTH = 6
ALPHA_CHARS = string.ascii_lowercase + string.digits


def generate_random_string(length=ALPHA_LENGTH, chars=ALPHA_CHARS):
    return ''.join(random.choice(chars) for _ in range(length))
