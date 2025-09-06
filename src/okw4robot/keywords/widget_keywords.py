from robot.api.deco import keyword
from ..runtime.context import context
from ..utils.loader import load_class

def resolve_widget(name):
    model = context.get_current_window_model()
    if name not in model:
        raise KeyError(f"Widget '{name}' not found in current window.")
    entry = model[name]
    widget_class = load_class(entry["class"])
    adapter = context.get_adapter()
    return widget_class(adapter, entry.get("locator"))

class WidgetKeywords:
    @keyword("ClickOn")
    def click_on(self, name):
        resolve_widget(name).okw_click()

    @keyword("DoubleClickOn")
    def double_click_on(self, name):
        resolve_widget(name).okw_double_click()

    @keyword("SetValue")
    def set_value(self, name, value):
        resolve_widget(name).okw_set_value(value)

    @keyword("Select")
    def select(self, name, value):
        resolve_widget(name).okw_select(value)

    @keyword("TypeKey")
    def type_key(self, name, key):
        resolve_widget(name).okw_type_key(key)

    @keyword("VerifyValue")
    def verify_value(self, name, expected):
        resolve_widget(name).okw_verify_value(expected)

    @keyword("VerifyValueWCM")
    def verify_value_wcm(self, name, expected):
        resolve_widget(name).okw_verify_value_wcm(expected)

    @keyword("VerifyValueREGX")
    def verify_value_regx(self, name, expected):
        resolve_widget(name).okw_verify_value_regex(expected)

    @keyword("VerifyExist")
    def verify_exist(self, name, expected):
        widget = resolve_widget(name)
        exists = widget.okw_verify_exist()

        expected = expected.strip().upper()
        if expected not in ("YES", "NO"):
            raise ValueError(f"[VerifyExist] Expected must be 'YES' or 'NO', got '{expected}'")

        if expected == "YES" and not exists:
            raise AssertionError(f"[VerifyExist] Element '{name}' should exist, but it does not.")
        if expected == "NO" and exists:
            raise AssertionError(f"[VerifyExist] Element '{name}' should NOT exist, but it does.")

    @keyword("LogValue")
    def log_value(self, name):
        resolve_widget(name).okw_log_value()

    @keyword("HasValue")
    def has_value(self, name):
        resolve_widget(name).okw_has_value()

    @keyword("MemorizeValue")
    def memorize_value(self, name, variable):
        value = resolve_widget(name).okw_memorize_value()
        from robot.libraries.BuiltIn import BuiltIn
        BuiltIn().set_test_variable(f"${{{variable}}}", value)