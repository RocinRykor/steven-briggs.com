import random
import re


def replace_bbcode(text):
    bbcode = [
        r"\[b](.*?)\[/b]",
        r"\[i](.*?)\[/i]",
        r"\[u](.*?)\[/u]",
        r"\[s](.*?)\[/s]",
        r"\[\*](.*)",
        r"\[list](.*?)\[/list]",
        r"\[ul](.*?)\[/ul]",
        r"\[ol\](.*?)\[\/ol\]",
    ]
    replacement = [
        r"<strong>\g<1></strong>",
        r"<em>\g<1></em>",
        r"<span style='text-decoration: underline'>\g<1></span>",
        r"<span style='text-decoration: strikethrough'>\g<1></span>",
        r"<li>\g<1></li>",
        r"<ul>\g<1></ul>",
        r"<ul>\g<1></ul>",
        r"<ol>\g<1></ol>",
    ]
    for i in range(len(bbcode)):
        if i > 4:
            text = re.sub(bbcode[i], replacement[i], text, flags=re.DOTALL)
        else:
            text = re.sub(bbcode[i], replacement[i], text)
    text = text.replace("\n", "<br>")
    return text


def replace_markdown(text):
    markdown = [
        r"\*\*(.*?)\*\*",  # bold
        r"\_(.*?)\_",  # italic
        r"\~\~(.*?)\~\~",  # strikethrough
        r"\[(.*?)\]\((.*?)\)",  # links
        r"\n- (.*)",  # unordered list items
        r"\n1\. (.*)",  # ordered list items
        r"\n# (.*?)#",  # h1
        r"\n## (.*?)#",  # h2
        r"\n### (.*?)#",  # h3
        r"\n#### (.*?)#",  # h4
        r"\n##### (.*?)#",  # h5
        r"\n###### (.*?)#",  # h6
    ]
    replacement = [
        r"<strong>\g<1></strong>",
        r"<em>\g<1></em>",
        r"<span style='text-decoration: line-through'>\g<1></span>",
        r"<a href='\g<2>'>\g<1></a>",
        r"<li>\g<1></li>",
        r"<li>\g<1></li>",
        r"<h1>\g<1></h1>",
        r"<h2>\g<1></h2>",
        r"<h3>\g<1></h3>",
        r"<h4>\g<1></h4>",
        r"<h5>\g<1></h5>",
        r"<h6>\g<1></h6>",
    ]
    for i in range(len(markdown)):
        if i > 5:
            text = re.sub(markdown[i], replacement[i], text, flags=re.DOTALL)
        else:
            text = re.sub(markdown[i], replacement[i], text)
    text = text.replace("\n", "<br>")
    return text
