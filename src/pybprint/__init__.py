import colorama
from colorama import Fore, Back, Style
import re


colorama.init(autoreset=True)


def addMissing(counter, box, boxSize):
    missing=boxSize-counter
    for i in range(missing):
        box+=" "
    box+="║"
    return box

def bprint(text, inBox=False, boxSize=100):

    text = "<|fR>"+text

    style = re.compile("<|s.>")
    if re.match(style, text):
        #STYLES REPLACEMENTS
        text=text.replace("<|sd>", Style.DIM)
        text=text.replace("<|sn>", Style.NORMAL)
        text=text.replace("<|sb>", Style.BRIGHT)


    back = re.compile("<|b.>")
    if re.match(back, text):
        #BACK REPLACEMENTS
        text=text.replace("<|br>", Back.RED)
        text=text.replace("<|bg>", Back.GREEN)
        text=text.replace("<|bb>", Back.BLUE)
        text=text.replace("<|bw>", Back.WHITE)
        text=text.replace("<|by>", Back.YELLOW)
        text=text.replace("<|bm>", Back.MAGENTA)
        text=text.replace("<|bc>", Back.CYAN)
        text=text.replace("<|bB>", Back.BLACK)
        text=text.replace("<|bR>", Back.RESET)

    fore = re.compile("<|f.>")
    if re.match(fore, text):
        #FORE REPLACEMENTS
        text=text.replace("<|fr>", Fore.RED)
        text=text.replace("<|fg>", Fore.GREEN)
        text=text.replace("<|fb>", Fore.BLUE)
        text=text.replace("<|fw>", Fore.WHITE)
        text=text.replace("<|fy>", Fore.YELLOW)
        text=text.replace("<|fm>", Fore.MAGENTA)
        text=text.replace("<|fc>", Fore.CYAN)
        text=text.replace("<|fB>", Fore.BLACK)
        text=text.replace("<|fR>", Fore.RESET)
    

    if inBox:
        #Boxes the text
        if boxSize < 3:
            boxSize=3

        boxSize=boxSize-2
        box="╔"
        for i in range(boxSize):
            box+="═"
        box+="╗\n║"

        toSkip=0
        counter=0

        text=text.replace("\t", "    ")

        for c in text:
            if toSkip!=0:
                toSkip-=1
                counter-=1
                c=""

            if c == "\n":
                box=addMissing(counter, box, boxSize)
                box+="\n║"
                c=""
                counter=-1

            if c == "":
                c=""
                counter-=1
                toSkip=4
                
            if counter==boxSize and counter!=0:
                box+="║\n║"
                counter=0
            box+=c
            counter+=1

        box = addMissing(counter, box, boxSize)

        box+="\n╚"
        for i in range(boxSize):
            box+="═"
        box+="╝"

        text=box

    print(text)
    return text
