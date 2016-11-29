from __future__ import print_function
import mysql.connector as connector

already = []
Wcount = 1
Scount = 1
arr = []

cnx = connector.connect(user='root', password='gotham', host='localhost', database='test_cl',
                        charset='utf8mb4', collation='utf8mb4_general_ci')
cursor = cnx.cursor()
print("Connected!")


def dump(array):
    add_data = (
        "INSERT INTO udtb1 (Sid, parent, category, gender, number, person, cas, tam, vibh, chunkid, stype, voicetype, pos, cpos, Wid, form, lemma)"
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    )
    data_test = tuple(array)
    cursor.execute(add_data, data_test, False)
    cnx.commit()


def stringify(array):
    for j in range(0, 19):
        array[j] = str(array[j])


def BIO_Tag(tline, already_words):
    pipe_sep = tline[1].split('|')
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
    for q in range(1, 10):
        temp_append += '|' + pipe_sep[q]
    tline[1] = temp_append


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
    temp1 = array[3]
    temp2 = array[4]
    temp3 = array[5]
    temp4 = array[6]
    temp5 = array[7]
    features_array = array[2]
    features_split = features_array.split('|')
    # print(features_split)
    num_features = len(features_split)
    index = 2
    flag = 0
    for j in range(0, num_features):
        put = features_split[j].split('-')
        final = put[1]
        if final == '':
            final = '-'
        if j is 6:
            if final == '0':
                flag = 1
        if index > 7:
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
    index += 1
    array.insert(index, temp5)
    if flag is 1:
        array[7], array[8] = array[8], array[7]
        # print(array[7], array[8])


with open('Urdu_data/sample_urdu') as f:
    for line in f:
        if line in ['\n', '\r\n']:  # Blank Line
            # add_parent_name(arr)
            # print('Blank Line with Wcount',Wcount)
            # for i in range(0, Wcount):
            #     final_form_arr(arr[i])
            #     stringify(arr[i])
            # dump(arr[i])
            # for i in range(0, Wcount):
            #     print(arr[i])
            # print('\n')
            already = []
            Wcount = 1
            # print(Scount)
            # print('\n')
            Scount += 1
            arr = []
        else:  # Normal Line
            # print(line)
            templineorig = line.split('\t')
            templineorig.reverse()
            templineorig.remove(templineorig[0])
            templineorig.remove(templineorig[0])
            templine = []
            templine.insert(0, Wcount)
            a = templineorig[6]
            templine.insert(0, a)
            a = templineorig[5]
            templine.insert(0, a)
            a = templineorig[4]
            templine.insert(0, a)
            a = templineorig[3]
            templine.insert(0, a)
            a = templineorig[2]
            templine.insert(0, a)
            a = templineorig[1]
            templine.insert(0, a)
            # print(templineorig)
            # print(templine)
            BIO_Tag(templine, already)
            # print(templine)
            templine = [str(Scount)] + templine
            # print(templine)
            final_form_arr(templine)
            print(templine)
            dump(templine)
            # arr.append(templine)
            # print(arr)
            Wcount += 1

cursor.close()
cnx.close()
