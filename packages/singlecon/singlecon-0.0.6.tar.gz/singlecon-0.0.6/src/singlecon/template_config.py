from functools import cached_property
import logging
from typing import Any, Dict, Optional, Tuple, Type, TypeVar
from pydantic import BaseModel
from pydantic.fields import FieldInfo
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, EnvSettingsSource, SettingsConfigDict
import tomlkit
from pathlib import Path

class TemplateMeta(type(BaseSettings)):

    def __init__(self, name, bases, *args, **kwargs) -> None:
        super().__init__(name, bases, *args, **kwargs)
        # if len(bases) > 1:
        #     raise TypeError("Multiple inheritance not supported")
        if name == "TemplateConfig":
            self._env_fields: list[str] = []
            self._file_fields: list[str] = []
        else:
            b = bases[0]
            self._env_fields = self._env_fields.copy()
            self._file_fields = self._file_fields.copy()
            if any(b.model_config['_extra_env'] for b in bases):
                self._env_fields += [
                    k for k in self.model_fields.keys() if k not in
                    [f for b in bases for f in b.model_fields.keys()] 
                ]
                self.model_config['_extra_env'] = False
            if any(b.model_config['_extra_file'] for b in bases):
                self._file_fields += [
                    k for k in self.model_fields.keys() if k not in
                    [f for b in bases for f in b.model_fields.keys()] 
                ]
                self.model_config['_extra_file'] = False

class TemplateConfig(BaseSettings, metaclass=TemplateMeta):
    
    def to_toml(self, config_file=None):
        config_file = config_file or self.model_config.config_file
        Path(config_file).touch(exist_ok=True)
        with open(config_file, 'w') as f:
            tomlkit.dump(self.file_dict(), f)

    def file_dict(self) -> Dict[str, Any]:
        file_dict = {}
        fs = {k: v for k, v in self if k in self._file_fields}
        for k, v in fs.items(): 
            # add submodels
            if isinstance(v, TemplateConfig):
                file_dict[k] = v.file_dict()
            elif isinstance(v, BaseModel):
                file_dict[k] = v.model_dump()
            else:
                file_dict[k] = v
        return file_dict

    def to_dotenv(self, env_file=None):
        env_file = env_file or self.model_config["env_file"]
        if self._env_fields:
            with open(env_file, 'w') as f:
                f.writelines(f"{k}={v}\n" for k,v in self.env_dict().items())

    def env_dict(self, prefix="") -> Dict[str, str]:
        env_name = lambda f: (prefix + next(
            n[1] for n in 
            EnvSettingsSource(TemplateConfig)._extract_field_info(self.model_fields[f], f)
            # self.model_fields[f].extra['env_names']
        )).upper()
        env_dict = {}
        # add submodels
        for k, v in self: 
            if isinstance(v, TemplateConfig):
                p = k+self.model_config["env_nested_delimiter"]
                env_dict.update(v.env_dict(prefix=p))
            elif k in self._env_fields:
                if isinstance(v, BaseModel):
                    env_dict[env_name(k)] = v.model_dump_json()
                else:
                    env_dict[env_name(k)] = v
        return env_dict

    model_config = SettingsConfigDict(
        env_nested_delimiter = '__', # cannot use it in naming the fields
        config_file_type = 'toml',
        config_file = None,
        _extra_env = False,
        _extra_file = False,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        file_settings = {
            'toml': TomlConfigSettingsSource(settings_cls),
        }[cls.model_config["config_file_type"]]
        return init_settings, env_settings, dotenv_settings, file_secret_settings, file_settings,

class TomlConfigSettingsSource(PydanticBaseSettingsSource):
    @cached_property
    def toml_settings(self) -> Dict[str, Any]:
        if not self.config["config_file"]:
            return {}
        path = Path(self.config["config_file"])
        if path.exists():
            with open(path, 'r') as f:
                conf_dict = tomlkit.load(f).value
            return conf_dict
        else:
            return {}
        
    def get_field_value(
        self, field: FieldInfo, field_name: str
    ) -> Tuple[Any, str, bool]:
        field_value = self.toml_settings.get(field_name)
        return field_value, field_name, False

    def __call__(self) -> Dict[str, Any]:
        return self.toml_settings

class FileConfig(TemplateConfig):
    model_config = SettingsConfigDict(_extra_file = True)

class EnvConfig(TemplateConfig):
    model_config = SettingsConfigDict(_extra_env = True)

T = TypeVar("T")

def extra_env(base: Type[T]) -> Type[T]:
    class ExtraEnv(base):
        model_config = SettingsConfigDict(_extra_env = True)

    return ExtraEnv

