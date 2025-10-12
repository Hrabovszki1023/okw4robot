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

def _require_adapter_method(adapter, method_name: str, widget, widget_name: str, keyword_name: str):
    if not hasattr(adapter, method_name):
        a = adapter.__class__.__name__
        w = widget.__class__.__name__ if widget else "<unknown>"
        loc = getattr(widget, 'locator', None)
        raise RuntimeError(
            f"[{keyword_name}] Not implemented by adapter: method '{method_name}' is missing on '{a}' "
            f"for widget '{widget_name}' ({w}), locator={loc}"
        )
    return getattr(adapter, method_name)

def _get_time(var_name: str, default_seconds: float) -> float:
    try:
        from robot.libraries.BuiltIn import BuiltIn
        to = BuiltIn().get_variable_value(var_name, default=default_seconds)
        return float(to) if isinstance(to, (int, float)) else BuiltIn().convert_time(str(to))
    except Exception:
        return float(default_seconds)

def _get_poll() -> float:
    try:
        from robot.libraries.BuiltIn import BuiltIn
        po = BuiltIn().get_variable_value("${OKW_POLL_VERIFY}", default=0.1)
        return float(po) if isinstance(po, (int, float)) else BuiltIn().convert_time(str(po))
    except Exception:
        return 0.1

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
        adapter = context.get_adapter()
        expected = str(expected).strip().upper()
        if expected not in ("YES", "NO"):
            raise ValueError(f"[VerifyExist] Expected must be 'YES' or 'NO', got '{expected}'")
        import time
        timeout = _get_time("${OKW_TIMEOUT_VERIFY_EXIST}", 2.0)
        poll = _get_poll()
        end = time.time() + timeout
        last = None
        while time.time() < end:
            last = bool(adapter.element_exists(widget.locator))
            if (expected == "YES" and last) or (expected == "NO" and not last):
                return
            time.sleep(poll)
        if expected == "YES":
            raise AssertionError(f"[VerifyExist] Element '{name}' should exist, but it does not.")
        else:
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

    @keyword("SetFocus")
    def set_focus(self, name):
        widget = resolve_widget(name)
        adapter = context.get_adapter()
        adapter.focus(widget.locator)

    @keyword("VerifyHasFocus")
    def verify_has_focus(self, name, expected):
        widget = resolve_widget(name)
        adapter = context.get_adapter()
        expected = str(expected).strip().upper()
        if expected not in ("YES", "NO"):
            raise ValueError(f"[VerifyHasFocus] Expected must be 'YES' or 'NO', got '{expected}'")
        import time
        timeout = _get_time("${OKW_TIMEOUT_VERIFY_FOCUS}", 2.0)
        poll = _get_poll()
        end = time.time() + timeout
        last = None
        while time.time() < end:
            last = bool(adapter.has_focus(widget.locator))
            if (expected == "YES" and last) or (expected == "NO" and not last):
                return
            time.sleep(poll)
        if expected == "YES":
            raise AssertionError(f"[VerifyHasFocus] Element '{name}' should have focus, but it does not.")
        else:
            raise AssertionError(f"[VerifyHasFocus] Element '{name}' should NOT have focus, but it does.")

    @keyword("VerifyVisible")
    def verify_visible(self, name, expected):
        widget = resolve_widget(name)
        adapter = context.get_adapter()
        # Strict: adapter must support method
        is_visible = _require_adapter_method(adapter, 'is_visible', widget, name, 'VerifyVisible')
        expected = str(expected).strip().upper()
        if expected not in ("YES", "NO"):
            raise ValueError(f"[VerifyVisible] Expected must be 'YES' or 'NO', got '{expected}'")
        import time
        timeout = _get_time("${OKW_TIMEOUT_VERIFY_VISIBLE}", 2.0)
        poll = _get_poll()
        end = time.time() + timeout
        last = None
        while time.time() < end:
            last = bool(is_visible(widget.locator))
            if (expected == "YES" and last) or (expected == "NO" and not last):
                return
            time.sleep(poll)
        if expected == "YES":
            raise AssertionError(f"[VerifyVisible] Element '{name}' should be visible, but it is not.")
        else:
            raise AssertionError(f"[VerifyVisible] Element '{name}' should NOT be visible, but it is.")

    @keyword("VerifyEnabled")
    def verify_enabled(self, name, expected):
        widget = resolve_widget(name)
        adapter = context.get_adapter()
        is_enabled = _require_adapter_method(adapter, 'is_enabled', widget, name, 'VerifyEnabled')
        expected = str(expected).strip().upper()
        if expected not in ("YES", "NO"):
            raise ValueError(f"[VerifyEnabled] Expected must be 'YES' or 'NO', got '{expected}'")
        import time
        timeout = _get_time("${OKW_TIMEOUT_VERIFY_ENABLED}", 2.0)
        poll = _get_poll()
        end = time.time() + timeout
        last = None
        while time.time() < end:
            last = bool(is_enabled(widget.locator))
            if (expected == "YES" and last) or (expected == "NO" and not last):
                return
            time.sleep(poll)
        if expected == "YES":
            raise AssertionError(f"[VerifyEnabled] Element '{name}' should be enabled, but it is not.")
        else:
            raise AssertionError(f"[VerifyEnabled] Element '{name}' should NOT be enabled, but it is.")

    @keyword("VerifyEditable")
    def verify_editable(self, name, expected):
        widget = resolve_widget(name)
        adapter = context.get_adapter()
        is_editable = _require_adapter_method(adapter, 'is_editable', widget, name, 'VerifyEditable')
        expected = str(expected).strip().upper()
        if expected not in ("YES", "NO"):
            raise ValueError(f"[VerifyEditable] Expected must be 'YES' or 'NO', got '{expected}'")
        import time
        timeout = _get_time("${OKW_TIMEOUT_VERIFY_EDITABLE}", 2.0)
        poll = _get_poll()
        end = time.time() + timeout
        last = None
        while time.time() < end:
            last = bool(is_editable(widget.locator))
            if (expected == "YES" and last) or (expected == "NO" and not last):
                return
            time.sleep(poll)
        if expected == "YES":
            raise AssertionError(f"[VerifyEditable] Element '{name}' should be editable, but it is not.")
        else:
            raise AssertionError(f"[VerifyEditable] Element '{name}' should NOT be editable, but it is.")

    @keyword("VerifyFocusable")
    def verify_focusable(self, name, expected):
        widget = resolve_widget(name)
        adapter = context.get_adapter()
        is_focusable = _require_adapter_method(adapter, 'is_focusable', widget, name, 'VerifyFocusable')
        expected = str(expected).strip().upper()
        if expected not in ("YES", "NO"):
            raise ValueError(f"[VerifyFocusable] Expected must be 'YES' or 'NO', got '{expected}'")
        import time
        timeout = _get_time("${OKW_TIMEOUT_VERIFY_FOCUSABLE}", 2.0)
        poll = _get_poll()
        end = time.time() + timeout
        last = None
        while time.time() < end:
            last = bool(is_focusable(widget.locator))
            if (expected == "YES" and last) or (expected == "NO" and not last):
                return
            time.sleep(poll)
        if expected == "YES":
            raise AssertionError(f"[VerifyFocusable] Element '{name}' should be focusable, but it is not.")
        else:
            raise AssertionError(f"[VerifyFocusable] Element '{name}' should NOT be focusable, but it is.")

    @keyword("VerifyClickable")
    def verify_clickable(self, name, expected):
        widget = resolve_widget(name)
        adapter = context.get_adapter()
        # Strict: adapter must support method
        is_clickable = _require_adapter_method(adapter, 'is_clickable', widget, name, 'VerifyClickable')
        expected = str(expected).strip().upper()
        if expected not in ("YES", "NO"):
            raise ValueError(f"[VerifyClickable] Expected must be 'YES' or 'NO', got '{expected}'")
        import time
        timeout = _get_time("${OKW_TIMEOUT_VERIFY_CLICKABLE}", 2.0)
        poll = _get_poll()
        end = time.time() + timeout
        last = None
        while time.time() < end:
            last = bool(is_clickable(widget.locator))
            if (expected == "YES" and last) or (expected == "NO" and not last):
                return
            time.sleep(poll)
        if expected == "YES":
            raise AssertionError(f"[VerifyClickable] Element '{name}' should be clickable, but it is not.")
        else:
            raise AssertionError(f"[VerifyClickable] Element '{name}' should NOT be clickable, but it is.")

    @keyword("ExecuteJS")
    def execute_js(self, script: str):
        adapter = context.get_adapter()
        # Selenium adapter exposes its SeleniumLibrary as 'sl'
        if hasattr(adapter, 'sl') and hasattr(adapter.sl, 'execute_javascript'):
            return adapter.sl.execute_javascript(script)
        a = adapter.__class__.__name__
        raise RuntimeError(f"[ExecuteJS] Not supported by adapter '{a}'")
