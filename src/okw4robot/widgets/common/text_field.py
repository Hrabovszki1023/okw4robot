from ..base.base_widget import BaseWidget

class TextField(BaseWidget):
    def okw_set_value(self, value):
        self.adapter.input_text(self.locator, value)

    def okw_click(self):
        self.adapter.click(self.locator)

    def okw_verify_value(self, expected):
        actual = self.adapter.get_text(self.locator)
        if actual != expected:
            raise AssertionError(f"Expected '{expected}', got '{actual}'")

    def okw_log_value(self):
        print("LOG:", self.adapter.get_text(self.locator))

    def okw_memorize_value(self):
        return self.adapter.get_text(self.locator)
    
    def okw_exists(self):
        return self.adapter.element_exists(self.locator)