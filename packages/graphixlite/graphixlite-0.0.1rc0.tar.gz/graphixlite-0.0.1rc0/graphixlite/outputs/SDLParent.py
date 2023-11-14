import sdl2
import sdl2.ext

from graphixlite.objects.GraphicParent import GraphicParent


class SDLParent(GraphicParent):
    def __init__(self, application):
        super().__init__(application)
        self.__nextID = 0

    def remove_window(self, window):
        self.windows.remove(window)
        window.get_graphical_output().window.close()

    def get_next_id(self):
        self.__nextID += 1
        return self.__nextID

    def append_window(self, window):
        self.windows.append(window)

    def event_handler(self):
        if self.application.running:
            sdl2.SDL_PumpEvents()
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    self.application.running = False
                elif event.type == sdl2.SDL_WINDOWEVENT:
                    if event.window.event == sdl2.SDL_WINDOWEVENT_CLOSE:
                        for window in self.windows:
                            if window.get_graphical_output().windowID == event.window.windowID:
                                self.remove_window(window)
                                break

    def update(self):
        pass  # not necessary for SDL2
