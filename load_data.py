import csv
from main.models import *

file_list = ["Y20%02d-%02d.csv_new" %(i,i+1) for i in range(6,18)]

def load_dept_codes(sample_file = file_list[-1]):
    rows = []
    with open(sample_file, 'r') as f:
        csv_file = csv.reader(f)
        for x in csv_file:
            rows.append(x)
    rows.pop(0)
    for x in rows:
        x = map(lambda a: a.strip(), x)
        try:
            temp = department(code = x[4].strip())
            temp.save()
        except:
            print x[4], "already added"
            pass

def load_courses():
    unadded = []
    for x in file_list:
        file_data = []
        unadded = []
        print x
        with open(x, 'r') as f:
            csv_file = csv.reader(f)
            for i in csv_file:
                file_data.append(i)
        file_data.pop(0)
        for i in file_data:
            try:
                temp = course.objects.get(code = i[2].strip())
                print i[2],"already added"
            except:
                print i
                print i[4].split(' ')
                try:
                    temp = course.objects.create(code = i[2].strip(),
                            dept = department.objects.get(code = i[4].strip()),
                            title = i[3].strip())
                    print i[2],"Added!"
                except:
                    pass
    print unadded

def load_stud_course(read_from = 0):
    unadded = []
    f1 = open('./data_dump.csv_new', 'r')
    csv_reader = csv.reader(f1)
    counter = 0
    for x in csv_reader:
        counter += 1
        if counter < read_from:
            continue
        try:
            stud = student.objects.get(rollno = x[1])
            print "student already added"
        except:
            print "adding student", x[1], x[2], x[3], x[4]
            try:
                stud = student.objects.create(rollno = x[1].strip(), 
                        dept = department.objects.get(code = x[3].strip()),
                        program = x[4].strip(),
                        name = x[2].strip()
                        )
                print "added student", x[1], x[2], x[3], x[4]
            except:
                pass
        print counter
        try:
            course_taken = course.objects.get(code = x[6].strip())
        except:
            unadded.append(counter)
            continue
        try:
            enrolled_entry = enrolled.objects.create(rollno = stud, 
                ccode = course_taken, 
                acad_year = x[7].strip(), 
                semester = x[8].strip(), 
                instructor = x[9].strip()
                )
        except:
            pass
        print "Course enrolled added", x
    f1.close()
    return unadded

def dept_all():
    for x in file_list:
        load_dept_codes(x)
