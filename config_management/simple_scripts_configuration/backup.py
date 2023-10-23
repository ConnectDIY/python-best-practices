from zipfile import ZipFile, ZIP_DEFLATED

COMPRESSED_FILENAME = 'backup.zip'
LIST_OF_FILES_TO_COMPRESS = [
    'pretty_print_json_cli.py',
]

if __name__ == '__main__':
    with ZipFile(COMPRESSED_FILENAME, 'w', compression=ZIP_DEFLATED) as myzip:
        for fname in LIST_OF_FILES_TO_COMPRESS:
            myzip.write(fname)
