from typing import List
from observer_pattern.INotificationObserver import INotificationObserver

class OrderSubject:
    def __init__(self):
        self.status = ""
        self.observers : List[INotificationObserver] = []

    def registerObserver(self, observer : INotificationObserver):
        self.observers.append(observer)

    def unregisterObserver(self, observer : INotificationObserver):
        self.observers.remove(observer)

    def notifyObservers(self, orderStatus : str):
        for observer in self.observers:
            observer.update(orderStatus)

    def setstate(self, state: str) -> None:
        self.status = state
        self.notifyObservers(state)



