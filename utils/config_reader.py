import yaml

class ConfigReader:
    _instance = {}

    def __new__(cls, path: str = 'config.yaml'):
        if path not in cls._instance:
            instance = super().__new__(cls)
            instance._load_config(path)
            cls._instance[path] = instance
        return cls._instance[path]
    
    def _load_config(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            self._data = yaml.safe_load(file)

    def get(self, key: str):
        return self._data.get(key)
