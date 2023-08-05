# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProfilePreview(Model):
    """A preview about the profile with some of its properties.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. A unique identifier of the profile
    :type id: str
    :param last_known_path: An absolute path where the related .kameleo
     profile file was accessed lastly. This is updated when a profile is saved
     to a .kameleo file, or loaded from a .kameleo file.
    :type last_known_path: str
    :param device: Required.
    :type device: ~kameleo.local_api_client.models.Device
    :param os: Required.
    :type os: ~kameleo.local_api_client.models.Os
    :param browser: Required.
    :type browser: ~kameleo.local_api_client.models.Browser
    :param language: Required. Language of the profile. This is derived from
     the base profile. Using ISO 639-1 language codes.
    :type language: str
    :param launcher: Required. The mode how the profile should be launched. It
     determines which browser to launch. This cannot be modified after
     creation. Possible values are 'automatic', 'chrome', 'chromium',
     'firefox', 'edge', 'external'
    :type launcher: str
    :param status: Required.
    :type status: ~kameleo.local_api_client.models.StatusResponse
    """

    _validation = {
        'id': {'required': True},
        'device': {'required': True},
        'os': {'required': True},
        'browser': {'required': True},
        'language': {'required': True},
        'launcher': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'last_known_path': {'key': 'lastKnownPath', 'type': 'str'},
        'device': {'key': 'device', 'type': 'Device'},
        'os': {'key': 'os', 'type': 'Os'},
        'browser': {'key': 'browser', 'type': 'Browser'},
        'language': {'key': 'language', 'type': 'str'},
        'launcher': {'key': 'launcher', 'type': 'str'},
        'status': {'key': 'status', 'type': 'StatusResponse'},
    }

    def __init__(self, *, id: str, device, os, browser, language: str, launcher: str, status, last_known_path: str=None, **kwargs) -> None:
        super(ProfilePreview, self).__init__(**kwargs)
        self.id = id
        self.last_known_path = last_known_path
        self.device = device
        self.os = os
        self.browser = browser
        self.language = language
        self.launcher = launcher
        self.status = status
