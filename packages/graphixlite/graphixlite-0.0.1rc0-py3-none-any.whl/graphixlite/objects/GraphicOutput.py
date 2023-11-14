from abc import ABC, abstractmethod


class GraphicOutput(ABC):
    def __init__(self, window_object):
        self.__window_object = window_object

    def get_view(self):
        return self.__window_object.get_view()

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def refresh_properties(self):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @abstractmethod
    def draw_at(self, position, color, alpha):
        raise NotImplementedError
