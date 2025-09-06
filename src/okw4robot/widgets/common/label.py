from ..base.base_widget import BaseWidget

class Label(BaseWidget):
    def okw_verify_value(self, expected):
        actual = self.adapter.get_text(self.locator)
        if actual != expected:
            raise AssertionError(f"Expected '{expected}', got '{actual}'")

    def okw_log_value(self):
        print("LOG:", self.adapter.get_text(self.locator))

    def okw_memorize_value(self):
        return self.adapter.get_text(self.locator)