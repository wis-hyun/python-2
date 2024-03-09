#파일을 읽어와 공백을 기준으로 나누어 저장
with open("D:/python/python_guide.txt",'r') as f:
    data=f.read().split()
    
#빈 딕셔너리 생성
word_count={}

#리스트에있는 단어들을 하나씩 실행
#딕셔너리에 있는 단어면 1을 증가시켜줌 아니라면 1
for word in data:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

#딕셔너리를 출력
print(word_count)

