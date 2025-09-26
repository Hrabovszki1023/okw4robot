from robot.api.deco import keyword


class ParamsKeywords:
    @keyword("SetOKWParameter")
    def set_okw_parameter(self, name: str, value):
        """Sets OKW runtime parameters such as timeouts.

        Supported names (case-insensitive):
        - TimeOutVerifyValue
        - TimeOutVerifyTooltip
        - TimeOutVerifyPlaceholder

        Value may be seconds (number) or Robot time string (e.g. '10s').
        Scope: suite variable.
        """
        mapping = {
            "TIMEOUTVERIFYVALUE": "${OKW_TIMEOUT_VERIFY_VALUE}",
            "TIMEOUTVERIFYTOOLTIP": "${OKW_TIMEOUT_VERIFY_TOOLTIP}",
            "TIMEOUTVERIFYPLACEHOLDER": "${OKW_TIMEOUT_VERIFY_PLACEHOLDER}",
            "TIMEOUTVERIFYLABEL": "${OKW_TIMEOUT_VERIFY_LABEL}",
            "TIMEOUTVERIFYCAPTION": "${OKW_TIMEOUT_VERIFY_CAPTION}",
        }
        key = str(name or "").strip().upper()
        if key not in mapping:
            raise ValueError(f"Unsupported OKW parameter: {name}")
        var_name = mapping[key]
        from robot.libraries.BuiltIn import BuiltIn
        # Keep raw value; readers will convert appropriately
        BuiltIn().set_suite_variable(var_name, value)
