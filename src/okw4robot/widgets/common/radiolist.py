from ..base.base_widget import BaseWidget


class RadioList(BaseWidget):
    """Group of radio buttons. Requires group name via YAML extras.

    YAML example:
      MyRadios:
        class: okw4robot.widgets.common.radiolist.RadioList
        group: paymentMethod   # radio group/name attribute
    """

    def __init__(self, adapter, locator, **options):
        super().__init__(adapter, locator, **options)
        self.group = options.get('group')
        if not self.group:
            raise ValueError("RadioList requires 'group' option in YAML")

    def okw_select(self, value):
        self.adapter.select_radio(self.group, value)

    def okw_verify_value(self, expected):
        # Delegate assertion to adapter to leverage backend's verification
        self.adapter.radio_button_should_be_set_to(self.group, expected)

