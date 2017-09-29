from ..libs import WinForms

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
        self._container = self
        self._impl = WinForms.SplitContainer()

        # The default direction is vertical
        if self.direction == self.HORIZONTAL:
            self._impl.Orientation = WinForms.Orientation.Horizontal

            # self._impl._interface = self

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
        pass

    def _update_child_layout(self):
        """Force a layout update on the widget.
        """
        if self.content and self._impl.is_visible():
            if self.direction == SplitContainer.VERTICAL:
                size = self._impl.get_allocation().width
                if self._ratio is None:
                    self._ratio = 0.5
                    self._impl.set_position(size * self._ratio)
                self._containers[0]._update_layout(width=size * self._ratio)
                self._containers[1]._update_layout(width=size * (1.0 - self._ratio))
            else:
                size = self._impl.get_allcoation().height
                if self._ratio is None:
                    self._ratio = 0.5
                    self._impl.set_position(size * self._ratio)
                self._containers[0]._update_layout(height=size * self._ratio)
                self._containers[1]._update_layout(height=size * (1.0 - self._ratio))
