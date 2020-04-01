import copy

from typing import List

class Solution:

    def __init__(self):

        self.impsible_block = []
        for y in range(9):
            self.impsible_block.append([''] * 9)
        self.posible_block = []
        for y in range(9):
            self.posible_block.append([''] * 9)

    def getPosibleblock(self):
        return self.posible_block

    def getImposibleblock(self):
        return self.impsible_block
        


    def solveSudoku(self, board: List[List[str]], onestep=False) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # question = board
        question = copy.deepcopy(board)
        question = self.solve(question,onestep)

        if onestep :
            for y in range(9):
                board[y] = question[y]
            return
                # print(question[y])
        # for y in range(9):
        #     for x in range(9):
        #         print(x,y,question[y][x],impsible_block[y][x])
        minposible = 9
        stack_solve = []
        for i in range(2,9):
            for y in range(9):
                for x in range(9):
                    if len(self.posible_block[y][x]) == i:
                        stack_solve.append([x,y,self.posible_block[y][x]])



        for i in range(len(stack_solve)):
            alist = []
            for j in stack_solve[:i+1]:
                j = [ (j[0],j[1], x ) for x in j[2]  ]
                
                alist.append(j)

            from itertools import product
            loop_val = alist
            for i in product(*loop_val):
                question1 = copy.deepcopy(question)
                for e in i :
                    question1[e[1]][e[0]] = e[2]
                question1 = self.solve(question1,onestep)

                if self.isFinished(question1):
                    # print("done")
                    question = question1
                    break
                else:
                    # print("not done")
                    pass
                    # if noResult(posible_block):
                    #     print("the answer is fail")
                    # else:
                    #     print("continue")
            else:        # else1
                continue
            break 


                    
        # board = copy.deepcopy(question)   
        for y in range(9):
            board[y] = question[y]
                # print(question[y])

        
    def isFinished( self,question ):
        for line in question:
            if "." in line:
                return False
        return True

    def noResult(self, posible_block):
        for y in range(9):
            for x in range(9):
                if len(posible_block[y][x]) != 0:
                    return  False
        return True
        

    def posible(self, x, y ,question):
        if not question[y][x] == '.' :
            return []
        test1 = ["1","2","3","4","5","6","7","8","9"]
        for i in question[y]:
            try:
                test1.remove(i)
            except:
                pass
        checky = [ question[0][x], question[1][x], question[2][x], 
                question[3][x], question[4][x], question[5][x], 
                question[6][x], question[7][x], question[8][x]]
        for i in checky: 
            try:
                test1.remove(i)
            except:
                pass

        x = x//3*3
        y = y//3*3
        checkblock = [question[y+0][x+0], question[y+0][x+1], question[y+0][x+2], 
                question[y+1][x+0], question[y+1][x+1], question[y+1][x+2], 
                question[y+2][x+0], question[y+2][x+1], question[y+2][x+2]]
        for i in checkblock:
            try:
                test1.remove(i)
            except:
                pass
        return test1 

    def imposible( self,x, y ,question):
        test1 = ["1","2","3","4","5","6","7","8","9"]
        
        if not question[y][x] == '.' :    
            # test1.remove(question[y][x])
            return test1
        else:
            checkx = question[y][:]

            imposiblesokudo = []
                        
            checky = [ question[0][x], question[1][x], question[2][x], 
                    question[3][x], question[4][x], question[5][x], 
                    question[6][x], question[7][x], question[8][x]]

            x = x//3*3
            y = y//3*3
            checkblock = [question[y+0][x+0], question[y+0][x+1], question[y+0][x+2], 
                    question[y+1][x+0], question[y+1][x+1], question[y+1][x+2], 
                    question[y+2][x+0], question[y+2][x+1], question[y+2][x+2]]

            imposiblesokudo = copy.deepcopy(checkx) + copy.deepcopy(checky) + copy.deepcopy(checkblock)
            while "." in imposiblesokudo:
                imposiblesokudo.remove(".")
            result = copy.deepcopy(sorted(list(set(imposiblesokudo))))
            return result

    # impsible_block = [[''] * 9] * 9  

    def solve(self, question,onestep):
        while True:
            count = 0
            
            for y in range(9):
                for x in range(9):
                    imposiblexy = self.imposible(x,y,question)
                    
                    self.impsible_block[y][x] = imposiblexy
                    self.posible_block[y][x] = self.posible(x,y,question)

                    # print(x, y, question[y][x],posible,impsible_block[y][x])
                    if len(self.posible_block[y][x]) ==1 :
                        # print(x, y,posible)
                        question[y][x] = self.posible_block[y][x][0]
                        count +=1
                        if onestep :
                            return question

            for y in range(0,9,3):
                for x in range(0,9,3):
                    checkblock = [self.impsible_block[y+0][x+0], self.impsible_block[y+0][x+1], self.impsible_block[y+0][x+2], 
                            self.impsible_block[y+1][x+0], self.impsible_block[y+1][x+1], self.impsible_block[y+1][x+2], 
                            self.impsible_block[y+2][x+0], self.impsible_block[y+2][x+1], self.impsible_block[y+2][x+2]]
                    # print(checkblock)
                    # print([ question[y+0][x+0], question[y+0][x+1], question[y+0][x+2], 
                    #         question[y+1][x+0], question[y+1][x+1], question[y+1][x+2], 
                    #         question[y+2][x+0], question[y+2][x+1], question[y+2][x+2]])

                    for i in  ['1', '2', '3', '4', '5', '6', '7', '8', '9'] :
                        
                        countblock = 0
                        for j in range(9):
                            # print (a[j])
                            if i in checkblock[j]:
                                pass
                            else:
                                countblock +=1
                                pos = j
                        if countblock == 1:
                            # print("found one",i, pos//3,pos%3)
                            # print(y+pos//3 , x+pos%3, question[y+pos//3][x+pos%3])
                            question[y+pos//3][x+pos%3] = i
                            # print(question[y+pos//3][x+pos%3])
                            count +=1
                            if onestep :
                                return question

            for y in range(0,9):
                checkblock = self.impsible_block[y]

                for i in  ['1', '2', '3', '4', '5', '6', '7', '8', '9'] :
                    
                    countblock = 0
                    for j in range(9):
                        # print (a[j])
                        if i in checkblock[j]:
                            pass
                        else:
                            countblock +=1
                            pos = j
                            
                    if countblock == 1:                    
                        # print(y+pos//3 , x+pos%3, question[y+pos//3][x+pos%3])
                        question[y][pos] = i
                        # self.display(question)
                        # print("第%d行，第%d列，只有一个答案，是：%s" % (y+1 , pos+1, question[y][pos]))

                        count +=1
                        if onestep :
                            return question

            for x in range(0,9):
                checkblock = [self.impsible_block[0][x], self.impsible_block[1][x], self.impsible_block[2][x], 
                            self.impsible_block[3][x], self.impsible_block[4][x], self.impsible_block[5][x], 
                            self.impsible_block[6][x], self.impsible_block[7][x], self.impsible_block[8][x]]

                for i in  ['1', '2', '3', '4', '5', '6', '7', '8', '9'] :
                    
                    countblock = 0
                    for j in range(9):
                        # print (a[j])
                        if i in checkblock[j]:
                            pass
                        else:
                            countblock +=1
                            pos = j
                            
                    if countblock == 1:                    
                        # print(y+pos//3 , x+pos%3, question[y+pos//3][x+pos%3])
                        question[pos][x] = i
                        # self.display(question)
                        # print("第%d行，第%d列，只有一个答案，是：%s" % (pos+1 , x+1, question[pos][x]))

                        count +=1
                        if onestep :
                            return question


            if count == 0:
                break
        return question
    def display(self, question):
    # print(chr(27)+'[2j')
    # print('\033c')
    # print('\x1bc')
        for row in question:
            print(row)

if __name__ == "__main__":
    
    question = [[".","3",".", "9",".",".", "1",".","."],
                [".",".","9", ".",".","5", ".","7","."],
                ["6",".",".", ".",".",".", ".","9","."],

                ["3","8",".", ".",".",".", ".",".","."],
                [".",".",".", "2","1",".", ".",".","6"],
                [".",".",".", ".",".",".", ".",".","4"],

                [".",".","4", "5",".",".", "7",".","2"],
                [".",".","7", ".",".","9", ".","8","."],
                [".",",",".", ".",".","7", ".",".","."]]
    s = Solution()
    s.display(question)

    s.solveSudoku(question,onestep=True)
    s.solveSudoku(question,onestep=True)
    s.solveSudoku(question,onestep=True)

    s.display(question)
