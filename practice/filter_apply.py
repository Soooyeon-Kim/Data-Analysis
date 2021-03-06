import numpy as np
import pandas as pd

df = pd.DataFrame({
    'key': ['A', 'B', 'C', 'A', 'B', 'C'],
    'data1': [0, 1, 2, 3, 4, 5],
    'data2': [4, 4, 6, 0, 6, 1]
})
print("DataFrame:")
print(df, "\n")

# groupby()로 묶은 데이터에 filter 적용
# key별 data2의 평균이 3이 넘는 인덱스만 출력
def filter_by(x):
    return x['data2'].mean() > 3
print("filtering : ")
print(df.groupby('key').filter(filter_by))



# groupby()로 묶은 데이터에 apply 적용
# 람다식을 이용해 최댓값에서 최솟값을 뺀 값을 적용

print("applying : ")
print(df.groupby('key').apply(lambda x : x.max() - x.min()))
