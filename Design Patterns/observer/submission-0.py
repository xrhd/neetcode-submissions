class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self._subscribers = set()

    def subscribe(self, observer: Observer) -> None:
        self._subscribers.add(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._subscribers:
            self._subscribers.remove(observer)

    def notify_subs(self):
        for ob in self._subscribers:
            ob.notify(self.itemName)

    def updateStock(self, newStock: int) -> None:
        old, self.stock = self.stock, newStock
        if old == 0 and self.stock > 0:
            self.notify_subs()
        
