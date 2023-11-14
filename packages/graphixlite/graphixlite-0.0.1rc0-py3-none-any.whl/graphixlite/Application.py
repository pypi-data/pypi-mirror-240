import graphixlite.ApplicationMeta
import graphixlite.PlatformMeta
import graphixlite.objects.Window
import graphixlite.objects.View
import graphixlite.outputs.SDLParent
import time


class Application:
    def __init__(self, appinfo):
        self.platformMeta = graphixlite.PlatformMeta.PlatformMeta()
        self.__appInfo = appinfo
        self.windows = []
        self.parent = None
        self.running = False
        self.graphic_parent = None
        self.target_fps = 60

    def remove_window(self, window):
        self.windows.remove(window)
        self.graphic_parent.remove_window(window)

    def append_window(self, window):
        self.windows.append(window)
        self.graphic_parent.append_window(window)

    def global_event_loop(self):
        target_fps = 0
        target_frame_time = 0

        while self.running:
            try:
                if self.target_fps != target_fps:
                    target_fps = self.target_fps
                    target_frame_time = 1 / target_fps
                self.graphic_parent.event_handler()
                for window in self.graphic_parent.windows:
                    window.get_graphical_output().update()
                self.event_loop()

                time.sleep(target_frame_time)
            except KeyboardInterrupt:
                self.running = False

    def run(self, parent=None):
        self.running = True
        if not parent:
            if self.platformMeta.graphical_output_string == "sdl2":
                self.graphic_parent = graphixlite.outputs.SDLParent.SDLParent(self)
            else:
                self.graphic_parent = graphixlite.outputs.WebParent.WebParent(self)
        else:
            self.parent = parent
            self.graphic_parent = self.parent.graphic_parent

    def event_loop(self):
        pass

    def get_app_info(self):
        return self.__appInfo
