# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProfileResponse(Model):
    """ProfileResponse.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. A unique identifier of the profile
    :type id: str
    :param last_known_path: An absolute path where the related .kameleo
     profile file was accessed lastly. This is updated when a profile is saved
     to a .kameleo file, or loaded from a .kameleo file.
    :type last_known_path: str
    :param created_at: Required. Date when the profile was created.
    :type created_at: datetime
    :param base_profile: Required.
    :type base_profile: ~kameleo.local_api_client.models.BaseProfile
    :param canvas: Required. Possible values include: 'intelligent', 'noise',
     'block', 'off'
    :type canvas: str or ~kameleo.local_api_client.models.enum
    :param webgl: Required.
    :type webgl:
     ~kameleo.local_api_client.models.WebglSpoofingTypeWebglSpoofingOptionsMultiLevelChoice
    :param audio: Required. Possible values include: 'off', 'noise', 'block'
    :type audio: str or ~kameleo.local_api_client.models.enum
    :param timezone: Required.
    :type timezone:
     ~kameleo.local_api_client.models.TimezoneSpoofingTypeTimezoneMultiLevelChoice
    :param geolocation: Required.
    :type geolocation:
     ~kameleo.local_api_client.models.GeolocationSpoofingTypeGeolocationSpoofingOptionsMultiLevelChoice
    :param proxy: Required.
    :type proxy:
     ~kameleo.local_api_client.models.ProxyConnectionTypeServerMultiLevelChoice
    :param web_rtc: Required.
    :type web_rtc:
     ~kameleo.local_api_client.models.WebRtcSpoofingTypeWebRtcSpoofingOptionsMultiLevelChoice
    :param fonts: Required.
    :type fonts:
     ~kameleo.local_api_client.models.FontSpoofingTypeFontIListMultiLevelChoice
    :param plugins: Required.
    :type plugins:
     ~kameleo.local_api_client.models.PluginSpoofingTypePluginIListMultiLevelChoice
    :param screen: Required.
    :type screen:
     ~kameleo.local_api_client.models.ScreenSpoofingTypeScreenSizeMultiLevelChoice
    :param start_page: Required. This website will be opened in the browser
     when the profile launches.
    :type start_page: str
    :param password_manager: Required. Possible values include: 'enabled',
     'disabled'
    :type password_manager: str or ~kameleo.local_api_client.models.enum
    :param extensions: Required. A list of extensions or addons that will be
     loaded to the profile when the profile is started. For chrome and edge use
     CRX3 format extensions. For firefox use signed xpi format addons.
    :type extensions: list[str]
    :param notes: Required. A free text including any notes written by the
     user.
    :type notes: str
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
        'created_at': {'required': True},
        'base_profile': {'required': True},
        'canvas': {'required': True},
        'webgl': {'required': True},
        'audio': {'required': True},
        'timezone': {'required': True},
        'geolocation': {'required': True},
        'proxy': {'required': True},
        'web_rtc': {'required': True},
        'fonts': {'required': True},
        'plugins': {'required': True},
        'screen': {'required': True},
        'start_page': {'required': True},
        'password_manager': {'required': True},
        'extensions': {'required': True},
        'notes': {'required': True},
        'launcher': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'last_known_path': {'key': 'lastKnownPath', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'base_profile': {'key': 'baseProfile', 'type': 'BaseProfile'},
        'canvas': {'key': 'canvas', 'type': 'str'},
        'webgl': {'key': 'webgl', 'type': 'WebglSpoofingTypeWebglSpoofingOptionsMultiLevelChoice'},
        'audio': {'key': 'audio', 'type': 'str'},
        'timezone': {'key': 'timezone', 'type': 'TimezoneSpoofingTypeTimezoneMultiLevelChoice'},
        'geolocation': {'key': 'geolocation', 'type': 'GeolocationSpoofingTypeGeolocationSpoofingOptionsMultiLevelChoice'},
        'proxy': {'key': 'proxy', 'type': 'ProxyConnectionTypeServerMultiLevelChoice'},
        'web_rtc': {'key': 'webRtc', 'type': 'WebRtcSpoofingTypeWebRtcSpoofingOptionsMultiLevelChoice'},
        'fonts': {'key': 'fonts', 'type': 'FontSpoofingTypeFontIListMultiLevelChoice'},
        'plugins': {'key': 'plugins', 'type': 'PluginSpoofingTypePluginIListMultiLevelChoice'},
        'screen': {'key': 'screen', 'type': 'ScreenSpoofingTypeScreenSizeMultiLevelChoice'},
        'start_page': {'key': 'startPage', 'type': 'str'},
        'password_manager': {'key': 'passwordManager', 'type': 'str'},
        'extensions': {'key': 'extensions', 'type': '[str]'},
        'notes': {'key': 'notes', 'type': 'str'},
        'launcher': {'key': 'launcher', 'type': 'str'},
        'status': {'key': 'status', 'type': 'StatusResponse'},
    }

    def __init__(self, **kwargs):
        super(ProfileResponse, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.last_known_path = kwargs.get('last_known_path', None)
        self.created_at = kwargs.get('created_at', None)
        self.base_profile = kwargs.get('base_profile', None)
        self.canvas = kwargs.get('canvas', None)
        self.webgl = kwargs.get('webgl', None)
        self.audio = kwargs.get('audio', None)
        self.timezone = kwargs.get('timezone', None)
        self.geolocation = kwargs.get('geolocation', None)
        self.proxy = kwargs.get('proxy', None)
        self.web_rtc = kwargs.get('web_rtc', None)
        self.fonts = kwargs.get('fonts', None)
        self.plugins = kwargs.get('plugins', None)
        self.screen = kwargs.get('screen', None)
        self.start_page = kwargs.get('start_page', None)
        self.password_manager = kwargs.get('password_manager', None)
        self.extensions = kwargs.get('extensions', None)
        self.notes = kwargs.get('notes', None)
        self.launcher = kwargs.get('launcher', None)
        self.status = kwargs.get('status', None)
