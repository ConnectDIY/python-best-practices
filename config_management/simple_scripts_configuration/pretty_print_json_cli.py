import sys
import json

"""
Execute this CLI command to test the script:

python pretty_print_json_cli.py '[{"ID":10,"Name":"Pankaj","Role":"CEO"}, 
{"ID":20,"Name":"David Lee","Role":"Editor"}]'
"""

if __name__ == '__main__':
    args = sys.argv[1:]  # 0 item is a script name.

    if not args:
        print("Json string isn't provided")
        exit(-1)

    json_str = args[0]

    json_object = json.loads(json_str)
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)
