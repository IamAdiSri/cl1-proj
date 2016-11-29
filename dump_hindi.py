from __future__ import print_function
import mysql.connector as connector

already = []
Wcount = 0
Scount = 15895
arr = []

cnx = connector.connect(user='root', password='gotham', host='localhost', database='test_cl')
cursor = cnx.cursor()
print("Connected!")


def dump(array):
    add_data = (
        "INSERT INTO hdtb (Sid, Wid, form, lemma, cpos, pos, category, gender, number, person, cas, vibh, tam, chunkid, chunktype, stype, voicetype, parent, drel)"
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    )
    array.remove(array[19])
    array.remove(array[19])
    data_test = tuple(array)
    cursor.execute(add_data, data_test, False)
    cnx.commit()


def stringify(array):
    for j in range(0, 19):
        array[j] = str(array[j])


def BIO_Tag(tline, already_words):
    pipe_sep = tline[5].split('|')
    chunk = pipe_sep[7].split('-')
    if chunk[1] not in already_words:
        already_words.append(chunk[1])
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
    for q in range(1, 11):
        temp_append += '|' + pipe_sep[q]
    tline[5] = temp_append


def add_parent_name(array):
    for q in range(0, Wcount):
        temp = array[q][7]
        if temp == '0':
            array[q][7] = 'root'
        else:
            for j in range(0, Wcount):
                temp2 = array[j][1]
                if temp2 == temp:
                    array[q][7] = array[j][2]


def final_form_arr(array):
    temp1 = array[7]
    temp2 = array[8]
    temp3 = array[9]
    temp4 = array[10]
    features_array = array[6]
    features_split = features_array.split('|')
    num_features = len(features_split)
    index = 6
    for j in range(0, num_features):
        put = features_split[j].split('-')
        final = put[1]
        if final == '':
            final = '-'
        if index > 10:
            array.insert(index, final)
        else:
            array[index] = final
        index += 1
    array.insert(index, temp1)
    index += 1
    array.insert(index, temp2)
    index += 1
    array.insert(index, temp3)
    index += 1
    array.insert(index, temp4)


with open('hdtb_development_wx.conll') as f:
    for line in f:
        if line in ['\n', '\r\n']:  # Blank Line
            # add_parent_name(arr)
            for i in range(0, Wcount):
                final_form_arr(arr[i])
                stringify(arr[i])
                dump(arr[i])
            # for i in range(0, Wcount):
            #     print(arr[i])
            # print('\n')
            already = []
            Wcount = 0
            print(Scount)
            # print('\n')
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
