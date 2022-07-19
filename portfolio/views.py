from django.shortcuts import render
from .models import Card, Illustration, Journal, Package
from django.views import generic

def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cards = Card.objects.filter(name__contains=searched)
        illustrations = Illustration.objects.filter(name__contains=searched)
        journals = Journal.objects.filter(name__contains=searched)
        packages = Package.objects.filter(name__contains=searched)

        return render(request,
        'portfolio/search_results.html',
        {'searched':searched, 'cards':cards, 'illustrations':illustrations, 'journals':journals, 'packages':packages})
    else:
        return render(request, 'portfolio/search_results.html', {})

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


class CardListView(generic.ListView):
    model = Card


class CardDetailView(generic.DetailView):
    model = Card

    def get_context_data(self, *args, **kwargs):
        context = super(CardDetailView, self).get_context_data(*args, **kwargs)
        context['card_list'] = Card.objects.all()
        return context


class IllustrationListView(generic.ListView):
    model = Illustration


class IllustrationDetailView(generic.DetailView):
    model = Illustration

    def get_context_data(self, *args, **kwargs):
        context = super(IllustrationDetailView, self).get_context_data(*args, **kwargs)
        context['illustration_list'] = Illustration.objects.all()
        return context


class JournalListView(generic.ListView):
    model = Journal


class JournalDetailView(generic.DetailView):
    model = Journal

    def get_context_data(self, *args, **kwargs):
        context = super(JournalDetailView, self).get_context_data(*args, **kwargs)
        context['journal_list'] = Journal.objects.all()
        return context


class PackageListView(generic.ListView):
    model = Package


class PackageDetailView(generic.DetailView):
    model = Package

    def get_context_data(self, *args, **kwargs):
        context = super(PackageDetailView, self).get_context_data(*args, **kwargs)
        context['package_list'] = Package.objects.all()
        return context
