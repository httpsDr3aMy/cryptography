shifted_alfabet = 'PAWEŁ'
znak_list = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ'
aha = []
for i in shifted_alfabet:
    for x in znak_list:
        if i == x:
            aha.append(1)
        else:
            aha.append(0)
