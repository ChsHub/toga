from android.view import Gravity

from toga.constants import *

from .base import WidgetMixin


class TogaLabel(extends=android.widget.TextView):
    @super({context: android.content.Context})
    def __init__(self, context, interface):
        self.interface = interface


class Label(Widget):
    def create(self):
        self.native = TogaLabel(self.app.native, self.interface)
        self.native.setSingleLine()

    def set_alignment(self, value):
        self.native.setGravity({
                LEFT_ALIGNED: Gravity.CENTER_VERTICAL | Gravity.LEFT,
                RIGHT_ALIGNED: Gravity.CENTER_VERTICAL | Gravity.RIGHT,
                CENTER_ALIGNED: Gravity.CENTER_VERTICAL | Gravity.CENTER_HORIZONTAL,
                JUSTIFIED_ALIGNED: Gravity.CENTER_VERTICAL | Gravity.CENTER_HORIZONTAL,
                NATURAL_ALIGNED: Gravity.CENTER_VERTICAL | Gravity.CENTER_HORIZONTAL,
            }[value])

    def set_text(self, value):
        self.native.setText(value)

    def rehint(self):
        # print("REHINT label", self, self.native.getMeasuredWidth(), self.native.getMeasuredHeight())
        self.interface.style.hint(
            width=self.native.getMeasuredWidth() / self.app.device_scale,
            height=self.native.getMeasuredHeight() / self.app.device_scale,
        )
