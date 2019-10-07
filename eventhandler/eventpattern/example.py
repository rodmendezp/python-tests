from eventpattern import EventHook


# Classes for an example where you have a dataset and want to be notified when
# something changes

class Dataset:
    def __init__(self):
        self.modified = EventHook()

    def change_something(self):
        self.modified.fire()


class Controller:
    def __init__(self):
        self.__dataset = None

    def set_dataset(self, dataset):
        if self.__dataset is not None:
            self.__dataset.modified -= self.on_modified
        self.__dataset = dataset
        self.__dataset.modified += self.on_modified

    def on_modified(self):
        print('modified')


class MainClass:
    def __init__(self):
        self._controller = Controller()
        self.observers = [self._controller]

    def load_dataset(self, dataset):
        for observer in self.observers:
            observer.set_dataset(dataset)

