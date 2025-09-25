from django.shortcuts import render,redirect
from.models import Question
# Create your views here.
def quiz_home(request):
    if request.method == 'POST':
        questions=Question.objects.all()
        score = 0
        for q in questions:
            selected= request.POST.get(f"q{q.id}")
            if selected and int(selected) == q.correct_option:
                score += 1 
        return render(request, 'quizapp/result_home.html', {'score': score, 'total': questions.count()})
    else:
        questions = Question.objects.all()
        return render(request, 'quizapp/quiz_home.html',{'questions': questions})


def quiz_view(request):
    total_questions = Question.objects.count()
    current_q = int(request.GET.get('q', 1))  # default is question 1

    # Handle bounds
    if current_q < 1:
        current_q = 1
    elif current_q > total_questions:
        current_q = total_questions

    question = Question.objects.all()[current_q - 1]  # get current question

    return render(request, 'quizapp/quiz_home.html', {
        'question': question,
        'current_q': current_q,
        'total_questions': total_questions
    }) 
def result_view(request):
    return render(request, 'quizapp/result_home.html')                                