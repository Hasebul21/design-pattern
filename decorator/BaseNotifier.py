from abc import ABC
from decorator.INotification import Notification

class BaseNotifier(Notification):
    def __init__(self, notification : Notification):
        self._notification = notification
        
    def send(self) -> None:
        self._notification.send()