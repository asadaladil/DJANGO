from django.contrib import admin
from first_app.models import StudentModel,StudentInfoModel,TeacherInfoModel,EmployeeModel,ManagerModel,Friend,Me,Person,Passport,Post
from first_app.models import Student,Teacher
# Register your models here.

#admin.site.register(StudentModel)
#admin.site.register(StudentInfoModel)
#admin.site.register(TeacherInfoModel)

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display=['id','name','city','designation']
    
class ManagerModelAdmin(admin.ModelAdmin):
    list_display=['id','name','city','designation','take_interview','hiring']
    
admin.site.register(EmployeeModel,EmployeeModelAdmin)
admin.site.register(ManagerModel,ManagerModelAdmin)

class FriendModelAdmin(admin.ModelAdmin):
    list_display=['id','school','section','class_teacher','attendance','hw']
    
admin.site.register(Friend,FriendModelAdmin)

class MeModelAdmin(admin.ModelAdmin):
    list_display=['id','school','section','class_teacher','attendance','hw']
    
admin.site.register(Me,MeModelAdmin)

class personModelAdmin(admin.ModelAdmin):
    list_display=['id','name','city','email']
    
class PassportModelAdmin(admin.ModelAdmin):
    list_display=['id','user','pass_number','page','validity']
    
admin.site.register(Person,personModelAdmin)
admin.site.register(Passport,PassportModelAdmin)

class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','user','post_cap','post_details']
admin.site.register(Post,PostModelAdmin)

class StudentModel(admin.ModelAdmin):
    list_display=['id','name','roll','class_name']
admin.site.register(Student,StudentModel)

class TeacherModel(admin.ModelAdmin):
    list_display=['id','name','subject','student_list','mobile']
admin.site.register(Teacher,TeacherModel)


        