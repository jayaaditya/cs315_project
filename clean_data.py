import csv 
file_list = ["Y20%02d-%02d.csv" %(i,i+1) for i in range(6,18)]
file_list.append('data_dump.csv')

file_list_out = map(lambda x: x+'_new', file_list)

for i in range(len(file_list)):
    fi = open(file_list[i], 'r')
    fo = open(file_list_out[i], 'w')
    csv_reader = csv.reader(fi)
    csv_writer = csv.writer(fo)
    for x in csv_reader:
        x_new = map(lambda a: a.strip(), x)
        csv_writer.writerow(x_new)
    fi.close()
    fo.close()

