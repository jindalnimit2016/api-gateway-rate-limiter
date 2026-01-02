# gateway/config/config_manager.py
class ConfigManager:
    _instance = None

    def __new__(cls, config=None):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.config = config or {}
        return cls._instance

    def get_config(self, key, default=None):
        return self.config.get(key, default)
