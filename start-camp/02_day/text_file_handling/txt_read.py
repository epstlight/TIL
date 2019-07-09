with open('with_ssafy.txt', 'r') as f :
    # print(f.read())    # f.read() all text 전체를 불러온다 개행문자 포함
    # print(f.readline())    #한줄을 불러온다. 
    lines = f.readlines()    #전체를 리스트로 불러온다. 
    for line in lines :
        print(line.strip())   #개행 문자 제거 (이미 개행문자가 포함된 리스트임)

        

 
