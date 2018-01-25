from android.view import Gravity

from toga.constants import *

from .base import Widget


class TogaProgressBar(extends=android.widget.ProgressBar):
    @super({context: android.content.Context})
    def __init__(self, context, interface):
        self.interface = interface


class ProgressBar(Widget):
    def create(self):
        self.native = TogaProgressBar(self.app.native, self.interface)
        self.native.setSingleLine()
        # self.native = NSProgressIndicator.new()
        # self.native.style = NSProgressIndicatorBarStyle
        # self.native.displayedWhenStopped = True
        # Add the layout constraints
        self.add_constraints()
        self.rehint()

    def set_alignment(self, value):
        self.native.setGravity({
                                   LEFT_ALIGNED: Gravity.CENTER_VERTICAL | Gravity.LEFT,
                                   RIGHT_ALIGNED: Gravity.CENTER_VERTICAL | Gravity.RIGHT,
                                   CENTER_ALIGNED: Gravity.CENTER_VERTICAL | Gravity.CENTER_HORIZONTAL,
                                   JUSTIFIED_ALIGNED: Gravity.CENTER_VERTICAL | Gravity.CENTER_HORIZONTAL,
                                   NATURAL_ALIGNED: Gravity.CENTER_VERTICAL | Gravity.CENTER_HORIZONTAL,
                               }[value])

    def rehint(self):
        # print("REHINT label", self, self.native.getMeasuredWidth(), self.native.getMeasuredHeight())
        self.interface.style.hint(
            width=self.native.getMeasuredWidth() / self.app.device_scale,
            height=self.native.getMeasuredHeight() / self.app.device_scale,
        )

    def set_value(self, value):
        if value is not None:
            self.native.progress = value

    def start(self):
        if self.native and not self.interface._running:
            self.native.startAnimation(self.native)
            self.interface._running = True

    def stop(self):
        if self.native and self.interface._running:
            self.native.stopAnimation(self.native)
            self.interface._running = False

    def set_max(self, value):
        #if value:
            #self.native.indeterminate = False
        self.native.max = value
        #else:
           # self.native.indeterminate = True
