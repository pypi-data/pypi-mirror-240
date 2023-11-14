from abc import ABC, abstractmethod

class GraphicParent(ABC):
    def __init__(self, application):
        self.application = application
        self.windows = []

    @abstractmethod
    def remove_window(self, window):
        raise NotImplementedError

    def append_window(self, window):
        self.windows.append(window)

    @abstractmethod
    def event_handler(self):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError