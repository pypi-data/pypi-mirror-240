import graphixlite.objects.Drawable


class Line(graphixlite.objects.Drawable.Drawable):
    def __init__(self, view, position, size, color, alpha=255):
        super().__init__(view, position, size, color, alpha, 0)
        self.type = "line"

    def draw(self):
        if self.get_view().get_graphical_output_string() == "sdl2":
            self.get_graphical_output().draw_line(self.position, self.size, self.color, self.alpha)