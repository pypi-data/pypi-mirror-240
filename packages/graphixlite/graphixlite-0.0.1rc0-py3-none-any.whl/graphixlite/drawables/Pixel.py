import graphixlite.objects.Drawable


class Pixel(graphixlite.objects.Drawable.Drawable):
    def __init__(self, view, position, color, alpha=255):
        super().__init__(view, position, (1, 1), color, alpha, 0)
        self.type = "pixel"

    def draw(self):
        self.get_graphical_output().draw_at(self.position, self.color, self.alpha)

