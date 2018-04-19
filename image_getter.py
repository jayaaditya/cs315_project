from main.models import *
import requests

file_path = "./static/photos/"

def get():
    get_url = "https://oa.cc.iitk.ac.in/Oa/Jsp/Photo/%s_0.jpg"
    students = student.objects.all().order_by('rollno')
    for x in students:
        print x.rollno
        new_file = file_path + x.rollno + ".jpg"
        r = requests.get(get_url %x.rollno)
        with open(new_file, 'wb') as f:
            f.write(r.content)
