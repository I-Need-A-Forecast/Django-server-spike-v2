from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect #, Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.template import loader

from .models import Choice, Question

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future). (lte == less than or equal)
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        #old
        #"""Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]

#old
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

##************                      --> READ FOR LATER!!!! <--
##     A shortcut: render()
##
## It’s a very common idiom to load a template, fill a context and return an
## HttpResponse object with the result of the rendered template. Django provides
## a shortcut. Here’s the full index() view, rewritten:
#
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)
#
## Note that once we’ve done this in all these views, we no longer need to import
## loader and HttpResponse (you’ll want to keep HttpResponse if you still have the
## stub methods for detail, results, and vote).
##
## The render() function takes the request object as its first argument, a template
## name as its second argument and a dictionary as its optional third argument. It
## returns an HttpResponse object of the given template rendered with the given context.
##************

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

#Appears to be now swapped out for the above function.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

#old
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})

#def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/details.html', {'question': question})

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)#

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#old
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
