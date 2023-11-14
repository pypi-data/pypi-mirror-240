import graphixlite.objects.View


class Window:
    def __init__(self, application, **kwargs):
        self.application = application
        self.title = kwargs.get("title", "PyGraphix Window")
        self.width = kwargs.get("width", 800)
        self.height = kwargs.get("height", 600)
        self.background_color = kwargs.get("background_color", (255, 255, 255))

        self.__view = graphixlite.objects.View.View(self)
        self.__output = self.get_available_graphical_output()

    def set_title(self, title):
        self.title = title
        self.__output.refresh_properties()

    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.__output.refresh_properties()

    def get_graphical_output(self):
        return self.__output

    def get_view(self):
        return self.__view

    def set_background_color(self, color):
        self.background_color = color
        self.__output.refresh_properties()

    def get_available_graphical_output(self):
        if self.application.platformMeta.graphical_output_string == "sdl2":
            return self.application.platformMeta.graphical_output(self)
