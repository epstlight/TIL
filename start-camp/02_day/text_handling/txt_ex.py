with open('ssafy.txt', 'r') as f :
    lines = f.readlines()


with open('reversed_ssafy.txt', 'w') as f :
    # lines.reverse()
    f.writelines(reversed(lines))

