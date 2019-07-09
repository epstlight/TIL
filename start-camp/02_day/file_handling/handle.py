import os

os.chdir(r'C:\Users\student\TIL\start-camp\02_day\file_handling')  #change dir r은 이스케이프 문자(\)를 막음
filenames = os.listdir('.')

for filename in filenames :     # .txt 확장자만 파일 명을 바꾼다. 
    if '.txt' == os.path.splitext(filename)[-1] :  #확장자만 따로 분리 
        os.rename(filename, filename.replace('samsung', 'ssafy')) #첫번째 인자로 넘어간 이름을 두번째 인자로 넘어간 이름으로 바꾼다.  

filenames = os.listdir('.')
print(filenames) 