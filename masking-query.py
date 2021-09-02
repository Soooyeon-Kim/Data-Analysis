import numpy as np
import pandas as pd

print("Masking & query")
df = pd.DataFrame(np.random.rand(5, 2), columns=["A", "B"])
#print(df, "\n")

# A컬럼값이 0.5보다 작고 B컬럼 값이 0.3보다 큰값 출력


# 마스킹 연산 활용
print(df[(df['A']<0.5)&(df['B']>0.3)])

# query 함수 활용
print(df.query("A<0.5 and B>0.3"))


