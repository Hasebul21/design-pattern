from decorator.INotification import Notification

class EmailNotifier(Notification):
    def __init__(self):
        pass

    def send(self) -> None:
        print("Email Sent")