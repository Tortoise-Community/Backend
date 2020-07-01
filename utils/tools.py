from django.db.models.signals import post_save
from userdata.models import ServerUtils
from websitedata.models import News
from .handlers import SocketHandler, WebhookHandler
from django.conf import settings


bot_socket = SocketHandler(settings.BOT_SOCKET_IP,
                          int(settings.BOT_SOCKET_PORT),
                          settings.BOT_SOCKET_TOKEN)

webhook = WebhookHandler(settings.WEBHOOK_ID,
                         settings.WEBHOOK_SECRET)


def reload_rules(sender, **kwargs):
    bot_socket.signal("rules")

def reload_serverutils(sender, **kwargs):
    bot_socket.signal("serverutils")

post_save.connect(reload_rules, sender=News, dispatch_uid="news")
post_save.connect(reload_serverutils, sender=ServerUtils, dispatch_uid="server")