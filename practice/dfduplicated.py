df.duplicated(['col'], keep='first') # 처음 발견 중복 값 제외 나머지 삭제

df.duplicated(['col'], keep='last') # 마지막 발견 중복값 제외 나머지 삭제

df.duplicated(['col'], keep=False) # 모든 중복데이터 삭제

df.duplicated(['colA', 'colB']) # 중복된 값이 없다면 => 모든 행 False

df.duplicated(['colA', 'colB']) # 중복된 값이 있는 행 존재 => True값 출력

df.drop_duplicates(['colA', 'colB']) # 중복된 값이 있는 행 삭제
