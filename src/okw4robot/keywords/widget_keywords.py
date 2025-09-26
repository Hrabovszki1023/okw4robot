from robot.api.deco import keyword
from ..runtime.context import context
from ..utils.loader import load_class

def _blank_ignore_enabled() -> bool:
    try:
        from robot.libraries.BuiltIn import BuiltIn
        val = BuiltIn().get_variable_value("${OKW_IGNORE_EMPTY}", default="NO")
        return str(val).strip().upper() in ("YES", "TRUE", "1")
    except Exception:
        return False

def _should_ignore(value) -> bool:
    """Return True if the keyword argument indicates 'ignore'.

    Rules:
    - Literal tokens '$IGNORE' or '${IGNORE}' (any case) -> ignore
    - Optionally, if ${OKW_IGNORE_EMPTY}=YES, then empty/whitespace-only -> ignore
    """
    if isinstance(value, str):
        sv = value.strip()
        t = sv.upper()
        if t in ("$IGNORE", "${IGNORE}"):
            return True
        if sv == "" and _blank_ignore_enabled():
            return True
    return False

def resolve_widget(name):
    model = context.get_current_window_model()
    if name not in model:
        raise KeyError(f"Widget '{name}' not found in current window.")
    entry = model[name]
    widget_class = load_class(entry["class"])
    adapter = context.get_adapter()
    extras = {k: v for k, v in entry.items() if k not in ("class", "locator")}
    return widget_class(adapter, entry.get("locator"), **extras)

class WidgetKeywords:
    @keyword("ClickOn")
    def click_on(self, name):
        resolve_widget(name).okw_click()

    @keyword("DoubleClickOn")
    def double_click_on(self, name):
        resolve_widget(name).okw_double_click()

    @keyword("SetValue")
    def set_value(self, name, value):
        if _should_ignore(value):
            print(f"[SetValue] '{name}' ignored (blank or $IGNORE)")
            return
        resolve_widget(name).okw_set_value(value)

    @keyword("Select")
    def select(self, name, value):
        if _should_ignore(value):
            print(f"[Select] '{name}' ignored (blank or $IGNORE)")
            return
        resolve_widget(name).okw_select(value)

    @keyword("TypeKey")
    def type_key(self, name, key):
        # Handle special delete token
        if isinstance(key, str) and key.strip().upper() in ("$DELETE", "${DELETE}"):
            widget = resolve_widget(name)
            try:
                widget.adapter.clear_text(widget.locator)
                return
            except Exception:
                pass
            try:
                widget.adapter.click(widget.locator)
                widget.adapter.press_keys(widget.locator, "CTRL+A")
                widget.adapter.press_keys(widget.locator, "DELETE")
                return
            except Exception:
                pass
        if _should_ignore(key):
            print(f"[TypeKey] '{name}' ignored (blank or $IGNORE)")
            return
        resolve_widget(name).okw_type_key(key)

    @keyword("VerifyValue")
    def verify_value(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyValue] '{name}' ignored (blank or $IGNORE)")
            return
        import time
        from robot.libraries.BuiltIn import BuiltIn
        w = resolve_widget(name)
        try:
            to = BuiltIn().get_variable_value("${OKW_TIMEOUT_VERIFY_VALUE}", default=10)
            timeout = float(to) if isinstance(to, (int, float)) else BuiltIn().convert_time(str(to))
        except Exception:
            timeout = 10.0
        end = time.time() + timeout
        last_error = None
        while time.time() < end:
            try:
                w.okw_verify_value(expected)
                return
            except AssertionError as e:
                last_error = e
                time.sleep(0.1)
        if last_error:
            raise last_error

    @keyword("VerifyValueWCM")
    def verify_value_wcm(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyValueWCM] '{name}' ignored (blank or $IGNORE)")
            return
        import time
        from robot.libraries.BuiltIn import BuiltIn
        w = resolve_widget(name)
        try:
            to = BuiltIn().get_variable_value("${OKW_TIMEOUT_VERIFY_VALUE}", default=10)
            timeout = float(to) if isinstance(to, (int, float)) else BuiltIn().convert_time(str(to))
        except Exception:
            timeout = 10.0
        end = time.time() + timeout
        last_error = None
        while time.time() < end:
            try:
                w.okw_verify_value_wcm(expected)
                return
            except AssertionError as e:
                last_error = e
                time.sleep(0.1)
        if last_error:
            raise last_error

    @keyword("VerifyValueREGX")
    def verify_value_regx(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyValueREGX] '{name}' ignored (blank or $IGNORE)")
            return
        import time
        from robot.libraries.BuiltIn import BuiltIn
        w = resolve_widget(name)
        try:
            to = BuiltIn().get_variable_value("${OKW_TIMEOUT_VERIFY_VALUE}", default=10)
            timeout = float(to) if isinstance(to, (int, float)) else BuiltIn().convert_time(str(to))
        except Exception:
            timeout = 10.0
        end = time.time() + timeout
        last_error = None
        while time.time() < end:
            try:
                w.okw_verify_value_regex(expected)
                return
            except AssertionError as e:
                last_error = e
                time.sleep(0.1)
        if last_error:
            raise last_error

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
