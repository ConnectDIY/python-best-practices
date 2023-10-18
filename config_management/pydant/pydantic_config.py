# from pydantic import BaseSettings  # for pydantic < 2
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import NewType, Dict, Any

"""
This file is your pydantic config file.
It describes pydantic models == options in your settings variable.

"""

L1 = str
L2 = NewType('L2', str)
L3 = NewType('L3', str)
L4 = NewType('L4', str)


class Secrets(BaseModel):
    """Just SubModel example."""
    SECRET_KEY: str = "pwd-in-pydantic-cfg"
    PASSWORD: str
    TOKEN: str


class Base(BaseSettings):
    """
    This class automatically loads and overwrite ENV variables.

    You need to describe your parameters here.
        Option_name: type

    This class called a Model.
    You can have nested models if you want (SubModel in this example below).
    """
    # NOTE:
    #   model_config - is not a config parameter. This is settings class-configuration parameter.
    model_config = SettingsConfigDict(
        env_nested_delimiter='.',
        # If you need to load multiple dotenv files, you can pass multiple file paths
        # as a tuple or list. The files will be loaded in order, with each file overriding
        # the previous one.
        # `.env.prod` takes priority over `.env`
        env_file=('../.env', '../.secrets', '.env.prod', '.secrets.prod'),
        # If you have secrets as separate files.
        # https://docs.pydantic.dev/latest/concepts/pydantic_settings/#secrets
        # Doesn't work with NESTED for some reason. Perhaps a lib bug.
        # secrets_dir='./secrets',  # Path to the folder with secret files
    )

    ENV: str
    PORT: int = 5050
    USERNAME: str = "Slavik"
    NAME: str  # Required parameter without default value.
               # App will raise exception if it is not initialized.

    # Not very convenient work with nested fields because you need to
    #   describe every field.
    NESTED: Dict[L1, Dict[L2, Dict[L3, Any]]] = {
        'l1-1': {
            'l2-1': {
                'l3-1': 1
            }
        },
        'l1-2': {
            'l2-2': {
                'l3-2': 'asb'
            }
        },
        'l1-3': {
            'l2-3': {
                'l3-3': 'asd'
            }
        },

    }

    SECRETS: Secrets


settings = Base()  # After that you can import this variable everywhere in your code.
