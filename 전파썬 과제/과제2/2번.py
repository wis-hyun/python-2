import csv
import statistics

#r모드로 파일을 불러와 읽음
with open('D:/python/population_seoul.csv','r', encoding='euc-kr') as f:
    reader = csv.reader(f)
     
#3번째 줄부터 자료 읽음
    next(reader)
    next(reader)
    
#총생활인구 수의 값을 가지고 옴    
    data=[]
    for line in reader:
        data += list(map(float, line[3:4]))
        
#max, min함수로 최댓값, 최솟값 구함
    print('최댓값 : ', max(data))
    print('최솟값 :', min(data))
    
#statistics에 있는 mean, variance함수로 평균과 분산을 구함
    print('평균 :', statistics.mean(data))
    print('분산 :', statistics.variance(data))

