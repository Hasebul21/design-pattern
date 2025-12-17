from observer_pattern.INotificationObserver import INotificationObserver

class LoggerNotifier(INotificationObserver):
    def update(self, orderStatus : str) -> None:
        print(f"Order {orderStatus}. Logger notification updated")