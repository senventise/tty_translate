import sys
import json
from utils.api import translate


guide = """python3 translate.py -h\n==>help\n
python3 translate.py -c\n==>command line mode\n
python3 translate.py -d -q <text>\n==>default mode, translate text to Simplified Chinese\n
python3 translate.py -o -f <language code a> -t <language code b> -q <text>\n==>translate text from language a to b\n
python3 translate.py list\n==>show the language code list
"""


# ordinary mode
def ordinary(f, t, q):
    data = translate(q, f, t)
    content = f+"->"+t+"\n"+data["dst"]
    return content

# command line mode


# default mode
def default(q):
    return translate(q, "auto", "zh")["dst"]


# list
def lang():
    f = open(sys.path[0]+"/lang.json").read()
    data = json.loads(f)
    for item in data:
        print(item.encode("utf-8")+"\t"+data[item].encode("utf-8"))


# test
print(ordinary("zh", "en", "这是一段没有实际意义的拉丁文"))
print(default("This is a piece of Latin that has no practical significance."))
lang()
# test end
args = sys.argv
if len(args) == 1:
    print("No arg,exit")
    sys.exit(0)
