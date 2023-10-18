
# 2 ways to start

## Way 1 -- init folder with configuration files by dynaconf CLI

The example of usage

~/tmp$ dynaconf init --format=yaml

    ⚙️  Configuring your Dynaconf environment
    ------------------------------------------
    🐍 The file `config.py` was generated.
      on your code now use `from config import settings`.
      (you must have `config` importable in your PYTHONPATH).
    
    🎛️  settings.yaml created to hold your settings.
    
    🔑 .secrets.yaml created to hold your secrets.
    
    🙈 the .secrets.yaml is also included in `.gitignore`
      beware to not push your secrets to a public repo
      or use dynaconf builtin support for Vault Servers.
    
    🎉 Dynaconf is configured! read more on https://dynaconf.com
       Use `dynaconf -i config.settings list` to see your settings

connect@pc-win:~/tmp$ cat config.py

    from dynaconf import Dynaconf
    
    settings = Dynaconf(
        envvar_prefix="DYNACONF",
        settings_files=['settings.yaml', '.secrets.yaml'],
    )
    
    # `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
    # `settings_files` = Load these files in the order.

connect@pc-win:~/tmp$ cat settings.yaml

    --- {}


connect@pc-win:~/tmp$ cat .secrets.yaml

    --- {}

connect@pc-win:~/tmp$ cat .gitignore

    # Ignore dynaconf secret files
    .secrets.*

## Way 2 -- use this repo as a template


# How it works

1. config.py -- the files to init configuration library with your parameters.
2. Just import settings in any module and use it `from config import settings`
3. 