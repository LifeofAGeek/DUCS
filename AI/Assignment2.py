from time import time
import copy
class SodukuSolver:
    def __init__(self,dim,fileDir):
        self.dim = dim
        self.expandedNodes = 0
        with open(fileDir) as f:
	        content = f.readlines()
	        self.board = [list(x.strip()) for x in content]
        self.rv = self.getRemainingValues()

    def __str__(self):
        string = ''
        for row in self.board:
            for x in row:
                string += x+" "
            string+='\n'
        string+= "Nodes expanded: {}".format(self.expandedNodes)
        return string

    def getDomainLength(self,lst):
        if 'x' in lst or lst == []:
            return 10
        else:
            return len(lst)

    def isSafe(self,row,col,choice):
        choiceStr = str(choice)
        for i in range(self.dim):
            if self.board[row][i] == choiceStr or self.board[i][col] ==choiceStr:
                return False

        boxR = row - (row % 3)
        boxV = col - (col % 3)
        for i in range(3):
            for j in range(3):
                if self.board[boxR + i][boxV + j] == choiceStr:
                    return False
        return True

    def getNextLocation(self):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.board[i][j] == '0':
                    return (i,j)
        return (-1,-1)

    def getNextLoctaionMRVRow(self):
        minRowCount = 10
        rowIndex = 9
        colIndex = 9
        minRow = []
        for i in range(self.dim):
            count = 0
            if '0' not in self.board[i]:
                continue
            for j in range(self.dim):
                if self.board[i][j]=='0':
                    count+=1
            if minRowCount > count:
                minRowCount = count
                minRow = self.board[i]
                rowIndex = i
        if minRow == []:
            return (-1,-1)
        for i in range(self.dim):
            if minRow[i] == '0':
                colIndex = i
                break
        return (rowIndex,colIndex)

    def getNextMRVRowCol(self):
        rvMap = list(map(self.getDomainLength,self.rv))
        minimum = min(rvMap)
        if minimum == 10:
            return (-1,-1)
        index = rvMap.index(minimum)
        return(index // 9, index % 9)


    def getNextDegreeHeuristic(self):
        maxRowCount = -1
        rowIndex = 9
        colIndex = 9
        maxRow = []
        for i in range(self.dim):
            count = 0
            if '0' not in self.board[i]:
                continue
            for j in range(self.dim):
                if self.board[i][j]=='0':
                    count+=1
            if maxRowCount < count:
                maxRowCount = count
                maxRow = self.board[i]
                rowIndex = i
        if maxRow == []:
            return (-1,-1)
        else:
            maxColCount = -1
            for i in range(self.dim):
                count = 0
                if maxRow[i] == '0':
                    for j in range(self.dim):
                        if self.board[j][i]=='0':
                            count+=1
                    if count > maxColCount:
                        maxColCount = count
                        colIndex = i
            return(rowIndex,colIndex)

    def removeValue(self,row,col,value,RV):
        RV[row*9 +col] = ['0']
        for lst in RV[row*9:row*9+9]:
            if value in lst:
                lst.remove(value)
        for i in range(self.dim):
            if value in RV[i*9+col]:
                RV[i*9+col].remove(value)
        boxRow = int(row/3)
        boxCol = int(col/3)
        for i in range(3):
            for j in range(3):
                if value in RV[(boxRow*3+i)*9 + j + boxCol*3]:
                    RV[(boxRow*3+i)*9 + j + boxCol*3].remove(value)

        #
        RV[row*9 + col] = [value]
        return RV

    def getDomain(self,row,col):
        RVCell = [str(i) for i in range(1 ,self.dim + 1)]
        for i in range(self.dim):
            if self.board[row][i] != '0':
                if self.board[row][i] in RVCell:
                    RVCell.remove(self.board[row][i])

        for i in range(self.dim):
            if self.board[i][col] != '0':
                if self.board[i][col] in RVCell:
                    RVCell.remove(self.board[i][col])

        boxRow = row - row%3
        boxCol = col - col%3
        for i in range(3):
            for j in range(3):
                if self.board[boxRow+i][boxCol+j]!=0:
                    if self.board[boxRow+i][boxCol+j] in RVCell:
                        RVCell.remove(self.board[boxRow+i][boxCol+j])
        return RVCell

    def getRemainingValues(self):
        RV=[]
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col] != '0':
                    RV.append(['x'])
                else:
                    RV.append(self.getDomain(row,col))
        return RV

    def getChoice(self,lst):
        count = [0 for i in range(len(lst))]
        for i in range(len(lst)):
            c = 0
            for j in range(self.dim):
                c += self.board[j].count(lst[i])
            count[i] = c

        return lst[count.index(min(count))]

    def isConsistent(self,row,col,value,rv):
        board = self.board[:][:]
        board[row][col] = value
        RV = []
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col] != '0':
                    digit = board[row][col]
                    RV.append([digit])
                else:
                    RVCell = [str(i) for i in range(1 ,self.dim + 1)]
                    for i in range(self.dim):
                        if board[row][i] != '0':
                            if board[row][i] in RVCell:
                                RVCell.remove(board[row][i])

                    for i in range(self.dim):
                        if board[i][col] != '0':
                            if board[i][col] in RVCell:
                                RVCell.remove(board[i][col])

                    boxRow = row - row%3
                    boxCol = col - col%3
                    for i in range(3):
                        for j in range(3):
                            if board[boxRow+i][boxCol+j]!=0:
                                if board[boxRow+i][boxCol+j] in RVCell:
                                    RVCell.remove(board[boxRow+i][boxCol+j])
                    if RVCell == []:
                        return False
        return True
    '''Solving methods'''
    def solveSimpleBackTracking(self):
        location = self.getNextLocation()
        if location[0] == -1:
            return True
        else:
            self.expandedNodes += 1
            for choice in range(1,self.dim+1):
                if self.isSafe(location[0],location[1],choice):
                    self.board[location[0]][location[1]] = str(choice)
                    if self.solveSimpleBackTracking():
                        return True
                    self.board[location[0]][location[1]] = '0'
            return False

    def solveCSP(self,locationFunction):
        location = locationFunction()

        if location[0] == -1:
            return True
        else:
            self.expandedNodes+=1
            for choice in range(1,self.dim+1):
                if self.isSafe(location[0],location[1],choice):
                    self.board[location[0]][location[1]] = str(choice)
                    if self.solveCSP(locationFunction):
                        return True
                    self.board[location[0]][location[1]] = '0'
            return False

    def isEmptyDomainProduced(self,row,col,choice):
        element = self.rv.pop(row*9 + col)
        if [] in self.rv:
            self.rv.insert(row*9+col,element)
            return True
        else:
            self.rv.insert(row*9+col,element)
            return False
                

    def solveCSPFH(self):
        location = self.getNextMRVRowCol()
        if location[0] == -1:
            return True
        else:
            self.expandedNodes+=1
            # rv = self.getRemainingValues()
            row = location[0]
            col = location[1]
            for choice in self.rv[row*9+col]:
                choice_str = str(choice)
                self.board[row][col] =  choice_str
                cpy = copy.deepcopy(self.rv) 
                self.rv = self.getRemainingValues()
                
                if not self.isEmptyDomainProduced(row,col,choice_str):
                    if self.solveCSPFH():
                        return True
                self.board[row][col] = '0'
                self.rv = cpy

            return False



file = 's2'
s = SodukuSolver(9,'testCases/{}.txt'.format(file))
start = time()
# s.solveCSP(s.getNextDegreeHeuristic)
# s.solveSimpleBackTracking()
s.solveCSPFH()
end = time()
print(s)
print("Time Elapsed:{}".format(end-start))

