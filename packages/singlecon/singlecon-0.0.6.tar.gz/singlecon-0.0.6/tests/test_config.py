import logging
import os
from pathlib import Path
import pytest
from pydantic import ValidationError, PrivateAttr, BaseModel

from singlecon import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# pytest tests/test_config.py --log-cli-level DEBUG 

@pytest.fixture
def env_path():
    conf_path = "tests/data/.env"
    p = Path(conf_path)
    p.unlink(missing_ok=True)
    yield conf_path
    # clean the path before and after use
    p.unlink(missing_ok=True)

@pytest.fixture
def persist_env_path():
    conf_path = "tests/data/.env"
    p = Path(conf_path)
    p.unlink(missing_ok=True)
    yield conf_path

@pytest.fixture
def conf_path():
    conf_path = "tests/data/config.toml"
    p = Path(conf_path)
    p.unlink(missing_ok=True)
    yield conf_path
    # clean the path before and after use
    p.unlink(missing_ok=True)

@pytest.fixture
def persist_conf_path():
    conf_path = "tests/data/config.toml"
    p = Path(conf_path)
    p.unlink(missing_ok=True)
    yield conf_path

def test_env_dict(monkeypatch, env_path):
    class SubConfig(TemplateConfig):
        a: int = 4
        b: int = 5
    SubConfig._env_fields = ['a']
    sub_config = SubConfig(a=7)
    class MockConfig(TemplateConfig):
        a: int = 1
        b: int = 2
        c: int = 3
        sub_c: SubConfig = sub_config
        
        model_config = SettingsConfigDict(
            env_nested_delimiter = '_'
        )
    MockConfig._env_fields = ['a','b']
    config = MockConfig(a=0)

    env_d = config.env_dict()
    
    assert config.env_dict() == {'A': 0, 'B': 2, 'SUB_C_A': 7}

    with pytest.raises(ValidationError) as excinfo:
        monkeypatch.setenv('SUB_C_A', '10')
        config = MockConfig()
    assert "type=extra_forbidden" in str(excinfo.value)
    assert os.getenv('SUB_C_A') == '10'

    config.model_config['env_nested_delimiter'] = '__'
    config.to_dotenv(env_file=env_path)

    class ReadEnv(MockConfig):
        model_config = SettingsConfigDict(env_file=env_path)

    read_conf = ReadEnv()
    assert read_conf.a == 0
    assert read_conf.sub_c.a == 7
    assert read_conf.model_dump() == config.model_dump()

    logger.debug({k:v for k,v in config})
    logger.debug(config.model_dump())
    logger.debug(type(MockConfig))

def test_multiple_inherit():
    class A(TemplateConfig):
        a: int = 1
    
    class B(TemplateConfig):
        a: int = 2
        b: int = 3

    class C(A, B, EnvConfig):
        a: int = 4
        c: int = 5
        d: str

    logger.debug(C.model_fields)
    logger.debug({k:v for k,v in C(c=2,d='45')})
    logger.debug(C(d='45').model_dump())
    assert EnvConfig.model_config['_extra_env']
    assert C._env_fields == ['c', 'd']
    with pytest.raises(ValidationError, match='Field required'):
        assert C().a == 4

    class D(A, B, EnvConfig):
        a: int = 4
        c: str = 5
        d: str

    assert D._env_fields == ['c', 'd']

def test_file_config(monkeypatch, conf_path, env_path):
    class SubConfig(TemplateConfig):
        a: int = 4
        b: int = 5
    SubConfig._env_fields = ['a']
    sub_config = SubConfig(a=7)
    class MockConfig(FileConfig):
        a: int = 1
        b: int = 2
        c: int = 3
        sub_c: SubConfig = sub_config

    assert not MockConfig.model_config['_extra_env']
    
    class EnvMock(extra_env(MockConfig)):
        env_field: str

    assert not MockConfig.model_config['_extra_env']
    assert not EnvMock.model_config['_extra_env']
    MockConfig(a=0)
    logger.debug(MockConfig._file_fields)
    assert MockConfig._file_fields == ['a', 'b', 'c', 'sub_c']
    logger.debug(MockConfig._env_fields)
    assert MockConfig._env_fields == []
    logger.debug(EnvMock._env_fields)
    assert EnvMock._env_fields == ['env_field']

    class MorePyConfig(EnvMock):
        a: int = -1
        pythonic: dict = {
            'a': 1,
            'b': 2,
        }
    assert MorePyConfig._file_fields == ['a', 'b', 'c', 'sub_c']
    assert MorePyConfig._env_fields == ['env_field']

    pyc = MorePyConfig(env_field='abc')
    pyc.sub_c.a = -10
    pyc.to_dotenv(env_file=env_path)

    with pytest.raises(ValidationError, match='env_field'):    
        MorePyConfig()

    pyconfig = MorePyConfig(_env_file=env_path)
    assert pyconfig.sub_c.a == -10
    logger.debug(pyconfig.model_dump())
    assert pyconfig.model_dump() == {'a': -1, 'b': 2, 'c': 3, 'sub_c': {'a': -10, 'b': 5}, 'env_field': 'abc', 'pythonic': {'a': 1, 'b': 2}}

    with pytest.raises(ValidationError, match='env_field'):    
        config = EnvMock(a=0)

    assert not MockConfig.model_config['_extra_env']
    class MoreEnv(MockConfig, EnvConfig):
        env_var: int = 99

    assert not MockConfig.model_config['_extra_env']
    assert MoreEnv._env_fields == ['env_var']
    assert not MoreEnv.model_config['_extra_env']
    logger.debug(MoreEnv().model_dump())

    class MoreEnv(MockConfig):
        env_var: int = 99

def test_tomlkit_rewrite_idempotent(conf_path):
    file_dict = {
        "a": {
            "a": {
                "a": 11
            }
        },
        "b": {
            "a": 11
        },
    }

    s1 = tomlkit.dumps(file_dict)
    file_dict2 = tomlkit.loads(tomlkit.dumps(file_dict))
    s2 = tomlkit.dumps(file_dict2)
    assert s2 == s1

    assert type(file_dict2['a']['a']) is not type(file_dict['a']['a'])

    # this is where it fails
    file_dict3 = {
        "a": {
            "a": file_dict2['a']['a']
        },
        "b": {
            "a": 11
        },
    }
    assert tomlkit.dumps(file_dict3) != s1

def test_file_config_read_rewrite_idempotent(conf_path):
    class CelerySection(FileConfig):
        broker_url: str = "amqp://rabbitmq-server"
        task_send_sent_event: bool = True
        beat_schedule: dict = {
            'sync-todoist': {
                'task': 'todo.sync_update.get',
                'schedule': 20.0,
                # 'kwargs': {'sync': False}
            },
        }

    class RedisSection(FileConfig):
        host: str = "redis-server"
        port: str = "6379"

    class MainConfig(FileConfig):
        celery: CelerySection = CelerySection()
        redis: RedisSection = RedisSection()
    
        model_config = SettingsConfigDict(config_file = conf_path)

    file_dict = {'celery': {'broker_url': 'amqp://rabbitmq-server', 'task_send_sent_event': True, 'beat_schedule': {'sync-todoist': {'task': 'todo.sync_update.get', 'schedule': 20.0}}}, 'redis': {'host': 'redis-server', 'port': '6379'}}
    dict_str = tomlkit.dumps(file_dict)

    config = MainConfig()
    file_dict_conf = config.file_dict()
    assert file_dict_conf == file_dict
    assert tomlkit.dumps(file_dict_conf) == dict_str
    assert type(file_dict['celery']['beat_schedule']) is type(file_dict_conf['celery']['beat_schedule'])

    assert tomlkit.dumps(tomlkit.loads(tomlkit.dumps(file_dict_conf))) == tomlkit.dumps(file_dict_conf)

    config.to_toml(conf_path)

    config2 = MainConfig()
    file_dict_conf2 = config2.file_dict()

    assert tomlkit.dumps(file_dict_conf2) == tomlkit.dumps(file_dict_conf)
    assert type(file_dict_conf2['celery']['beat_schedule']) is type(file_dict_conf['celery']['beat_schedule'])

def test_composite_template_config_with_partially_init_subconfig_from_env(monkeypatch):
    class SubClass(TemplateConfig):
        host: str = "postgres"
        port: int = 1234
    class SubClass2(SubClass):
        host: str = "mysql"
    class SubClass3(SubClass2):
        host: str = "oracle"
    class Config(TemplateConfig):
        subconfig: SubClass2 = SubClass3()

    assert Config().subconfig.host == "oracle"
    
    monkeypatch.setenv('SUBCONFIG__PORT', '2345')
    assert Config().subconfig.port == 2345
    assert Config().subconfig.host == "mysql"
    # because it needs to init subconfig