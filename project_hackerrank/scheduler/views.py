from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random as rn
from itertools import permutations, combinations
import csv


def class_(request):

    if request.method=='GET':
        all_class = Class.objects.all()
        return render(request, 'show_class.html', {'all_class': all_class})
    
    else:
        data = dict(request.POST)
        print(data)
        subjects = data['subjects'][0].split(',')
        
        if len(subjects)!=5:
            all_class = Class.objects.all().order_by('class_num')
            return render(request, 'show_class.html', {'all_class': all_class, 'error': 'enter 5 subjects separated by comma "," '})
        sections = int(data['sections'][0])
        
        if sections>3:
            all_class = Class.objects.all().order_by('class_num')
            return render(request, 'show_class.html', {'all_class': all_class, 'error': 'enter maximum 3 sections'})
        
        subjects = ', '.join([x.strip().capitalize() for x in subjects])
        
        Class(class_num=int(data['class_number'][0]), strength=int(data['strength'][0]), sections=sections, subjects=subjects).save()
        all_class = Class.objects.all().order_by('class_num')
        
        return render(request, 'show_class.html', {'all_class': all_class})



def class_id(request, id):
    if request.method=='GET':
        try:
            class_data = Class.objects.get(class_num=int(id))
        except:
            return HttpResponse(f"Class id {id} does not exist")
        return render(request, 'show_class.html', {'class_data': class_data})
    
    else:
        Class.objects.filter(class_num=id).delete()
        print(f'class {id} deleted')
        return HttpResponse(f"Class Number {id} deleted!")


def teacher(request):
    if request.method=="GET":
        all_teachers = Teacher.objects.all().order_by('class_num')
        return render(request, 'show_teachers.html', {'all_teachers': all_teachers})
    else:
        data = dict(request.POST)
        print(data)
        Teacher(class_num=int(data['class_number'][0]), name=data['name'][0].strip().capitalize(), subject=data['subject'][0].strip().capitalize(), id=rn.randint(100,99999)).save()
        all_teachers = Teacher.objects.all().order_by('class_num')
        return render(request, 'show_teachers.html', {'all_teachers': all_teachers})


def teacher_id(request, id):
    if request.method=='GET':
        try:
            teacher_data = Teacher.objects.get(id=int(id))
        except:
            return HttpResponse(f"Teacher id {id} does not exist")
        return render(request, 'show_teachers.html', {'teacher_data': teacher_data})
    else:
        Teacher.objects.filter(id=id).delete()
        print(f'Teacher {id} deleted')
        return HttpResponse(f"Teacher id {id} deleted!")



def generate(request):
    schedule = get_schedule()
    #print(schedule)
    schedule_ = []
    
    for cls, _ in schedule:
        sec_num = len(cls[0])
        cls_ = []
        
        for sec in range(sec_num):
            table = []
           
            for day in range(5):
                table.append(cls[day][sec])
            cls_.append(table) 
        schedule_.append(cls_)
    
    class_nums = [x[1] for x in schedule]
    del schedule
    #print(*schedule_, sep='\n\n')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=schedule.csv'
    writer=csv.writer(response)
    sections = ['A', 'B', 'C']
    days = ["Mon", 'Tue', 'Wed', 'Thu', 'Fri']
    
    for i in range(len(schedule_)):
        tables = schedule_[i]
        sec_num = len(tables)
        
        for section in range(sec_num):
            writer.writerow(['Class Number', 'Section', 'Day',' ', '1st - Sub.', '2nd - Sub.', '3rd - Sub.', '4th - Sub.', '5th - Sub.'])
            sec = tables[section]
        
            for day in range(5):
                writer.writerow([class_nums[i], sections[section], days[day],' ', sec[day][0] , sec[day][1], sec[day][2], sec[day][3], sec[day][4]])
            writer.writerow(['']*9)
        writer.writerow(['Teachers', 'ID', 'Name', 'Subject'])
        
        for x in Teacher.objects.all():
            if x.class_num == class_nums[i]:
                writer.writerow([' ',x.id, x.name, x.subject])
        writer.writerow(['']*9)
        writer.writerow(['']*9)
    
    return(response)


def get_schedule():
    all_class = Class.objects.all()
    classes = []
    for cls in all_class:
        try:
            days = []
            subs = [x.strip() for x in cls.subjects.split(',')]
            sec_num = cls.sections
            class_num = cls.class_num
            perms = list(permutations(range(5)))
            rn.shuffle(perms)
            combs = list(combinations(perms, sec_num))
            rn.shuffle(combs)
            for comb in combs:
                f = False
                
                for j in range(5):
                    subs_ = [comb[i][j] for i in range(sec_num)]
                    if len(subs_)!=len(set(subs_)):
                        f = True
                        break
                if f: continue
                day = []
                
                for section in comb:
                    day.append([subs[i] for i in section])
                days.append(day)

                if len(days)==5:
                    break
            classes.append((days, class_num))
        
        except:
            pass
    return classes
            

        
