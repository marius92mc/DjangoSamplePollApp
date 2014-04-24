from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.template import RequestContext, loader

from polls.models import Poll, Choice

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	context = {'latest_poll_list': latest_poll_list} # context is a dictionary mapping template variable names to Python objects
	return render(request, 'polls/index.html', context)
	"""The render() function takes the request object as its first argument,
			   a template name as its second argument 
			   and a dictionary as its optional third argument.
			   It returns an HttpResponse object of the given template
			   rendered with the given context.
	"""

def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	context = {'poll': poll}
	return render(request, 'polls/detail.html', context) 


def results(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	context = {'poll': poll}
	return render(request, 'polls/results.html', context)


def vote(request, poll_id):
	try:
		p = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
		# request.POST['choice'] returns the ID of the selected choice, 
		# as a string. request.POST values are always strings.
	except (KeyError, Choice.DoesNotExist):
		#redisplay the poll voting form
		return render(request, 'polls/detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice."
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing 
		# with POST data. This prevents data from being posted twice if a user 
		# user hits the Black button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
		# reverse() function helps avoid having to hardcode a URL in the view function
		# reverse() returns something like '/polls/3/results/'



# Create your views here.
