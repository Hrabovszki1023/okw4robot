from ..base.base_widget import BaseWidget

class Button(BaseWidget):
    def okw_click(self):
        self.adapter.click(self.locator)