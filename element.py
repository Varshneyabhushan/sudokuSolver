class element:
    def __init__(self,table,row,col,block):
        self.__val = 0
        self.__poss = []
        self.__row = row
        self.__col = col
        self.__block = block
        self.__table = table

    def setVal(self,val):
        if(self.__row.contains(val) or self.__col.contains(val) or self.__block.contains(val)):
            self.__table.expired = True
        self.__val = val
        self.__table.solved += 1
        self.clearPoss()
        self.__block.addVal(val)
        self.__col.addVal(val)
        self.__row.addVal(val)
        
    def myRow(self):
        return self.__row

    def myCol(self):
        return self.__col
    
    def myBlock(self):
        return self.__block

    def markPoss(self,val):
        if not val in self.__poss:
            self.__poss.append(val)

    def clearPoss(self):
        self.__poss = []

    def getVal(self):
        return self.__val

    def getPoss(self):
        return self.__poss

    def removePoss(self,val):
        if val in self.__poss:
            self.__poss.remove(val)
            if(len(self.__poss) == 1 and self.__val == 0):
                self.setVal(self.__poss[0])
            
