from observer_pattern.INotificationObserver import INotificationObserver

class EmailNotifier(INotificationObserver):
    def __init__(self):
        pass
    def update(self, status: str) -> None:
        print(f"Order {status}. Email Notification sent")