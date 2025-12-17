from abc import ABC, abstractmethod
class INotificationObserver(ABC):
    @abstractmethod
    def update(self, orderStatus : str) -> None:
        ...
