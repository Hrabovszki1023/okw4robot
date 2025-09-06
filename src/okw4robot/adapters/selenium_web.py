from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn

class SeleniumWebAdapter:

    def __init__(self, browser):
        self.browser = browser
        self.sl = SeleniumLibrary()
        self.sl.open_browser("about:blank", browser=self.browser)


    def go_to(self, url):
        self.sl.go_to(url)

    def maximize_window(self):
        self.sl.maximize_browser_window()

    def input_text(self, locator, value):
        resolved = self._resolve(locator)
        self.sl.input_text(resolved, value)

    def click(self, locator):
        resolved = self._resolve(locator)
        self.sl.click_element(resolved)

    def get_text(self, locator):
        resolved = self._resolve(locator)
        return self.sl.get_text(resolved)

    def element_exists(self, locator):
        try:
            self.sl.get_webelement(self._resolve(locator))
            return True
        except Exception:
            return False

    def _resolve(self, locator_dict):
        if not locator_dict:
            raise ValueError("Locator missing")
        if isinstance(locator_dict, str):
            return locator_dict
        if isinstance(locator_dict, dict):
            if len(locator_dict) != 1:
                raise ValueError(f"Locator must have exactly one key, got: {locator_dict}")
            key, value = list(locator_dict.items())[0]
            return f"{key}:{value}"
        raise TypeError(f"Unsupported locator format: {locator_dict}")