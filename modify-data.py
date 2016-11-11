from __future__ import print_function
import mysql.connector

already = []
Wcount = 0
Scount = 1
arr = []

cnx = mysql.connector.connect(user='root', password='gotham', host='localhost', database='test_cl')
cursor = cnx.cursor()
print("Connected!")


def dump(arr):
    add_data = (
        "INSERT INTO hdtb (Sid, Wid, form, lemma, cpos, pos, category, gender, number, person, cas, vibh, tam, chunkid, chunktype, stype, voicetype, parent, drel)"
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    )
    arr.remove(arr[19])
    arr.remove(arr[19])
    data_test = tuple(arr)
    cursor.execute(add_data, data_test, False)
    cnx.commit()


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


def final_form_arr(arr):
    temp1 = arr[7]
    temp2 = arr[8]
    temp3 = arr[9]
    temp4 = arr[10]
    features_array = arr[6]
    features_split = features_array.split('|')
    num_features = len(features_split)
    index = 6
    for j in range(0, num_features):
        put = features_split[j].split('-')
        final = put[1]
        if final == '':
            final = '-'
        if index > 10:
            arr.insert(index, final)
        else:
            arr[index] = final
        index += 1
    arr.insert(index, temp1)
    index += 1
    arr.insert(index, temp2)
    index += 1
    arr.insert(index, temp3)
    index += 1
    arr.insert(index, temp4)


with open('test.txt') as f:
    for line in f:
        if line in ['\n', '\r\n']:  # Blank Line
            #add_parent_name(arr)
            for i in range(0, Wcount):
                final_form_arr(arr[i])
                dump(arr[i])
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

cursor.close()
cnx.close()
