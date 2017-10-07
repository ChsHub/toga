from ..libs import WinForms
from System.Drawing import Point

from toga.interface import SplitContainer as SplitContainerInterface

from ..container import Container
from .base import WidgetMixin


class SplitContainer(SplitContainerInterface, WidgetMixin):
    _CONTAINER_CLASS = Container

    def __init__(self, id=None, style=None, direction=SplitContainerInterface.VERTICAL):
        super().__init__(id=id, style=style, direction=direction)
        self._create()
        self._ratio = None

    def create(self):
        self._impl = WinForms.SplitContainer()

    def _add_content(self, position, container):

        if position == 0:
            self._impl.Panel1.Controls.Add(container._impl)
        elif position == 1:
            self._impl.Panel2.Controls.Add(container._impl)
        else:
            raise ValueError('SplitContainer content must be a 2-tuple')

    def _set_app(self, app):
        if self._content:
            self._content[0].app = self.app
            self._content[1].app = self.app

    def _set_window(self, window):
        if self._content:
            self._content[0].window = self.window
            self._content[1].window = self.window

    def _set_direction(self, value):

        if self.direction == self.HORIZONTAL:
            self._impl.Orientation = WinForms.Orientation.Horizontal
        elif self.direction == self.VERTICAL:
            self._impl.Orientation = WinForms.Orientation.Vertical
        else:
            raise ValueError('Direction must be SplitContainer.VERTICAL or SplitContainer.HORIZONTAL')

    def _update_child_layout(self):
        """Force a layout update on the widget.
        """
        if self.content and self._impl.Visible:
            if self._ratio is None:
                self._ratio = 0.5

            if self.direction == SplitContainer.VERTICAL:
                size = self._impl.Width
                #self._impl.Location = Point(size * self._ratio)
                # self._impl.set_position(size * self._ratio)
                self._containers[0]._update_layout(width=size * self._ratio)
                self._containers[1]._update_layout(width=size * (1.0 - self._ratio))
            else:
                size = self._impl.Height
               # self._impl.Location = Point(size * self._ratio)
                # self._impl.set_position(size * self._ratio)
                self._containers[0]._update_layout(height=size * self._ratio)
                self._containers[1]._update_layout(height=size * (1.0 - self._ratio))
        return
        if self.content:
            for i, (container, content) in enumerate(zip(self._containers, self.content)):
                #frame = container._impl.frame
                content._update_layout(
                    width=self._impl.Height,
                    height=self._impl.Height
                )


        return

