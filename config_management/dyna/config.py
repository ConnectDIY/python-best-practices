from dynaconf import Dynaconf

settings = Dynaconf(
    # TODO -- don't want to work with custom prefix for some reason.
    #   Works only with default `DYNACONF_` prefix.
    #   It doesn't matter will you provide envvar_prefix or not.
    envvar_prefix="A_",
    # It is also possible to make dynaconf read the files separated by layered
    # environments so each section or first level key is loaded as a distinct environment.
    # dynaconf.com/settings_files/#layered-environments-on-files
    # Config will look like
    #       default:
    #           name: ''
    #       development:
    #           name: developer
    #       production:
    #           name: admin
    # environments=True,

    # It can read only file with .env that placed next to the entry-point script.
    load_dotenv=True,
    # You cannot read .env files here as in pydantic, but you can read toml, yaml, json, in, py
    settings_files=['../config.yaml', 'secrets.yaml'],  # Load these files in the order.
)

