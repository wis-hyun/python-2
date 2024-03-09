import csv

result = []
with open('d:/secondpython/2회고사/score.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f)
    for line in reader:
        datamax= max(map(int, line[1].split(',')))
        line.append(datamax)
        result.append(line)

with open('score_result.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
