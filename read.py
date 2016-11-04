# count = 0
already=[]
with open('hdtb_development_wx.conll') as f:
    for line in f:
        # if count is 5:
        #     break
        if line in ['\n', '\r\n']:
            print("BLANK LINE\n")
            # count += 1
            already = []
        else:
            print("LINE")
            print(line)
            # count += 1
            arr = line.split('\t')
            # print(arr[5])
            pipe_sep = arr[5].split('|')
            # print(pipe_sep)
            chunk = pipe_sep[7].split('-')
            print(chunk)

            if chunk[1] not in already:
                already.append(chunk[1])
                temp = chunk[1]
                temp += '_B'
                # print(temp)
                chunk[1] = temp
                # print(chunk)
            else:
                temp = chunk[1]
                temp += '_I'
                # print(temp)
                chunk[1] = temp
                # print(chunk)
            temp = chunk[0] + '-' + chunk[1]
            print(temp)
            pipe_sep[7] = temp
            print(pipe_sep)
            print("LINE ENDS\n")
