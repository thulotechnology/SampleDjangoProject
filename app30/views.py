from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tasklist = {
    'day1': 'Learn HTML for 5 hours.',
    'day2': 'Listen to Book The Lean Startup',
    'day3': 'Learn CSS'
}
def index(request):
    return render(request, 'app30/index.html')

def daysdata(request, key):
    try:
        tasklists = list(tasklist.keys())
        index = tasklists.index(key)
        index+=1
        content = {
            'num': index,
            'value': tasklist[key]
            
        }
        return render(request, 'app30/day.html',content)
    except:
        return HttpResponse(f"Something went wrong")
