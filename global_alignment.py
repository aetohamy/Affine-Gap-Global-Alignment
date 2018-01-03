#===================================================BLOSUM MATRIX==============================================#
BLOSUM80 = {
           'A':{'A':5,'R':-2,'N':-2,'D':-2,'C':-1,'Q':-1,'E':-1,'G':0,'H':-2,'I':-2,'L':-2,'K':-1,'M':-1,'F':-3,'P':-1,'S':1,'T':0,'W':-3,'Y':-2,'V':0,'B':-2,'J':-2,'Z':-1,'X':-1,'*':-6},
           'R':{'A':-2,'R':6,'N':-1,'D':-2,'C':-4,'Q':1,'E':-1,'G':-3,'H':0,'I':-3,'L':-3,'K':2,'M':-2,'F':-4,'P':-2,'S':-1,'T':-1,'W':-4,'Y':-3,'V':-3,'B':-1,'J':-3,'Z':0,'X':-1,'*':-6},
           'N':{'A':-2,'R':-1,'N':6,'D':1,'C':-3,'Q':0,'E':-1,'G':-1,'H':0,'I':-4,'L':-4,'K':0,'M':-3,'F':-4,'P':-3,'S':0,'T':0,'W':-4,'Y':-3,'V':-4,'B':5,'J':-4,'Z':0,'X':-1,'*':-6},
           'D':{'A':-2,'R':-2,'N':1,'D':6,'C':-4,'Q':-1,'E':1,'G':-2,'H':-2,'I':-4,'L':-5,'K':-1,'M':-4,'F':-4,'P':-2,'S':-1,'T':-1,'W':-6,'Y':-4,'V':-4,'B':5,'J':-5,'Z':1,'X':-1,'*':-6},
           'C':{'A':-1,'R':-4,'N':-3,'D':-4,'C':9,'Q':-4,'E':-5,'G':-4,'H':-4,'I':-2,'L':-2,'K':-4,'M':-2,'F':-3,'P':-4,'S':-2,'T':-1,'W':-3,'Y':-3,'V':-1,'B':-4,'J':-2,'Z':-4,'X':-1,'*':-6},
           'Q':{'A':-1,'R':1,'N':0,'D':-1,'C':-4,'Q':6,'E':2,'G':-2,'H':1,'I':-3,'L':-3,'K':1,'M':0,'F':-4,'P':-2,'S':0,'T':-1,'W':-3,'Y':-2,'V':-3,'B':0,'J':-3,'Z':4,'X':-1,'*':-6},
           'E':{'A':-1,'R':-1,'N':-1,'D':1,'C':-5,'Q':2,'E':6,'G':-3,'H':0,'I':-4,'L':-4,'K':1,'M':-2,'F':-4,'P':-2,'S':0,'T':-1,'W':-4,'Y':-3,'V':-3,'B':1,'J':-4,'Z':5,'X':-1,'*':-6},
           'G':{'A':0,'R':-3,'N':-1,'D':-2,'C':-4,'Q':-2,'E':-3,'G':6,'H':-3,'I':-5,'L':-4,'K':-2,'M':-4,'F':-4,'P':-3,'S':-1,'T':-2,'W':-4,'Y':-4,'V':-4,'B':-1,'J':-5,'Z':-3,'X':-1,'*':-6},
           'H':{'A':-2,'R':0,'N':0,'D':-2,'C':-4,'Q':1,'E':0,'G':-3,'H':8,'I':-4,'L':-3,'K':-1,'M':-2,'F':-2,'P':-3,'S':-1,'T':-2,'W':-3,'Y':2,'V':-4,'B':-1,'J':-4,'Z':0,'X':-1,'*':-6},
           'I':{'A':-2,'R':-3,'N':-4,'D':-4,'C':-2,'Q':-3,'E':-4,'G':-5,'H':-4,'I':5,'L':1,'K':-3,'M':1,'F':-1,'P':-4,'S':-3,'T':-1,'W':-3,'Y':-2,'V':3,'B':-4,'J':3,'Z':-4,'X':-1,'*':-6},
           'L':{'A':-2,'R':-3,'N':-4,'D':-5,'C':-2,'Q':-3,'E':-4,'G':-4,'H':-3,'I':1,'L':4,'K':-3,'M':2,'F':0,'P':-3,'S':-3,'T':-2,'W':-2,'Y':-2,'V':1,'B':-4,'J':3,'Z':-3,'X':-1,'*':-6},
           'K':{'A':-1,'R':2,'N':0,'D':-1,'C':-4,'Q':1,'E':1,'G':-2,'H':-1,'I':-3,'L':-3,'K':5,'M':-2,'F':-4,'P':-1,'S':-1,'T':-1,'W':-4,'Y':-3,'V':-3,'B':-1,'J':-3,'Z':1,'X':-1,'*':-6},
           'M':{'A':-1,'R':-2,'N':-3,'D':-4,'C':-2,'Q':0,'E':-2,'G':-4,'H':-2,'I':1,'L':2,'K':-2,'M':6,'F':0,'P':-3,'S':-2,'T':-1,'W':-2,'Y':-2,'V':1,'B':-3,'J':2,'Z':-1,'X':-1,'*':-6},
           'F':{'A':-3,'R':-4,'N':-4,'D':-4,'C':-3,'Q':-4,'E':-4,'G':-4,'H':-2,'I':-1,'L':0,'K':-4,'M':0,'F':6,'P':-4,'S':-3,'T':-2,'W':0,'Y':3,'V':-1,'B':-4,'J':0,'Z':-4,'X':-1,'*':-6},
           'P':{'A':-1,'R':-2,'N':-3,'D':-2,'C':-4,'Q':-2,'E':-2,'G':-3,'H':-3,'I':-4,'L':-3,'K':-1,'M':-3,'F':-4,'P':8,'S':-1,'T':-2,'W':-5,'Y':-4,'V':-3,'B':-2,'J':-4,'Z':-2,'X':-1,'*':-6},
           'S':{'A':1,'R':-1,'N':0,'D':-1,'C':-2,'Q':0,'E':0,'G':-1,'H':-1,'I':-3,'L':-3,'K':-1,'M':-2,'F':-3,'P':-1,'S':5,'T':1,'W':-4,'Y':-2,'V':-2,'B':0,'J':-3,'Z':0,'X':-1,'*':-6},
           'T':{'A':0,'R':-1,'N':0,'D':-1,'C':-1,'Q':-1,'E':-1,'G':-2,'H':-2,'I':-1,'L':-2,'K':-1,'M':-1,'F':-2,'P':-2,'S':1,'T':5,'W':-4,'Y':-2,'V':0,'B':-1,'J':-1,'Z':-1,'X':-1,'*':-6},
           'W':{'A':-3,'R':-4,'N':-4,'D':-6,'C':-3,'Q':-3,'E':-4,'G':-4,'H':-3,'I':-3,'L':-2,'K':-4,'M':-2,'F':0,'P':-5,'S':-4,'T':-4,'W':11,'Y':2,'V':-3,'B':-5,'J':-3,'Z':-3,'X':-1,'*':-6},
           'Y':{'A':-2,'R':-3,'N':-3,'D':-4,'C':-3,'Q':-2,'E':-3,'G':-4,'H':2,'I':-2,'L':-2,'K':-3,'M':-2,'F':3,'P':-4,'S':-2,'T':-2,'W':2,'Y':7,'V':-2,'B':-3,'J':-2,'Z':-3,'X':-1,'*':-6},
           'V':{'A':0,'R':-3,'N':-4,'D':-4,'C':-1,'Q':-3,'E':-3,'G':-4,'H':-4,'I':3,'L':1,'K':-3,'M':1,'F':-1,'P':-3,'S':-2,'T':0,'W':-3,'Y':-2,'V':4,'B':-4,'J':2,'Z':-3,'X':-1,'*':-6},
           'B':{'A':-2,'R':-1,'N':5,'D':5,'C':-4,'Q':0,'E':1,'G':-1,'H':-1,'I':-4,'L':-4,'K':-1,'M':-3,'F':-4,'P':-2,'S':0,'T':-1,'W':-5,'Y':-3,'V':-4,'B':5,'J':-4,'Z':0,'X':-1,'*':-6},
           'J':{'A':-2,'R':-3,'N':-4,'D':-5,'C':-2,'Q':-3,'E':-4,'G':-5,'H':-4,'I':3,'L':3,'K':-3,'M':2,'F':0,'P':-4,'S':-3,'T':-1,'W':-3,'Y':-2,'V':2,'B':-4,'J':3,'Z':-3,'X':-1,'*':-6},
           'Z':{'A':-1,'R':0,'N':0,'D':1,'C':-4,'Q':4,'E':5,'G':-3,'H':0,'I':-4,'L':-3,'K':1,'M':-1,'F':-4,'P':-2,'S':0,'T':-1,'W':-3,'Y':-3,'V':-3,'B':0,'J':-3,'Z':5,'X':-1,'*':-6},
           'X':{'A':-1,'R':-1,'N':-1,'D':-1,'C':-1,'Q':-1,'E':-1,'G':-1,'H':-1,'I':-1,'L':-1,'K':-1,'M':-1,'F':-1,'P':-1,'S':-1,'T':-1,'W':-1,'Y':-1,'V':-1,'B':-1,'J':-1,'Z':-1,'X':-1,'*':-6},
           '*':{'A':-6,'R':-6,'N':-6,'D':-6,'C':-6,'Q':-6,'E':-6,'G':-6,'H':-6,'I':-6,'L':-6,'K':-6,'M':-6,'F':-6,'P':-6,'S':-6,'T':-6,'W':-6,'Y':-6,'V':-6,'B':-6,'J':-6,'Z':-6,'X':-6,'*':1},
}
#================================================================================================================
NEGATIVE_INFINITY = -10000000000
MATCH_SCORE = 2
MISMATCH_SCORE = -1
#================================================================================================================
class GlobalAlignment:
    def __init__(self,s1,s2,gap_opening,gap_extension,is_protein):
        self.r = len(s2)
        self.c = len(s1)
        self.s1 = s1
        self.s2 = s2
        self.gap_opening = gap_opening
        self.gap_extension = gap_extension
        self.is_protein = is_protein
        self.MMatrix = [[0 for x in range(self.c+1)] for y in range(self.r+1)]
        self.IxMatrix = [[0 for x in range(self.c+1)] for y in range(self.r+1)]
        self.IyMatrix = [[0 for x in range(self.c+1)] for y in range(self.r+1)]
        self.all_alignments = []
    
    def initialize_matrices(self):
        #===================Initialize self.MMatrix===================
        self.MMatrix[0][0] = 0
        for i in range(1,self.r+1):
            self.MMatrix[i][0] = NEGATIVE_INFINITY
        for j in range(1,self.c+1):
            self.MMatrix[0][j] = NEGATIVE_INFINITY
        #=============================================================
        #===================Initialize self.IxMatrix==================
        for j in range(self.c+1):
            self.IxMatrix[0][j] = NEGATIVE_INFINITY
        for i in range(self.r+1):
            self.IxMatrix[i][0] = self.gap_opening + self.gap_extension*i
        #=============================================================
        #===================Initialize self.IyMatrix==================
        for i in range(self.r+1):
            self.IyMatrix[i][0] = NEGATIVE_INFINITY
        for j in range(self.c+1):
            self.IyMatrix[0][j] = self.gap_opening + self.gap_extension*j
        #=============================================================
    
    def score_of(self,c1,c2):
        if self.is_protein == False:
            if c1==c2:
                return MATCH_SCORE
            else:
                return MISMATCH_SCORE
        else:
            return BLOSUM80[c1][c2]

    def fill_matrices(self):
        for i in range(1,self.r+1):
            for j in range(1,self.c+1):
                s1_char = self.s1[j-1]
                s2_char = self.s2[i-1]
                score = self.score_of(s1_char,s2_char)
                self.MMatrix[i][j] = max(self.MMatrix[i-1][j-1],self.IxMatrix[i-1][j-1],self.IyMatrix[i-1][j-1])+score
                self.IxMatrix[i][j] = max(self.MMatrix[i-1][j]+self.gap_opening+self.gap_extension,self.IxMatrix[i-1][j]+self.gap_extension)
                self.IyMatrix[i][j] = max(self.MMatrix[i][j-1]+self.gap_opening+self.gap_extension,self.IyMatrix[i][j-1]+self.gap_extension)
        self.final_score = max(self.MMatrix[self.r][self.c],self.IxMatrix[self.r][self.c],self.IyMatrix[self.r][self.c])
    
    def print_matrix(self,matrix,r,c):
        for i in range(r):
            for j in range(c):
                print( '%-20i' %matrix[i][j] ,end="")
            print()

    def print_matrices(self):
        #===================== Print Matrices====================================
        print("MMatrix")
        self.print_matrix(self.MMatrix, self.r+1, self.c+1)
        print("=======================================================================================")
        print("IxMatrix")
        self.print_matrix(self.IxMatrix, self.r+1, self.c+1)
        print("=======================================================================================")
        print("IyMatrix")
        self.print_matrix(self.IyMatrix, self.r+1, self.c+1)
        print("=======================================================================================")
    
    def run_alignment(self):
        self.initialize_matrices()
        self.fill_matrices()
        self.print_matrices()
        self.traceback(self.r,self.c,"","","")

    def traceback(self,i,j,s1path,s2path,align):
        if i==0 and j==0:
            s1path = s1path[::-1]
            s2path = s2path[::-1]
            align = align[::-1]
            #print(s1path)
            #print(align)
            #print(s2path)
            self.all_alignments.append([s1path,align,s2path])
        
        else:
            if i==0 and j>0:
                char1 = self.s1[j-1]
                s1path+=char1
                s2path+='-'
                align+=" "
                self.traceback(i,j-1,s1path,s2path,align)
            
            elif i>0 and j==0:
                char2=self.s2[i-1]
                s1path+='-'
                s2path+=char2
                align+=" "
                self.traceback(i-1,j,s1path,s2path,align)
            else:
                char1=self.s1[j-1]
                char2=self.s2[i-1]
                score = self.score_of(char1,char2)
                max_value = max(self.MMatrix[i][j],self.IxMatrix[i][j],self.IyMatrix[i][j])
                if(max_value == self.MMatrix[i][j]):
                    if max_value==self.IxMatrix[i][j]:
                        x_s1path = s1path
                        x_s2path = s2path
                        x_align = align
                        s1path+=char1
                        s2path+=char2
                        if(char1==char2):
                            align+="|"
                        else:
                            align+=" "
                        x_s1path+='-'
                        x_s2path+=char2
                        x_align+=" "
                        self.MMatrix[i-1][j]+=self.gap_extension+self.gap_opening
                        self.IxMatrix[i-1][j]+=self.gap_extension
                        self.MMatrix[i-1][j-1]+=score
                        self.IxMatrix[i-1][j-1]+=score
                        self.IyMatrix[i-1][j-1]+=score
                        self.traceback(i-1,j-1,s1path,s2path,align)
                        self.traceback(i-1,j,x_s1path,x_s2path,x_align)
                    elif(max_value==self.IyMatrix[i][j]):
                        y_s1path = s1path
                        y_s2path = s2path
                        y_align = align
                        s1path+=char1
                        s2path+=char2
                        if(char1==char2):
                            align+="|"
                        else:
                            align+=" "
                        y_s1path+=char1
                        y_s2path+="-"
                        y_align+=" "
                        self.MMatrix[i][j-1]+=self.gap_extension+self.gap_opening
                        self.IyMatrix[i][j-1]+=self.gap_extension
                        self.MMatrix[i-1][j-1]+=score
                        self.IxMatrix[i-1][j-1]+=score
                        self.IyMatrix[i-1][j-1]+=score
                        self.traceback(i-1,j-1,s1path,s2path,align)
                        self.traceback(i,j-1,y_s1path,y_s2path,y_align)
                    else:
                        s1path+=char1
                        s2path+=char2
                        if(char1==char2):
                            align+="|"
                        else:
                            align+=" "
                        self.MMatrix[i-1][j-1]+=score
                        self.IxMatrix[i-1][j-1]+=score
                        self.IyMatrix[i-1][j-1]+=score
                        self.traceback(i-1,j-1,s1path,s2path,align)
                elif(max_value == self.IxMatrix[i][j]):
                    if max_value==self.IyMatrix[i][j]:
                        y_s1path = s1path
                        y_s2path = s2path
                        y_align = align
                        y_s1path+=char1
                        y_s2path+="-"
                        y_align+=" "
                    s1path+='-'
                    s2path+=char2
                    align+=" "
                    if(max_value==self.IyMatrix):
                        self.MMatrix[i][j-1]+=self.gap_extension+self.gap_opening
                        self.IyMatrix[i][j-1]+=self.gap_extension
                    self.MMatrix[i-1][j]+=self.gap_extension+self.gap_opening
                    self.IxMatrix[i-1][j]+=self.gap_extension
                    self.traceback(i-1,j,s1path,s2path,align)
                    if(max_value==self.IyMatrix[i][j]):
                        self.traceback(i,j-1,y_s1path,y_s2path,y_align)
                elif(max_value==self.IyMatrix[i][j]):
                    s1path+=char1
                    s2path+="-"
                    align+=" "
                    self.MMatrix[i][j-1]+=self.gap_extension+self.gap_opening
                    self.IyMatrix[i][j-1]+=self.gap_extension
                    self.traceback(i,j-1,s1path,s2path,align)


#alignment = GlobalAlignment("ACACT","AAT",-3,-1,False)
#alignment.run_alignment()
#print("Final Score : ",alignment.final_score)