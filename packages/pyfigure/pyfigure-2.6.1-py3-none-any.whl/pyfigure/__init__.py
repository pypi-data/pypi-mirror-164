from pathlib import Path
from typing import Callable, Any, Tuple
from dataclasses import dataclass
from sys import argv
from inspect import isclass
from tomlkit import load, dump, table
from typeguard import check_type
from superdict import SuperDict

class Config:
    """Declare config options."""

@dataclass
class Option:
    default: Any
    type: Any = Any
    description: str = ''
    parse: Callable = lambda x: x

class ParseError(Exception):
    def __init__(self, *args, original_error: Exception()):
        self.original_error = original_error
        super().__init__(*args)

class CheckError(ParseError):
    pass

class Configurable:
    """Create configuration files from classes.

    Attributes:
        config: A dictionary containing all of the parsed values from the class' configuration file.
        config_file: The Path object of the configuration file. 
    """

    config: SuperDict = SuperDict()
    config_file: Path

    def __init__(self,
        manual_errors: bool = False
    ):

        self.manual_errors = manual_errors

        if not hasattr(self, 'config_file'):
            executed_file = Path(argv[0])
            self.config_file = executed_file.with_suffix('.toml')
        if not isinstance(self.config_file, Path):
            self.config_file = Path(self.config_file)

        self.reload_config()

    def _get_nested_configs(self):
        result = []
        for name in dir(self):
            if not hasattr(self, name): continue
            obj = getattr(self, name)
            if isclass(obj) and issubclass(obj, Config):
                result.append(obj)
        return result

    def reload_config(self):
        """(Re)load the config option."""
        self._defaults = {}
        for config in self._get_nested_configs():
            self._defaults.update(self.generate_defaults(config))
        if hasattr(self, 'Config'):
            self._defaults.update(self.generate_defaults(self.Config))
        if not self._defaults:
            return

        if self.config_file.exists() and self.config_file.stat().st_size > 0:
            self.load_config()
            self.config, updated = self.fill_config(self._defaults, self.config)
            if updated: self.save_config()
        else:
            self.config = self.generate_config(self._defaults)
            self.save_config()

        if self.manual_errors:
            self.config = self.parse_config(self._defaults, self.config)
        else:
            try:
                self.config = self.parse_config(self._defaults, self.config)
            except (ParseError, CheckError) as error:
                print(error)

        del self._defaults

    def generate_defaults(self, config: dict, defaults: dict = None):
        """Generate config defaults from classes."""

        if not defaults: defaults = {}
        values = dict(config.__dict__)
        types = values.get('__annotations__', {})

        # remove internal values
        for key, _ in values.copy().items():
            if key.startswith('__'):
                del values[key]

        for key, value in values.items():

            if isinstance(value, Option):
                defaults[key] = value
                if key in types:
                    defaults[key].type = types[key]
                else:
                    defaults[key].type = Any
            elif isclass(value):
                if key not in types: types[key] = {}
                defaults[value.__name__] = self.generate_defaults(values[key], types[key])
            elif isinstance(value, dict):
                raise TypeError("Dictionary options are currently not functional, please use a list of dictionaries or a config subgroup instead.")
            else:
                raise TypeError("Config values must be Option objects")
        
        return defaults

    def save_config(self):
        """Save the config locally."""
        with open(self.config_file, 'w+') as file:
            dump(self.document_from_config(self._defaults, self.config), file)

    def load_config(self):
        """Load a locally saved config."""
        with open(self.config_file, 'r') as file:
            data = load(file)
            for key, value in data.items():
                if not isinstance(value, bool):
                    self.config[key] = value.value
                else:
                    self.config[key] = value

    def document_from_config(self, defaults: dict, config: dict) -> table():
        """Turn a config into a TOML Document with comments."""
        document = table()

        for key, value in defaults.items():
            
            if isinstance(value, dict):
                document[key] = self.document_from_config(defaults[key], config[key])
            else:
                document[key] = config[key]
                if value.description:
                    document.value.item(key).comment(value.description)

        return document

    def fill_config(self, defaults: dict, config: dict) -> Tuple[dict, bool]:
        """Fill a config if it has missing default values."""
        updated = False

        for key, value in defaults.items():

            if isinstance(value, dict):
                if key not in config: config[key] = {}
                sub, sub_up = self.fill_config(defaults[key], config[key])
                updated = updated or sub_up
                if sub: config[key] = sub

            elif key not in config:
                config[key] = value.default
                updated = updated or True

        return config, updated

    def generate_config(self, defaults: dict, config: dict = None) -> dict:
        """Generate a config from defaults."""
        if not config: config = {}

        for key, value in defaults.items():

            if isinstance(value, dict):
                config[key] = self.generate_config(defaults[key])
            else:
                config[key] = value.default
        
        return config

    def parse_config(self, defaults: dict, config: dict) -> dict:
        """Parse config values and check types."""
        # go over every value in the config
        for key, value in config.items():

            # if the value isn't in the default values, ignore it
            if key not in defaults: continue

            # if dict, loop over it
            if isinstance(value, dict):
                config[key] = self.parse_config(defaults[key], config[key])
                continue

            data = defaults[key]

            try:
                check_type(key, config[key], data.type)
            except TypeError as check_error:
                config[key] = data.default
                raise CheckError(f"Error while trying to load option '{key}': '{str(check_error)}'", original_error=check_error) from check_error

            try:
                config[key] = data.parse(config[key])
            except Exception as parse_error:
                config[key] = data.default
                raise ParseError(f"Error while trying to load option '{key}': '{str(parse_error)}'", original_error=parse_error) from parse_error

        return config