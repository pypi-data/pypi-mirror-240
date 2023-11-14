import string
import random

class View:
    def __init__(self, window_object):
        self.__window_object = window_object
        self.was_updated = True

        self.__objects = {}

    def append(self, obj, obj_id=None):
        if not obj_id:
            obj_id = "".join(random.choices(string.ascii_lowercase, k=10))
        self.__objects[obj_id] = obj
        self.was_updated = True

    def iterate_objects(self):
        for obj in self.__objects.items():
            yield obj

    def get_object(self, obj_id):
        if obj_id in self.__objects:
            return self.__objects[obj_id]

    def draw(self):
        for obj in self.__objects.values():
            obj.draw()
        self.was_updated = False

    def tick(self):
        for obj in self.__objects.values():
            obj.tick()

    def get_graphical_output_string(self):
        return self.__window_object.application.platformMeta.graphical_output_string

    def get_graphical_output(self):
        return self.__window_object.get_graphical_output()

    def get_window_object(self):
        return self.__window_object

    def get_surface(self):
        return self.__window_object.get_surface()
