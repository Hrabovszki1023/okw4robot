from ..base.base_widget import BaseWidget


class ComboBox(BaseWidget):
    """Combo with text entry and optional dropdown selection.

    Strategy for SetValue:
    1) Try selecting by label (if it's a native <select>),
    2) If that fails, clear and type the text, then press ENTER.
    """

    def okw_set_value(self, value):
        try:
            self.adapter.select_by_label(self.locator, value)
            return
        except Exception:
            pass
        try:
            self.adapter.clear_text(self.locator)
        except Exception:
            pass
        self.adapter.input_text(self.locator, value)
        # confirm with Enter to commit selection in many combos
        try:
            self.adapter.press_keys(self.locator, "ENTER")
        except Exception:
            pass

    def okw_select(self, value):
        # Alias to set value (supports both semantics)
        self.okw_set_value(value)

    def okw_verify_value(self, expected):
        actual = None
        # Try value (input) first
        try:
            actual = self.adapter.get_value(self.locator)
        except Exception:
            pass
        # Fallback to selected label (native select)
        if actual is None or actual == "":
            try:
                labels = self.adapter.get_selected_list_labels(self.locator)
                if labels:
                    actual = labels[0]
            except Exception:
                pass
        if actual != expected:
            raise AssertionError(f"[ComboBox] Expected '{expected}', got '{actual}'")

    def okw_log_value(self):
        try:
            val = self.adapter.get_value(self.locator)
        except Exception:
            val = None
        print("LOG:", val)

    def okw_memorize_value(self):
        try:
            return self.adapter.get_value(self.locator)
        except Exception:
            labels = self.adapter.get_selected_list_labels(self.locator)
            return labels[0] if labels else None

    # Placeholder (for combos that are input-based)
    def _get_placeholder(self):
        ph = None
        try:
            ph = self.adapter.get_attribute(self.locator, 'placeholder')
        except Exception:
            ph = None
        return ph if ph is not None else ""

    def okw_verify_placeholder(self, expected):
        actual = self._get_placeholder()
        if actual != expected:
            raise AssertionError("[VerifyPlaceholder] Expected '" + str(expected) + "', got '" + str(actual) + "'")

    def okw_verify_placeholder_wcm(self, expected):
        import re
        value = self._get_placeholder()
        pattern = '^' + re.escape(expected).replace(r'\\*', '.*').replace(r'\\?', '.') + '$'
        if not re.compile(pattern, re.DOTALL).match(value):
            raise AssertionError("[VerifyPlaceholderWCM] Value '" + str(value) + "' does not match pattern '" + str(expected) + "'")

    def okw_verify_placeholder_regex(self, expected):
        import re
        value = self._get_placeholder()
        if not re.search(expected, value or ""):
            raise AssertionError("[VerifyPlaceholderREGX] Value '" + str(value) + "' does not match regex '" + str(expected) + "'")
