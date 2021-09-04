# 트럼프 대통령 트윗을 공백 기준으로 분리한 리스트
trump_tweets = ['america', 'is', 'back', 'and', 'we', 'are', 'coming', 'back', 'bigger', 'and', 'better', 'and', 'stronger', 'than', 'ever', 'before']

def make_new_list(text):
    new_list = []
    for word in text:
        if word[0] == 'b':
      # if word.startswith('b'):
            new_list.append(word)
    
    return new_list



new_list = make_new_list(trump_tweets)
print(new_list)