'''
num을 제곱한 값을 리턴
'''
def _square(num):
    return num * num

# _square()와 동일한 기능을 하는 lambda 함수 square
square = lambda num : num * num

'''
string이 빈 문자열일 경우 빈 문자열을, 아니면 첫 번째 글자를 리턴
'''
def _first_letter(string):
    return string[0] if string else ''

first_letter = lambda string : string[0] if string else ''
