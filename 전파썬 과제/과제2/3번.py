import csv

#r모드로 파일을 읽어옴
with open('D:/python/population_seoul.csv','r', encoding='euc-kr') as f:
    reader = csv.reader(f)
    
#1번째 줄 건너뛰고부터 읽음
    next(reader)
    
#리스트에다가 읽어온 부분 추가
    data=[]
    for line in reader:
        data.append(line)
        
#총인구수를 기준으로 내림차순하여 정렬
sorted_dates = sorted(data, key=lambda x:float(x[3]), reverse=True)

#w모드로 새로 써줌
with open('D:/python/population_seoul_result.csv','w', newline='', encoding='euc-kr') as f:
    writer=csv.writer(f)
    
#1번째 줄 헤드라이너 작성
    writer.writerow(['기준일ID','시군구코드','시군구명','총생활인구수','내국인생활인구수','장기체류외국인인구수','단기체류외국인인구수','일최대인구수','일최소인구수','주간인구수(09~18)','야간인구수(19~08)','일최대이동인구수','서울외유입인구수','동일자치구행정동간이동인구수','자치구간이동인구수'
])
    
# 내림차순으로 정렬한 데이터를 하나씩 써내려감   
    for row in sorted_dates:
        writer.writerow(row)
print(sorted_dates)


