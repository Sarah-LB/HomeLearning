from django.shortcuts import render


def view_reviews(request):
    """ A view that renders the review contents page """

    return render(request, 'reviews/reviews.html')