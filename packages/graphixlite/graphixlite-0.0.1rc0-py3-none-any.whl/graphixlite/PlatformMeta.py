import platform


def detectPlatform() -> str:
    system = platform.system()
    if system in ("Windows", "Linux", "Android", "iOS", "FreeBSD"):
        return system
    elif system == "Darwin":
        return "MacOS"
    elif system == "Emscripten":
        return "Browser"
    else:
        return "Unknown"


class PlatformMeta:
    def __init__(self):
        self.platform = detectPlatform()
        graphical_output = self.__get_available_graphical_output_type()
        self.graphical_output = graphical_output[1]
        self.graphical_output_string = graphical_output[0]

    def __get_available_graphical_output_type(self):
        try:
            if self.platform == "Browser":
                import graphixlite.outputs.WebWindow
                return "web", graphixlite.outputs.WebWindow.WebWindow
            import graphixlite.outputs.SDLWindow
            return "sdl2", graphixlite.outputs.SDLWindow.SDLWindow
        except Exception:
            raise Exception("No graphical output available for this platform")
