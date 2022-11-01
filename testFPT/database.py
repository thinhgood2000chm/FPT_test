import os
from dotenv import load_dotenv
load_dotenv()
DATABASE = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("USER"),
        'PASSWORD':  os.getenv("PASSWORD"),
        'HOST':  os.getenv("HOST"),
        'PORT':  os.getenv("PORT"),
}

