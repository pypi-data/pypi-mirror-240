from abc import ABC, abstractmethod
import graphixlite.CollisionEngine as CollisionEngine


class Drawable(ABC):
    def __init__(self, view, position, size, color, alpha, rotation):
        self.__view = view
        self.position = position
        self.size = size
        self.color = color
        self.alpha = alpha
        self.rotation = rotation
        self.collides_with = []
        self.type = "unknown"

    def add_collision(self, obj, callback):
        self.collides_with.append((obj, callback))

    def remove_collision(self, obj):
        for i in range(len(self.collides_with)):
            if self.collides_with[i][0] == obj:
                self.collides_with.pop(i)
                return

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.__view.was_updated = True

    def set_color(self, color):
        self.color = color
        self.__view.was_updated = True

    def set_position(self, position):
        self.position = position
        self.__view.was_updated = True

    def move_x(self, x):
        tmp = list(self.position)
        tmp[0] += x
        self.position = tuple(tmp)
        self.__view.was_updated = True

    def move_y(self, y):
        tmp = list(self.position)
        tmp[1] += x
        self.position = tuple(tmp)
        self.__view.was_updated = True

    def set_size(self, size):
        self.size = size
        self.__view.was_updated = True

    def set_rotation(self, rotation):
        self.rotation = rotation
        self.__view.was_updated = True

    def get_surface(self):
        return self.__view.get_surface()

    def get_view(self):
        return self.__view

    def get_graphical_output(self):
        return self.__view.get_graphical_output()

    @abstractmethod
    def draw(self):
        raise NotImplementedError

    def collides(self, other_drawable):
        return CollisionEngine.check_collision(self, other_drawable)

    def tick(self):
        for obj in self.collides_with:
            if self.collides(obj[0]):
                obj[1]()
