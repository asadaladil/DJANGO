from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'./first_app/index.html',{'courses': [
        {
            'id':1,'course':'C','teacher': 'Rahim'
        },
        {
            'id':2,'course':'C++','teacher': 'Kahim'
        },
        {
            'id':3,'course':'Pyhton','teacher': 'Rahim'
        }
    ]
        
    })

# Create your views here.
