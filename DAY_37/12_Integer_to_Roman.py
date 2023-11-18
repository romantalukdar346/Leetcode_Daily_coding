def intToRoman( num):
    mapping=[[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],
            [50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]
    roman=''
    for i in range(len(mapping)):

        while num>= mapping[i][0]:
            num-=mapping[i][0]
            roman+= mapping[i][1]
    return roman

