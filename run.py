def finds_parterns_frequency(seqA, seqB, low, high): 
    
    sqm1 = seqA.upper()
    sqm2 = seqB.upper()
    dic = {}
    temp = []


    while(low <= high):
        for i in range(len(sqm1)-low + 1):
            sub_seq = sqm1[i: i+low]
            if sub_seq not in dic.keys():
                dic[sub_seq] = 0
                temp.append(sub_seq)
        
        for i in range(len(sqm2)-low + 1):
            if sqm2[i: i+low] in temp:
                dic[sqm2[i: i+low]] += 1

        temp = []
        low += 1
    
    return sorted(dic.items(), key=lambda x: x[1], reverse = True)


def test():
    seqA = "MTSRTKKLKMDEEEILKKEDGSETTSEEEKEEVEEEEEEDKKRKLVKKTPAKKAPAKKAAAKKKSKDEDEDEEEKEEEEETNKTTASVSIAIDNLDEPKVEENQMKIISWNVAGFKSVLSKGFTEYVEKENPDVLCLQETKINPSNIKKDQMPKGYEYHFIEADQKGHHGTGVLTKKKPNAITFGIGIAKHDNEGRVITLEYDQFYIVNTYIPNAGTRGLQRLDYRIKEWDVDFQAYLEKLNATKPIIWCGDLNVAHTEIDLKNPKTNKKSAGFTIEERTSFSNFLEKGYVDSYRHFNPGKEGSYTFWSYLGGGRSKNVGWRLDYFVVSKRLMDSIKISPFHRTSVMGSDHCPIGVVVDLN"
    seqB = "MPKRGKKGAVAEDGDELKTEPEAKKSKTAAKKNDKEAAGEGPALYEDPPDQKTSPSGKPATLKICSWNVDGLRAWIKKKGLDWVKEEAPDILCLQETKCSENKLPAELQELPGLSYQYWSAPXXKEGYSGVGLLSRQCPLKVSYGIGEEEHDQEGRVIVAEFDSFVLVTAYVPNAGRGLVRLEYRQRWDEAFRRFLKGLASRKPLVLCGDLNVAHEEIDLRNPKGNKKNAGFTPQERQGFGELLQAVPLADSFRHLYPNTPYAYTFWTYMMNARSKNVGWRLDYFLLSHSLLPALCDSKIRSKALGSDHCPITLYLAL"
    
    dic = finds_parterns_frequency(seqA,seqB,2,3)

    for k,v in dic:
        print("", k ," - " , v)

    ##print("Out:", finds_parterns_frequency(seqA,seqB,2,3))



if __name__ == "__main__":
    test()
    
