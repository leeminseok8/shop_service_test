import os

from dotenv import load_dotenv

load_dotenv()  # .env 파일을 읽어서 환경변수에 삽입

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["SHOP_DATABASE_NAME"],
        "USER": os.environ["SHOP_DATABASE_USER"],
        "PASSWORD": os.environ["SHOP_DATABASE_PASSWORD"],
        "HOST": os.environ["SHOP_DATABASE_HOST"],
        "PORT": int(os.environ.get("SHOP_DATABASE_PORT", "3306")),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

SECRET_KEY = os.environ["SHOP_SECRET_KEY"]
