from .base import Widget


class SplitContainer(Widget):
    """ A SplitContainer displays two widgets vertically or horizontally
    next to each other with a movable divider.

    Args:
        id (str):  An identifier for this widget.
        style (:class:`colosseum.CSSNode`): An optional style object.
            If no style is provided then a new one will be created for the widget.
        direction: The direction for the container split,
            either `SplitContainer.HORIZONTAL` or `SplitContainer.VERTICAL`
        content(``list`` of :class:`toga.Widget`): The list of components to be split.
        factory (:obj:`module`): A python module that is capable to return a
            implementation of this class with the same name. (optional & normally not needed)
    """
    HORIZONTAL = False
    VERTICAL = True

    def __init__(self, id=None, style=None, direction=VERTICAL, content=None, factory=None):
        super().__init__(id=id, style=style, factory=factory)
        self._direction = direction
        self._containers = []

        # Create a platform specific implementation of a SplitContainer
        self._impl = self.factory.SplitContainer(interface=self)

        self.content = content
        self.direction = direction

    @property
    def content(self):
        """ The sub layouts of the `SplitContainer`.

        Returns:
            A ``list`` of :class:`toga.Widget`. Each element of the list
            is a sub layout of the `SplitContainer`

        Raises:
            ValueError: If the list is less than two elements long.
        """
        return self._content

    @content.setter
    def content(self, content):
        if content is None:
            self._content = None
            return

        if len(content) < 2:
            raise ValueError('SplitContainer content must have at least 2 elements')

        self._content = content

        for position, widget in enumerate(self._content):
            widget._update_layout()
            widget.app = self.app
            widget.window = self.window
            self._impl.add_content(position, widget._impl)

    def _set_app(self, app):
        if self._content:
            for content in self._content:
                content.app = self.app

    def _set_window(self, window):
        if self._content:
            for content in self._content:
                content.window = self.window

    @property
    def direction(self):
        """ The direction of the split

        Returns:
            True if `True` for vertical, `False` for horizontal.
        """
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
        self._impl.set_direction(value)
        self.rehint()
