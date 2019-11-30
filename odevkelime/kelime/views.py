from django.http import HttpResponse
from django.shortcuts import render
import operator


# Create your views here.

def index(request):
    return render(request, 'index.html')

def hesapla(request):
    fulltext = request.GET['fulltext']
    full_words = fulltext.split(' ')
    full_words = [word.lower() for word in full_words]
    # create dictionary word[word_count]
    words = {}
    for word in full_words:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    # sort dictionary by largest count value
    # returned as list, so need to convert back to dictionary
    words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    words = dict(words)

    return render(request,'hesapla.html',
    {'fulltext': fulltext,
    'word_len': len(full_words),
    'word_len_uniq': len(set(full_words)),
    'word_dict': words})

def hakkinda(request):
    return render(request, 'hakkinda.html')