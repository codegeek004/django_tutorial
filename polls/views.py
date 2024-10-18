from django.shortcuts import render
from django.db.models import F 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Question
from django.urls import reverse
from .models import Choice, Question
from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = question
    template_name = "polls/results.html"

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(request, "polls/index.html", context)

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

    # #########another approach##################
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "poll/detail.html", {"question: ": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
                request, 
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice"
                },
            )
    else:
        selected_choice.votes = F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results"), args=(question.id,))



