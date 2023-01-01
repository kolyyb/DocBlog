from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")

def article(request, num_article):
    if num_article in [1, 2, 3]:
        return render(request, f"blog/article{num_article}.html")
    return render(request, f"blog/article_not_found.html", {'num_article': num_article})
