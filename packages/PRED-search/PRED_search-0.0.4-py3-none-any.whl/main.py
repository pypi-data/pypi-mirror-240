import locale

import pandas as pd
import lxml
import os

def read_pred_tab(WD):
    enc = locale.getencoding()
    if not os.path.isfile("%s/pred_ls.txt"):
        df = pd.read_html("https://www.mtmt.hu/kifogasolhato_folyoiratok")[0]
        ls = df.iloc[:, 0]
        with open("%s/pred_ls.txt" % WD, 'w', encoding="utf") as ls_file:
            ls_file.write('\n'.join(str(i) for i in ls))
    else:
        ls = []
        ls_file = open("%s/pred_ls.txt" % WD, 'w')
        while True:
            line = ls_file.readline()
            if line == "":
                break
            ls.append(line)
    return ls

def srch_term():
    WD = os.getcwd()
    tm = input("NOTE: search is based on the 2024 list. To update in current run, delete %s/pred_ls.txt manually now!\n"
               "Please enter search term!\n\033[92m" % WD)
    pred_ls = read_pred_tab(WD)
    print("\033[0m")
    for elem in pred_ls:
        if elem.lower().__contains__(tm.lower()):
            print(elem)

def run():
    srch_term()


if __name__ == "__main__":
    run()