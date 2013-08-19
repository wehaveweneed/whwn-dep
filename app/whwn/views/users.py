from annoying.decorators import render_to, ajax_request
from annoying.functions import get_object_or_None
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.db import connections
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render, render_to_response
from django.views.generic import TemplateView, FormView, RedirectView, View
from whwn.models import UserProfile, EmailSender, Team
import random
import string


class LoginView(FormView):
    template_name = "index.html"
    form_class = AuthenticationForm
    get_success_url = lambda x: reverse('inventory_list')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse("inventory_list"))
        else:
            return super(LoginView, self).get(self, request, *args, **kwargs)

    def form_valid(self, form):
        user = auth.authenticate(username=form.cleaned_data['username'],
                                 password=form.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                auth.login(self.request, user)
                return redirect(reverse('inventory_list'))
            else:
                messages.error(self.request, 'Your account is not active, ' + \
                               'please check your email.')
                return super(LoginView. self).form_valid(form)
        else:
            messages.error(self.request, 
                           'The username or password is incorrect.')
            return super(LoginView, self).form_valid(self, form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please enter a username and a password.')
        return super(LoginView, self).form_invalid(form)

class SubscribeView(TemplateView):
    template_name = "registration/subscribe.html"
    

class LogoutView(RedirectView):
    get_redirect_url = lambda x: reverse('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

class SettingsView(TemplateView):
    template_name = "users/settings.html"

    @method_decorator(login_required)
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super(SettingsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)

        account = {'username': self.request.user.username,
                   'email':    self.request.user.email,
                   'phone_number':    self.request.user.get_profile().phone_number,
                   'team': self.request.user.get_profile().team,
                   'password': '*******',
                   'date_format': 'mm/dd/yy',
                   'time_format': '12hr',
                  }

        comm = {'sms': 'On',
                'email': 'On' }

        # location = self.request.user.get_profile().point

        context['account'] = account
        context['comm'] = comm
        # context['default_location'] = location

        return context


class UpdateEmailView(View):

    @method_decorator(ajax_request)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateEmailView, self).dispatch(request, *args,
                                                      **kwargs)
    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.get_profile()
        email = request.POST["email"]
        profile.change_email(email)
        json = {'status': 'Success'}
        return HttpResponse(simplejson.dumps(json),
                            mimetype="application/json")

class UpdatePhoneNumberView(View):

    @method_decorator(ajax_request)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdatePhoneNumberView, self).dispatch(request, *args,
                                                      **kwargs)
    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.get_profile()
        phone_number = request.POST["phone_number"]
        profile.change_phone_number(phone_number)
        json = {'status': 'Success'}
        return HttpResponse(simplejson.dumps(json),
                            mimetype="application/json")



class UpdatePasswordView(View):

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.get_profile()
        password = request.POST["password"]
        profile.change_password(password)
        json = {'status': 'Success'}
        return HttpResponse(simplejson.dumps(json),
                            mimetype="application/json")

class UpdateTeamView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.get_profile()
        teams = Team.objects.filter(pk=request.POST['team'])
        if len(teams) == 0:
            json = {'status': 'Not found'}
        else:
            profile.team = teams[0]
            profile.save()
            json = {'status': 'Success'}
        return HttpResponse(simplejson.dumps(json),
                            mimetype="application/json")

class UpdateLocationView(View):

    def post(self, request, *args, **kwargs):
        u = request.user.get_profile()
        name = request.POST['name']
        lat = request.POST['latitude']
        lon = request.POST['longitude']
        try:
            u.latitude = float(lat)
            u.longitude = float(lon)
        except ValueError:
            return HttpResponse(simplejson.dumps({'error': 'Invalid latitude/longitude coordinates.'}),
                    mimetype="application/json")
        u.save()
        json = { 'name': name,
                 'latitude': float(lat),
                 'longitude': float(lon) }
        return HttpResponse(simplejson.dumps(json),
                            mimetype="application/json")


class DeleteLocationView(View):

    def post(self, request, *args, **kwargs):
        # location = Location.objects.get(id=request.POST['id'])
        profile = request.user.get_profile()
        # location.delete()
        # profile.location = None
        # profile.save()
        json = {'status': 'Success' }
        return HttpResponse(simplejson.dumps(json),
                            mimetype="application/json")

class AddLocationView(View):

    def post(self, request, *args, **kwargs):
        profile = self.request.user.get_profile()
        # location = Location.objects.create(name=request.POST['name'],
                                           # point=Point(float(request.POST['longitude']),
                                                       # float(request.POST['latitude'])))
        # location.save()
        # profile.location = location
        # profile.save()
        json = {'status': 'Success'}
        serialized_location = { 'name': request.POST['name'],
                                'longitude': float(request.POST['longitude']),
                                'latitude': float(request.POST['latitude'])
                                }
        json['location'] = serialized_location
        return HttpResponse(simplejson.dumps(json),
                            mimetype="application/json")

@login_required
@render_to("users/inventory.html")
def inventory(request):
    """ Returns all the items that a user 'has' """
    user = UserProfile.objects.get(user=request.user)
    items = user.get_user_inventory()
    return {"items": items}

@login_required
@render_to('users/user_requests.html')
def requests(request):
    """ Returns all the items that a user 'needs' """
    items = Items.objects.filter(possessor=request.user, requested=True)
    return {"items": items}

@login_required
@render_to('users/inventory.html')
def me(request):
    user = UserProfile.objects.get(user=request.user)
    haves = user.get_user_inventory(True)
    needs = user.get_user_requests(True)
    return {"haves": haves, "needs": needs}

@login_required
@render_to("users/message_inbox.html")
def user_messages(request):
    """ Displays all the messages that are sent to the user """
    conversations = request.user.conversation_set
    return {"conversations": conversations}

@login_required
@render_to("users/user_profile.html")
def profile(request, id):
    """ Displays all of the items owned by the users """
    user_profile = get_object_or_None(UserProfile,id=id)

    if user_profile is None:
        raise Http404

    items_have = user_profile.items_have()
    user_name = user_profile.user.username

    return {"items_have": items_have, "user_name": user_name}

def pw_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    """ Generates a random password of length size combining uppercase,lowercase
        and digits """
    return ''.join(random.choice(chars) for x in range(size))


def confirm_location_change(request,old_location,new_location):
    return render(request,'users/change_location.html',{"new_location":new_location,"old_location":old_location})


####### Ajax API type requests ######

@login_required
@ajax_request
def unread_count(request, user):
    user_profile = UserProfile.objects.get(user=request.user)
    return HttpResponse(user_profile.get_unread_count())

@login_required
@ajax_request
def teams_autocomplete(request):
    if request.user.is_authenticated():
        team_names = map(lambda t: { 'label': t.name, 'value': t.pk }, Team.objects.all())
        return {'teams': team_names}
    return {}
