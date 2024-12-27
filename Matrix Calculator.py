import numpy as np

class Matrix:
    def __init__(self, Mat1=None, Mat2=None):
        self.Mat1=np.array(Mat1) if Mat1 is not None else None
        self.Mat2=np.array(Mat2) if Mat2 is not None else None

    def addition(self):
        if np.shape(self.Mat1)==np.shape(self.Mat2):
            result=self.Mat1+self.Mat2
            print(result)
        else:
            print("Dimensions should be same")
    
    def subtraction(self):
        if self.Mat1.shape==self.Mat2.shape:
            result=self.Mat1-self.Mat2
            print(result)
        else:
            print("Dimensions should be same")
    
    def Mult(self):
        if self.Mat1.ndim==self.Mat2.ndim and self.Mat1.shape[1]==self.Mat2.shape[0]:
            result=self.Mat1@self.Mat2
            print(result)
        else:
            print("Dimensions should be same")
    
    def inverse(self):
        if self.Mat1 is not None and self.Mat1.shape[0]==self.Mat1.shape[1] and self.Mat1.ndim==2:
            if np.linalg.det(self.Mat1)!=0:
                result=np.linalg.inv(self.Mat1)
                print(f"Inverse is: {result}")
            else:
                print('Singular matrix is not allowed')
        else:
            print('Matrix must be square')
    
    def Transpose(self):
        if self.Mat1 is not None:
            result=self.Mat1.transpose()
            print(result)
        else:
            print("Matrix should not be empty")

    def determinant(self):
        if self.Mat1 is not None and self.Mat1.shape[0] == self.Mat1.shape[1]:
            result = np.linalg.det(self.Mat1)
            print(f"Determinant is: {result}")
        else:
            print("Matrix must be square")
