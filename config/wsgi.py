"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application
import requests
import time
import threading

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = Cling(get_wsgi_application())

def awake():
    while True:
        try:
            print("Start Awaking")
            requests.get("https://memo-blog.herokuapp.com/")
            print("End")
        except:
            print("error")
        time.sleep(300)

t=threading.Thread(target=awake)
t.start()



