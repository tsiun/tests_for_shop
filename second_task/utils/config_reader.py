import yaml

class ConfigReader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self):
        with open('config.yaml', 'r', encoding='utf-8') as file:
            self._data = yaml.safe_load(file)

    def get(self, key: str):
        return self._data.get(key)
