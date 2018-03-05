from subTable import subTable
from element import element
from copy import deepcopy
from time import clock

class sudoku:
    def __init__(self,vals):
        self.__n = len(vals)
        self.__rows = []
        self.__cols = []
        self.__eles = []
        self.blocks = []
        self.isChanged = False
        self.solved = 0
        self.expired = False
        self.Iterations = 0
        self.guesses = 0

        for i in range(self.__n):
            x = subTable(self.__n,self)
            y = subTable(self.__n,self)
            z = subTable(self.__n,self)
            self.__rows.append(x)
            self.__cols.append(y)
            self.blocks.append(z)

        for i in range(self.__n):
            for j in range(self.__n):
                b = 3*(i//3) + (j//3)
                e = element(self,self.__rows[i],self.__cols[j],self.blocks[b])
                if(vals[i][j] != 0):
                    e.setVal(vals[i][j])
                self.__rows[i].setVal(j,e)
                self.__cols[j].setVal(i,e)
                self.blocks[b].setVal( 3*(i%3) + j%3,e)
                self.__eles.append(e)
                
        for i in self.__eles:
            for n in range(self.__n):
                if(i.getVal() == 0):
                    if not (i.myRow().contains(n+1) or i.myCol().contains(n+1) or i.myBlock().contains(n+1)):
                        i.markPoss(n+1)

    def markOut(self):
        for i in self.__rows:
            i.reposs()
        
        for i in self.__cols:
            i.reposs()
        
        for i in self.blocks:
            i.reposs()

    def solve(self):
        clock()
        self.Iterations += 1
        self.isChanged = False
        self.markOut()
        if(self.isChanged):
            return self.solve()
        else:
            if self.expired: #wrong puzzle
                return {
                    'done' : False,
                    'iterations' : self.Iterations - 1 ,
                    'guesses' : self.guesses,
                    'timeTaken' : clock(),
                    'solution' : None}
            elif(self.solved == self.__n**2): #solved
                return {
                    'done' : True ,
                    'iterations' : self.Iterations - 1 ,
                    'guesses' : self.guesses,
                    'timeTaken' : clock(),
                    'solution' : self.myTable() }
            else: #unsolved
                return self.guessOne()

    def myTable(self):
        table = []
        for i in self.__rows:
            row = []
            for ele in i.myeles():
                if(ele.getVal() == 0):
                    row.append(" ")
                else:
                    row.append(ele.getVal())
            table.append(row)
        return table

    def guessOne(self):
        self.guesses += 1
        selected = 0
        itrs = []
        for i in range(len(self.__eles)):
            posses = self.__eles[i].getPoss()
            if(len(posses) != 0):
                selected = i
                itrs = posses
                break
        
        for i in itrs:
            newTab = deepcopy(self)
            newTab.__eles[selected].setVal(i)
            ss = newTab.solve()
            if(ss['done']):
                return ss


