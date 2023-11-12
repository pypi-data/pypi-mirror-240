import locale
from lxml import etree
import urllib.request
import os

def read_pred_tab(WD):
    # WD = os.getcwd()
    enc = locale.getencoding()
    if not os.path.isfile("%s/pred_ls.txt" % WD):
        ls = []
        print("Downloading database")
        website = urllib.request.urlopen("https://www.mtmt.hu/kifogasolhato_folyoiratok")
        s = website.read()
        # print(s)
        html_enc = etree.HTML(s)
        td_nodes = html_enc.xpath("//td/a")
        for td in td_nodes:
            ls.append(td.text)
        ls = ls[0::2]
        with open("%s/pred_ls.txt" % WD, 'w') as ls_file:
            ls_file.write('\n'.join(str(i) for i in ls))
    else:
        ls = []
        ls_file = open("%s/pred_ls.txt" % WD, 'r')
        while True:
            line = ls_file.readline()
            if line == "":
                break
            ls.append(line.strip())
    return ls

def srch_term():
    WD = os.getcwd()
    os.system("")
    pred_ls = read_pred_tab(WD)
    tm = input("NOTE: search is based on the 2024 list. To update in current run, delete %s/pred_ls.txt manually now!\n"
               "Please enter search term!\n\033[92m" % WD)
    print("\033[0m")
    for elem in pred_ls:
        if elem.lower().__contains__(tm.lower()):
            print(elem)
    input("\n\033[92mPress any key\033[0m")

def run():
    srch_term()


if __name__ == "__main__":
    run()