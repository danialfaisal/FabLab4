from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from courses.models import Course
from students.models import Enroll
from .cart import Cart
from .forms import CartAddCourseForm


@require_POST
def cart_add(request, slug):
    cart = Cart(request)
    course = get_object_or_404(Course, slug=slug)
    form = CartAddCourseForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(course=course, quantity=cd['quantity'], update_quantity=False)
    return redirect('cart:cart_detail')


def cart_remove(request, slug):
    cart = Cart(request)
    course = get_object_or_404(Course, slug=slug)
    cart.remove(course)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def cart_checkout(request):
    carts = Cart(request)
    for cart in carts:
        course = cart['course']
        # course = get_object_or_404(Course, slug=course.slug)
        Enroll.objects.create(course=course, user_id=request.user.id)
    messages.success(request, 'Successfully checked out!')
    carts.clear()
    return redirect(reverse_lazy('account:enrolled-courses'))
