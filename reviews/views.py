from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product

@login_required
def view_reviews(request):
    """ A view that renders the review contents page """

    return render(request, 'reviews/reviews.html')
