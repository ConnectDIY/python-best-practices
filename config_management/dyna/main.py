from pprint import pprint

from config import settings

if __name__ == '__main__':

    print(f"========= Run with {settings.ENV} configuration =========")

    # [1] Update the config.
    settings.A = 2
    settings.NESTED[12] = {'s': {'12-l2': 'l3-value'}}

    # [2] Getting value
    x = settings.NESTED.get(12)

    # [3] Pretty print of the config.
    print('config file:')
    pprint(settings.to_dict())  # Please note, it prints secrets!

