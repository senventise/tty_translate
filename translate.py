#!/bin/python
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

guide = """python3 translate.py -h\n==>帮助\n
python3 translate.py -c\n==>命令行模式\n
python3 translate.py -d -q <文本>\n==>将任何语言的文本翻译成中文\n
python3 translate.py -o -f <语言代码 a> -t <语言代码 b> -q <text>\n==>把文本从语言 a 翻译为语言 b\n
python3 translate.py list\n==>显示语言代码

为避免不必要的麻烦,参数请务必加引号!

示例:将 "I swear I lived" 翻译为繁体中文:python translate.py -o -f "en" -t "cht" -q "I swear I lived"
"""

cmd_guide = """
@from <语言代码>     更改原文语言
@to <语言代码>       更改译文语言
@exit               退出

"""


# ordinary mode
def ordinary(f, t, q):
    data = translate(q, f, t)
    content = json.loads(language_list)[f]+"->"+json.loads(language_list)[t]+"\n"+data["dst"]
    return content


# command line mode
def cmd():
    f = "auto"
    t = "zh"
    print(cmd_guide)
    while 1:
        inp = input(">")
        if len(inp.replace(" ","")) == 0:
            #no input, do nothing
        elif "@from" == inp.split(" ")[0]:
            f = inp.split(" ")[1]
            print("原文语言已变更为:"+json.loads(language_list)[f])
        elif "@to" == inp.split(" ")[0]:
            t = inp.split(" ")[1]
            print("译文语言已变更为:"+json.loads(language_list)[t])
        elif "@exit" == inp.split(" ")[0]:
            sys.exit(0)
            print("已退出")
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
    print("没有指令")
    sys.exit(0)
else:
    if args[1] == "-o":
        if not (args[2] == "-f" and args[4] == "-t" and args[6 == "-q"]):
            print("指令有误")
            sys.exit(0)
        print(ordinary(args[3], args[5], args[7]))
    elif args[1] == "-d":
        if not (args[2] == "-q"):
            print("指令有误")
            sys.exit(0)
        print(default(args[3]))
    elif args[1] == "-c":
        cmd()
    elif args[1] == "-h":
        print(guide)
    elif args[1] == "list":
        lang()
    else:
        print("指令有误")
