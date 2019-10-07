# https://en.wikipedia.org/wiki/Observer_pattern


class Observable:
    def __init__(self) -> None:
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observer(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)


class Observer:
    def __init__(self, observable):
        observable.register_observer(self)

    def notify(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)
