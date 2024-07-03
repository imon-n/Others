from django.shortcuts import render

def alumni_list(request):
    return render(request, 'alumni_list.html')
