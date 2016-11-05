already = []
Wcount = 0
arr = []


def BIO_Tag(templine, already):
    pipe_sep = templine[5].split('|')
    chunk = pipe_sep[7].split('-')
    # print(chunk)
    if chunk[1] not in already:
        already.append(chunk[1])
        temp = chunk[1]
        temp += '_B'
        chunk[1] = temp
    else:
        temp = chunk[1]
        temp += '_I'
        chunk[1] = temp
    temp = chunk[0] + '-' + chunk[1]
    # print(temp)
    pipe_sep[7] = temp
    temp_append = pipe_sep[0]
    for i in range(1, 11):
        temp_append += '|' + pipe_sep[i]
    templine[5] = temp_append


def add_parent_name(arr):
    for i in range(0, Wcount):
        temp = arr[i][6]
        if temp == '0':
            arr[i][6]='root'
        else:
            for j in range(0, Wcount):
                temp2 = arr[j][0]
                if temp2 == temp:
                    arr[i][6] = arr[j][1]


with open('hdtb_development_wx.conll') as f:
    for line in f:
        if line in ['\n', '\r\n']:  # Blank Line
            add_parent_name(arr)
            for i in range(0, Wcount):
                print(arr[i])
            print('\n')
            # print("BLANK LINE\n")
            already = []
            Wcount = 0
            arr = []
        else:  # Normal Line
            # print(line)
            templine = line.split('\t')
            # print(templine)
            BIO_Tag(templine, already)
            # print(templine)
            arr.append(templine)
            Wcount += 1
            # print("LINE ENDS\n")
