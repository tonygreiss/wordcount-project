from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter  

def homepage(request):
	return render(request, "home.html")

def count(request):
	fulltext = request.GET["fulltext"]
	
	words_list = fulltext.split()
	
	word_dict = {}

	for word in words_list:
		if word in word_dict:
			word_dict[word] += 1
		else:
			word_dict[word] = 1

	sorted_words = sorted(word_dict.items(), key = itemgetter(1), reverse = True)

	print(sorted_words)

	return render(request, "count.html", {'fulltext':fulltext, "word_dict":sorted_words ,"count":len(words_list)})

def about(request):
	return render(request, "about.html")