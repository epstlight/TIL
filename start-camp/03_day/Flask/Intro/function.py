def sum(num1,num2) :
    return num1 + num2

def diff(num1, num2) :
    if num1 > num2 :
        return num1 - num2

    else : 
        return num2 - num1 

def main() :
    num1 = int(input('number 1:'))
    num2 = int(input('number 2:'))

    print('더하기 : %d' % sum(num1, num2))
    print('빼기 : %d' % diff(num1, num2))

if __name__ == "__main__":
    main()