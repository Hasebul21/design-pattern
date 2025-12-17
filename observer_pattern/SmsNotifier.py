from observer_pattern.INotificationObserver import INotificationObserver

class SmsNotifier(INotificationObserver):
    def __init__(self):
        pass

    def update(self, orderStatus : str) -> None:
        print(f"Order {orderStatus}. SMS Notification sent")