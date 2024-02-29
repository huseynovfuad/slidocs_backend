from .base import * #noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="F3sluwQ7m2ClNqe5vp_N2hZH8LLcPEfKnUyHMtQW2nHYblKMNsE"
)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DEBUG = True