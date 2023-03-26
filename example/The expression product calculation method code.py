
import pandas as pd
import numpy as np


a1 = pd.read_csv("The_expression_product_data.csv", header=None, index_col=None).to_numpy()  
b1 = pd.read_csv("LRI.csv", header=None, index_col=None).to_numpy()  # LRI obtained after filtering


for w in range(0, b1.shape[0]): 
    zhibiao1 = 0
    zhibiao2 = 0
    flag = False
    for x in range(0, a1.shape[0]): 
        if b1[w][0] == a1[x][0]:
            b11 = a1[x] 
            zhibiao1 = 1
        if b1[w][1] == a1[x][0]:
            b12 = a1[x]  
            zhibiao2 = 1
        if zhibiao1 == 1 and zhibiao2 == 1:  
            flag = True
            break
    if not flag:
        continue
    b11 = np.delete(b11, 0)  
    b12 = np.delete(b12, 0)  
    for i in range(0, 7):
        for j in range(0, 7):
            Cheng = b11[i] * b12[j]
            with open(r"melanoma\expression_product\\" + str(i) + str(j) + ".csv", mode="a") as f:
                f.write(str(Cheng))
                f.write('\n')
            f.close()

print('------------------------------------------------------------')

for i in range(0, 7):
    for j in range(0, 7):
        a1 = pd.read_csv(r"melanoma\expression_product\\" + str(i) + str(j) + ".csv", header=None, index_col=None).to_numpy()  # Obtain the result
        SUM = a1.sum()
        with open(r"melanoma\expression_product\\result.csv", mode="a") as f:
            f.write(str(i))
            f.write(str(j))
            f.write('____')
            f.write(str(SUM))
            f.write('\n')
        f.close()
print('------------------End of calculation---------------------------')
