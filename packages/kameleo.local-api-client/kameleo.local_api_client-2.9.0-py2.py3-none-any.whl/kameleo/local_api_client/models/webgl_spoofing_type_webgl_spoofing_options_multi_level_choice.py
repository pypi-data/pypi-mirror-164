# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WebglSpoofingTypeWebglSpoofingOptionsMultiLevelChoice(Model):
    """WebglSpoofingTypeWebglSpoofingOptionsMultiLevelChoice.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Possible values include: 'noise', 'block', 'off'
    :type value: str or ~kameleo.local_api_client.models.enum
    :param extra:
    :type extra: ~kameleo.local_api_client.models.WebglSpoofingOptions
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'extra': {'key': 'extra', 'type': 'WebglSpoofingOptions'},
    }

    def __init__(self, **kwargs):
        super(WebglSpoofingTypeWebglSpoofingOptionsMultiLevelChoice, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.extra = kwargs.get('extra', None)
