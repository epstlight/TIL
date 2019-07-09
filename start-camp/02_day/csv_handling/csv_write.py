dinner = {
    '양자강' : '02-557-4211',
    '김밥카페' : '02-553-3181',
    '순남시레기' : '02-508-0887',
}

# 1. String formatting
with open('dinner.csv', 'w', encoding='utf-8') as f :
    f.write('음식점,전화번호\n')
    for item in dinner.items() : 
        f.write(f'{item[0]},{item[1]}\n')

# 2. csv writer
import csv
with open('dinner.csv', 'w', encoding='utf-8', newline='') as f :  # newline자리에 아무것도 x, 옵션을 넣을 때는 = 양옆에 붙여서 작성 
    f.write('음식점,전화번호\n')
    csv_writer = csv.writer(f) #f라는 파일에 csv를 작성하는 객체를 생성
    for item in dinner.items() :
        csv_writer.writerow(item)
