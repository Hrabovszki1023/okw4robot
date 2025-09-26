import inspect
from okw4robot.utils.logging_mixin import LoggingMixin

class BaseWidget(LoggingMixin):
    def __init__(self, adapter, locator, **options):
        self.adapter = adapter
        self.locator = locator
        self.options = options or {}

    def okw_click(self): raise NotImplementedError()
    def okw_double_click(self): raise NotImplementedError()
    def okw_set_value(self, value): raise NotImplementedError()
    def okw_select(self, value): raise NotImplementedError()
    def okw_type_key(self, key): raise NotImplementedError()
    def okw_verify_value(self, expected): raise NotImplementedError()
    def okw_verify_value_wcm(self, expected): raise NotImplementedError()
    def okw_verify_value_regex(self, expected): raise NotImplementedError()

    def okw_verify_exist(self):
        self.log_current_method()
        return self.adapter.element_exists(self.locator)

    def okw_log_value(self): raise NotImplementedError()
    def okw_has_value(self): raise NotImplementedError()
    def okw_memorize_value(self): raise NotImplementedError()
