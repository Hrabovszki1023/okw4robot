from robot.api.deco import keyword
from ..runtime.context import context


def _should_ignore(value) -> bool:
    if isinstance(value, str):
        sv = value.strip()
        t = sv.upper()
        if t in ("$IGNORE", "${IGNORE}"):
            return True
        # Allow optional global empty-ignore toggle
        try:
            from robot.libraries.BuiltIn import BuiltIn
            if sv == "" and str(BuiltIn().get_variable_value("${OKW_IGNORE_EMPTY}", default="NO")).strip().upper() in ("YES", "TRUE", "1"):
                return True
        except Exception:
            pass
    return False


def _resolve_widget(name):
    model = context.get_current_window_model()
    if name not in model:
        raise KeyError(f"Widget '{name}' not found in current window.")
    entry = model[name]
    from ..utils.loader import load_class
    widget_class = load_class(entry["class"])
    adapter = context.get_adapter()
    extras = {k: v for k, v in entry.items() if k not in ("class", "locator")}
    return widget_class(adapter, entry.get("locator"), **extras)


class PlaceholderKeywords:
    @keyword("VerifyPlaceholder")
    def verify_placeholder(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyPlaceholder] '{name}' ignored (blank or $IGNORE)")
            return
        w = _resolve_widget(name)
        if not hasattr(w, 'okw_verify_placeholder'):
            raise NotImplementedError(f"Widget '{name}' does not support VerifyPlaceholder")
        w.okw_verify_placeholder(expected)

    @keyword("VerifyPlaceholderWCM")
    def verify_placeholder_wcm(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyPlaceholderWCM] '{name}' ignored (blank or $IGNORE)")
            return
        w = _resolve_widget(name)
        if not hasattr(w, 'okw_verify_placeholder_wcm'):
            raise NotImplementedError(f"Widget '{name}' does not support VerifyPlaceholderWCM")
        w.okw_verify_placeholder_wcm(expected)

    @keyword("VerifyPlaceholderREGX")
    def verify_placeholder_regx(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyPlaceholderREGX] '{name}' ignored (blank or $IGNORE)")
            return
        w = _resolve_widget(name)
        if not hasattr(w, 'okw_verify_placeholder_regex'):
            raise NotImplementedError(f"Widget '{name}' does not support VerifyPlaceholderREGX")
        w.okw_verify_placeholder_regex(expected)

