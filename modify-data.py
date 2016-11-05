already = []
Wcount = 0
Scount = 1
arr = []


def BIO_Tag(templine, already):
    pipe_sep = templine[5].split('|')
    chunk = pipe_sep[7].split('-')
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
    pipe_sep[7] = temp
    temp_append = pipe_sep[0]
    for i in range(1, 11):
        temp_append += '|' + pipe_sep[i]
    templine[5] = temp_append


def add_parent_name(arr):
    for i in range(0, Wcount):
        temp = arr[i][7]
        if temp == '0':
            arr[i][7] = 'root'
        else:
            for j in range(0, Wcount):
                temp2 = arr[j][1]
                if temp2 == temp:
                    arr[i][7] = arr[j][2]


with open('hdtb_development_wx.conll') as f:
    for line in f:
        if line in ['\n', '\r\n']:  # Blank Line
            add_parent_name(arr)
            for i in range(0, Wcount):
                print(arr[i])
            print('\n')
            already = []
            Wcount = 0
            Scount += 1
            arr = []
        else:  # Normal Line
            templine = line.split('\t')
            BIO_Tag(templine, already)
            templine = [str(Scount)] + templine
            arr.append(templine)
            Wcount += 1
