

Use this `check_copyright.py` script to check that all files have copyright in 
the beginning of the file.


### Precommit
repos:
  - repo: local
    hooks:
      - id: check_copyright
        name: check_copyright
        stages: [ commit ]
        entry: python check_copyright.py copyright.txt ./th2_data_services
        language: python
        pass_filenames: false
        always_run: true

### GitHub CI
???