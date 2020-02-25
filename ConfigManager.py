import json


class ConfigManager:
    """JSONParser app to parse configuration file config.json"""

    _instance = None
    _data = None
    _json_file = 'config.json'

    def __new__(cls):
        if not ConfigManager._instance:
            ConfigManager._instance = object.__new__(cls)
        return ConfigManager._instance

    @staticmethod
    def get_all_config():
        return ConfigManager._data.copy()

    @staticmethod
    def get_token():
        return ConfigManager._get_item('token')

    @staticmethod
    def get_backup_chats():
        return ConfigManager._get_item('backup_chats')

    @staticmethod
    def get_backup_name():
        return ConfigManager._get_item('backup_name')

    @staticmethod
    def _get_item(key: str):
        if not ConfigManager._data:
            with open(ConfigManager._json_file) as f:
                ConfigManager._data = json.load(f)
        try:
            ref = ConfigManager._data.get(key)
        except KeyError:
            raise LookupError(
                "{} wasn't found in {}, make sure this entry is present!".format(key, ConfigManager._json_file)
            )
        # se ref ha il metodo copy ritorna la copia
        # altrimenti ritorna ref (oggetto immutabile)
        # es: str, int, None
        try:
            value = ref.copy()
        except AttributeError:
            value = ref
        return value