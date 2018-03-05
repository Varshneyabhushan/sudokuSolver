class subTable:
    
    def __init__(self,n,table):
        self.__n = n
        self.__eles = [None for i in range(n)]
        self.__vals = []
        self.__table = table

    def setVal(self,i,val):
        self.__eles[i] = val
        if(val.getVal() != 0):
            self.__vals.append(val.getVal())

    def myeles(self):
        return self.__eles

    def contains(self,val):
        return val in self.__vals

    def addVal(self,val):
        if not val in self.__vals:
            self.__vals.append(val)

        for e in self.__eles:
            if(e != None):
                e.removePoss(val)

    def reposs(self):
        poss = []
        isChanged = False
        for i in self.__eles:
            if(i.getVal() == 0):
                poss.append(i.getPoss())
            else:
                poss.append([i.getVal()])
        
        vals = solveCons(poss)['val']

        for i in range(len(vals)):
            poss = vals[i]
            if(len(poss) == 1):
                if(poss[0] != self.__eles[i].getVal() and self.__eles[i].getVal() != 0):
                    print(self.__eles[i].getVal(),"Errorrr",poss[0])
                    isChanged = True
                elif(poss[0] != self.__eles[i].getVal() and self.__eles[i].getVal() == 0):
                    self.__eles[i].setVal(poss[0])
                    isChanged = True
            else:
                posses = self.__eles[i].getPoss()
                for poss in posses:
                    if not poss in vals[i]:
                        self.__eles[i].removePoss(poss)
                        isChanged = True
            if(isChanged):
                self.__table.isChanged = True
        

def solveCons(row):
    if(len(row) == 1):
        return { "exists" : True , "val" : row}
    else:
        head = row[0]
        tail = row[1:]
        headfinal = []
        tailfinal = [[] for k in range(len(tail))]
        for ele in head:
            reformed_tail = list(map(lambda x : [e for e in x if e != ele],tail))
            tail_val = solveCons(reformed_tail)
            if(tail_val['exists'] and (not ([] in tail_val['val']))):
                headfinal.append(ele)
                tailfinal = concatAll(tailfinal,tail_val['val'])
        if(len(head) ==0):
            return {'exists' : False , 'val' : None}
        else:
            
            return {'exists' : True , 'val' : [headfinal] + tailfinal}
            
def concatAll(lists1,lists2):
    lists0 = []
    for i in range(len(lists1)):
        resulting_list = list(lists1[i])
        resulting_list.extend([x for x in lists2[i] if x not in lists1[i]])
        lists0.append(resulting_list)
    return lists0