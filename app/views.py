from annoying.decorators import render_to
from django.shortcuts import redirect

@render_to('index.html')
def root(request):
    if request.user.is_authenticated():
        return redirect(reverse("inventory_list"))
    else:
        return {}
