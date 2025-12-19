from decorator.BaseNotifier import BaseNotifier
from decorator.INotification import Notification

class WhatsAppNotifier(BaseNotifier):
    def __init__(self, notifier: Notification):
        super().__init__(notifier)

    def send(self) -> None:
        super().send()
        print("WHATSAPP Sent")