def perevod_vlada(text):
    slovar_perevoda = {'q':'й', 'w':'ц', 'e':'у', 'r':'к', 't':'е', 'y':'н', 'u':'г', 'i':'ш', 'o':'щ', 'p':'з', 
                       '[':'х', ']':'ъ', 'a':'ф', 's':'ы', 'd':'в', 'f':'а', 'g':'п', 'h':'р', 'j':'о', 'k':'л',
                       'l':'д', ';':'ж', '"':'э', 'z':'я', 'x':'ч', 'c':'с', 'v':'м', 'b':'и', 'n':'т', 'm':'ь', ',' : 'б', '.': 'ю'}
    nach_letters, rez = list(slovar_perevoda.keys()), ''
    rez = ''.join([i if i not in nach_letters else str(slovar_perevoda.get(str(i))) for i in text])
    print(rez)

perevod_vlada('dkfl crhsnsq utq f vj;tn ,snm b ytn ')