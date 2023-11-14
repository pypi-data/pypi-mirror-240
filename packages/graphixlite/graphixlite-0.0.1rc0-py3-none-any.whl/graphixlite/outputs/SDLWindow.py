import sdl2
import sdl2.ext

from graphixlite.objects.GraphicOutput import GraphicOutput


class SDLWindow(GraphicOutput):
    def __init__(self, window_object):
        super().__init__(window_object)

        self.__window_object = window_object
        sdl2.ext.init()
        self.windowID = self.__window_object.application.graphic_parent.get_next_id()
        self.window = sdl2.ext.Window(self.__window_object.title,
                                      size=(self.__window_object.width, self.__window_object.height))
        self.window.show()

        self.__running = True

    def refresh_properties(self):
        self.window.title = self.__window_object.title
        self.window.size = (self.__window_object.width, self.__window_object.height)
        self.update()

    def get_graphic_parent(self):
        return self.__window_object.application.graphic_parent

    def get_surface(self):
        try:
            return self.window.get_surface()
        except Exception:
            self.close()

    def draw_at(self, position, color, alpha):
        surface = self.get_surface()
        if not surface:
            return
        pixel = sdl2.ext.pixels2d(surface)
        try:
            pixel[position[0]][position[1]] = sdl2.ext.Color(color[0], color[1], color[2], alpha)
        except IndexError:
            pass

    def draw_rectangle(self, position, size, color, alpha):
        surface = self.get_surface()
        if not surface:
            return
        sdl2.ext.fill(surface, sdl2.ext.Color(color[0], color[1], color[2], alpha),
                      (position[0], position[1], size[0], size[1]))

    def draw_circle(self, position, radius, color, alpha):
        surface = self.get_surface()
        if not surface:
            return
        sdl2.ext.fill(surface, sdl2.ext.Color(color[0], color[1], color[2], alpha),
                      (position[0], position[1], radius, radius))

    def draw_line(self, position, width, color, alpha):
        surface = self.get_surface()
        if not surface:
            return
        sdl2.ext.line(surface, sdl2.ext.Color(color[0], color[1], color[2], alpha),
                      (position[0], position[1], position[2], position[3]), width)

    def close(self):
        self.__running = False
        self.window.close()
        self.__window_object.application.remove_window(self.__window_object)

    def update(self, force_refresh=False):
        if not self.__running:
            return
        view = self.__window_object.get_view()
        view.tick()
        if force_refresh or self.__window_object.get_view().was_updated:
            surface = self.get_surface()
            if not surface:
                return self.close()
            bg = self.__window_object.background_color
            sdl2.ext.fill(surface, sdl2.ext.Color(bg[0], bg[1], bg[2]))
            view.draw()
            self.window.refresh()
