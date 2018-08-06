import sys
import json

path = sys.path[0]+"/.config"
print("loading: "+path)
config = json.loads(open(path).read())


def get_id():
    if "APPID" in config:
        return str(config["APPID"])
    else:
        print("NO APPID")
        sys.exit(0)


def get_key():
    if "KEY" in config:
        return str(config["KEY"])
    else:
        print("NO KEY")
        sys.exit(0)
