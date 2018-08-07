import sys
import json
from utils.api import translate


language_list = """{
"zh":"中文",
"en":"英语",
"yue":"粤语",
"wyw":"文言文",
"jp":"日语",
"kor":"韩语",
"fra":"法语",
"spa":"西班牙语",
"th":"泰语",
"ara":"阿拉伯语",
"ru":"俄语",
"pt":"葡萄牙语",
"de":"德语",
"it":"意大利语",
"el":"希腊语",
"nl":"荷兰语",
"pl":"波兰语",
"bul":"保加利亚语",
"est":"爱沙尼亚语",
"dan":"丹麦语",
"fin":"芬兰语",
"cs":"捷克语",
"rom":"罗马尼亚语",
"slo":"斯洛文尼亚语",
"swe":"瑞典语",
"hu":"匈牙利语",
"cht":"繁体中文",
"vie":"越南语"
}"""

guide = """python3 translate.py -h\n==>help\n
python3 translate.py -c\n==>command line mode\n
python3 translate.py -d -q <text>\n==>default mode, translate text to Simplified Chinese\n
python3 translate.py -o -f <language code a> -t <language code b> -q <text>\n==>translate text from language a to b\n
python3 translate.py list\n==>show the language code list
"""

cmd_guide = """
@from <language code>
@to <language>
<text> translate 
"""


# ordinary mode
def ordinary(f, t, q):
    data = translate(q, f, t)
    content = f+"->"+t+"\n"+data["dst"]
    return content


# command line mode
def cmd():
    f = "auto"
    t = "zh"
    print(cmd_guide)
    while 1:
        inp = input(">")
        if "@from" == inp.split(" ")[0]:
            f = inp.split(" ")[1]
        elif "@to" == inp.split(" ")[0]:
            t = inp.split(" ")[1]
        elif "@exit" == inp.split(" ")[0]:
            sys.exit(0)
        else:
            print(translate(inp, f, t)["dst"])


# default mode
def default(q):
    return translate(q, "auto", "zh")["dst"]


# list
def lang():
    data = json.loads(language_list)
    for item in data:
        print(item+"\t\t"+data[item])


# arg explain
args = sys.argv
if len(args) == 1:
    print("No arg,exit")
    sys.exit(0)
else:
    if args[1] == "-o":
        print(ordinary(args[3], args[5], args[7]))
    elif args[1] == "-d":
        print(default(args[3]))
    elif args[1] == "-c":
        cmd()
    elif args[1] == "-h":
        print(guide)
    elif args[1] == "list":
        lang()
    else:
        print("wrong")
