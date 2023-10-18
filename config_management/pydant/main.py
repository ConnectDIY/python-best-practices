from pprint import pprint
from pydantic_config import settings, L2, L3


if __name__ == '__main__':

    print(f"========= Run with {settings.ENV} configuration =========")

    # [1] Update the config.
    settings.NESTED[12] = {'s': {L3('12-l2'): 'l3-value'}}

    # [2] Getting value
    x = settings.NESTED.get(12)

    # [3] Pretty print of the config.
    # Here Pydantic will print UserWarning
    #   `Expected `str` but got `int` - serialized value may not be as expected`
    # It happens because NESTED[ expected type is STRING ]
    print('config file:')
    pprint(settings.model_dump())  # Please note, it prints secrets!
