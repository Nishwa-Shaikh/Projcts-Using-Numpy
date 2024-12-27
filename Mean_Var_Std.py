import numpy as np
class mean_var_std:
    @staticmethod
    def calculate(Array):
        if len(Array)!=9:
            raise ValueError("List must contain 9 digits")
        matrix=np.array(Array).reshape(3,3)

        result={'Mean':[list(np.mean(matrix, axis=0)),
                        list(np.mean(matrix, axis=1)),
                        np.mean(matrix)],
                'Variance':[list(np.var(matrix, axis=0)),
                            list(np.var(matrix, axis=1)),
                            np.var(matrix)],
                'Standard Deviation':[list(np.std(matrix, axis=0)),
                                      list(np.std(matrix, axis=1)),
                                      np.std(matrix)],
                'Max':[list(np.max(matrix, axis=0)),
                       list(np.max(matrix, axis=1)),
                       np.max(matrix)],
                'Min':[list(np.min(matrix, axis=0)),
                       list(np.min(matrix, axis=1)),
                       np.min(matrix)],
                'Sum':[list(np.sum(matrix, axis=0)),
                       list(np.sum(matrix, axis=1)),
                       np.sum(matrix)]}
        return result
    
SUM=mean_var_std
print(SUM.calculate([1,2,3,4,5,6,7,8,9]))
