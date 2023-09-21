class SparseMatrix:
    """Initiating SparseMatrix Class"""
    def __init__(self):
        self.matrix={}
        """Initiating empty sparse matrix"""
    
    def set(self,row,col,value):
        self.matrix[(row,col)]=value
        """sets value at row,col"""
    
    def get(self,row,col):
        return self.matrix.get((row,col),0)
        """retrieves value from row,col"""

    def recommend(self,vector):
        recommendations={}
        for (row,col),value in self.matrix.items():
            if col not in recommendations:
                recommendations[col]=0
            recommendations[col]+=value*vector[row]
        return recommendations
    """multiplies input vector wih sparse matrix and gives recommendation vector"""
    
    def add_movie(self,matrix):
        newmat=SparseMatrix()
        newmat.matrix=self.matrix.copy()
        for(row,col),value in  matrix.matrix.items():
           newmat.matrix[(row,col)]=value
        return newmat
    """adds another sparse matrix to the current sparse matrix and returns a new sparse matrix"""
    def to_dense(self):
        if not self.matrix:
             return[]
        maxrow=max(row for row,_ in self.matrix.keys())+1
        maxcolumn=max(column for column in self.matrix.keys())+1
        densemat=[[0]* maxcolumn for _ in range(maxrow)]
        for (row,col),value in self.matrix.items():
            densemat[row][col]=value 
        return densemat
    """converts sparse matrix to dense matrix."""


