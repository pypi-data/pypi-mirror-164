import os
import traceback


def to_boolean(value):
    return str(value).lower() == "true"


_defaultValues = {
    "enable_sql_trace": True,
    "ignore_url_postfix": None,
}

_valueFunc = {
    "enable_sql_trace": to_boolean,
}


class AppConfig(object):
    def __init__(self, config_path):
        self.path = None
        self.config = None
        self.cache = {}
        self.load_config(config_path)

    def __getattr__(self, attr_name):
        cached_value = self.cache.get(attr_name)
        if cached_value is not None:
            return cached_value

        if self.config is None:
            return None

        try:
            value_func = _valueFunc.get(attr_name)
            default_value = _defaultValues.get(attr_name)

            if default_value is None:
                return None

            if not self.config.has_option('JENNIFER', attr_name):
                attr_value = self.config.get('SERVER', attr_name, default_value)
            else:
                attr_value = self.config.get('JENNIFER', attr_name, default_value)

            if value_func is None:
                self.cache[attr_name] = attr_value
                return attr_value

            result = value_func(attr_value)
            self.cache[attr_name] = result

            return result
        except:
            return None

    def reload(self):
        self.load_config(self.path)

    def load_config(self, config_path):
        from jennifer.agent import config_parser

        if config_path is None:
            return

        try:
            self.path = config_path
            self.config = config_parser.ConfigParser()

            if len(self.cache) != 0:
                print(os.getpid(), 'jennifer', 'config_changed')
            self.cache = {}

            self.config.read(config_path)
        except Exception as e:
            print(os.getpid(), 'jennifer.exception', 'load_config', e)
            traceback.print_stack()
