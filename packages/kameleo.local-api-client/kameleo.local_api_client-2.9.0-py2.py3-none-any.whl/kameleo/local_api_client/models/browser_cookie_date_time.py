# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BrowserCookieDateTime(Model):
    """BrowserCookieDateTime.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar unix_timestamp:
    :vartype unix_timestamp: long
    :ivar web_kit_timestamp:
    :vartype web_kit_timestamp: long
    :ivar microsecond_timestamp:
    :vartype microsecond_timestamp: long
    :ivar has_value:
    :vartype has_value: bool
    """

    _validation = {
        'unix_timestamp': {'readonly': True},
        'web_kit_timestamp': {'readonly': True},
        'microsecond_timestamp': {'readonly': True},
        'has_value': {'readonly': True},
    }

    _attribute_map = {
        'unix_timestamp': {'key': 'unixTimestamp', 'type': 'long'},
        'web_kit_timestamp': {'key': 'webKitTimestamp', 'type': 'long'},
        'microsecond_timestamp': {'key': 'microsecondTimestamp', 'type': 'long'},
        'has_value': {'key': 'hasValue', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(BrowserCookieDateTime, self).__init__(**kwargs)
        self.unix_timestamp = None
        self.web_kit_timestamp = None
        self.microsecond_timestamp = None
        self.has_value = None
