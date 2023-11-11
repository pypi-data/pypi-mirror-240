import locale

import pandas as pd
import lxml
import os

def read_pred_tab():
    WD = os.getcwd()
    print(locale.getencoding())
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
    tm = input("Please enter search term!\n")
    pred_ls = read_pred_tab()
    for elem in pred_ls:
        if elem.__contains__(tm):
            print(elem)

def run():
    srch_term()


if __name__ == "__main__":
    run()