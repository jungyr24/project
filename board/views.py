from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProblemInputForm
from board.scraping import problem_scraping

def main_page(request):
    if( request.user.is_authenticated == True):
        return render(request, 'board/base.html', {})
    else:
        return redirect('login')

# 문제 긁어오기
def prob_page(request):
    return render(request, 'board/test.html')




def tab_page(request):
    return render(request, 'board/tab.html', {})


def new_number(request):
    problem = {}
    if request.method == 'POST':
        form = ProblemInputForm(request.POST)
        if form.is_valid():
            number=form.cleaned_data['number']
            print(number)
            problem = problem_scraping(number)

    elif request.method == 'GET':
        form = ProblemInputForm()

    else:
        pass
    return render(request, 'board/test.html', {'problem': problem})