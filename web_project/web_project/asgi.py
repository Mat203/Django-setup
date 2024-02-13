import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from hello.consumers import YourConsumer

from django.urls import path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdev.settings')
django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws', YourConsumer.as_asgi())
        ])
    )
})