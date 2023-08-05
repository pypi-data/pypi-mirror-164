# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class TestProxyResponse(Model):
    """TestProxyResponse.

    All required parameters must be populated in order to send to Azure.

    :param is_valid_proxy: Required. Tells weather the proxy is valid or not.
    :type is_valid_proxy: bool
    :param message: Required. A written message about the result of the test.
    :type message: str
    """

    _validation = {
        'is_valid_proxy': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'is_valid_proxy': {'key': 'isValidProxy', 'type': 'bool'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TestProxyResponse, self).__init__(**kwargs)
        self.is_valid_proxy = kwargs.get('is_valid_proxy', None)
        self.message = kwargs.get('message', None)


class TestProxyResponseException(HttpOperationError):
    """Server responsed with exception of type: 'TestProxyResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(TestProxyResponseException, self).__init__(deserialize, response, 'TestProxyResponse', *args)
