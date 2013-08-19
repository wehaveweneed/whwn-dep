from datetime import time
from exceptions import Exception
from smtplib import SMTPException
from twilio.rest import TwilioRestClient
import operator
import json
import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.utils.datetime_safe import date
from django.utils.dateformat import format
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth.models import User
from annoying.decorators import ajax_request, render_to
from annoying.functions import get_object_or_None

from whwn.models import (Item, UserProfile, EmailSender, Message)
from django.views.generic import ListView, View
from settings.common import TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER
from settings.common import DEFAULT_FROM_EMAIL
from django.utils import simplejson

DELETED_POST_CONVO_JSON = {
    'item_not_found': True,
    'item': {'name': 'not found', 
            'owner': 'no one',
            'other': 'no one',
            'amount': 0,
            'location': 'not found',
            'description': 'not found',
            'is_needed': True},
}



#class ConversationListView(ListView):
    #""" Grabs the users's conversations and messages for the first
    #message """
    #template_name = "messages/index.html"
    #context_object_name = "convos"

    #@method_decorator(login_required)
    #def dispatch(self, request, *args, **kwargs):
        #return super(ConversationListView, self).dispatch(request, 
                                                      #*args, **kwargs)
    #def get(self, request, *args, **kwargs):
        #return super(ConversationListView, self).get(request, *args, **kwargs)
        
    #def get_queryset(self):
        #return self.request.user.conversation_set.filter(active=True)

    #def get_context_data(self, **kwargs):
        #context = super(ConversationListView, self).get_context_data(**kwargs)

        ## First convo is displayed so needs extra info
        #if len(self.object_list) > 0:
            #convo = self.object_list[0]
            #context['other'] = convo.users.exclude(id=self.request.user.id)[0]  
        #context['convos'] = self.object_list
        #return context


#class ConversationView(View):

    #@method_decorator(ensure_csrf_cookie)
    #def dispatch(self, request, *args, **kwargs):
        #if "application/json" in request.META.get('HTTP_ACCEPT'): 
            #return super(ConversationView, self).dispatch(request, *args, **kwargs)
        #else:
            #convos =  request.user.conversation_set.filter(active=True)
            #context = {}
            #context['convos'] = convos
            #return render_to_response("messages/index.html", context)

    #def get(self, request, *args, **kwargs):
            #convo = Conversation.objects.get(id=self.kwargs["id"])
            #json = {}
            #messages = []
            #for message in convo.sorted_messages:
                #messages.append({ 'sender': message.sender.username,
                                  #'sent_on': format(message.sent_on, 'U'),
                                  #'contents': message.contents })
            #item = convo.get_item()
            #others = convo.users.exclude(id=item.owner_id)
            #item = { 
                #'name': item.name, 
                #'owner': item.owner.username,
                #'other': others[0].username if others else 'no one',
                #'amount': item.amount,
                #'location': item.location.name,
                #'description': item.description,
                #'is_needed': item.is_needed,
                #'deleted': item.deleted,
            #}
            #json['item'] = item
            #json['messages'] = messages if messages else []
            #json['request'] = { 'user': self.request.user.username }
            #return HttpResponse(simplejson.dumps(json),
                                #mimetype="application/json")

    #def item(self, request, *args, **kwargs):
        #convo = Conversation.objects.get(id=self.kwargs["id"])
        #contents = request.POST['m']
        #message = convo.send_message(request.user, contents)

        #json = {}
        #json['message'] = { 'sender': message.sender.username,
                            #'sent_on': format(message.sent_on, 'U'),
                            #'contents': message.contents }
        #return HttpResponse(simplejson.dumps(json),
                            #mimetype="application/json")

#class CreateConversationView(View):

    #def item(self, request, *args, **kwargs):
        #item = Item.objects.get(item_id=kwargs['id'])
        #convo = item.create_conversation_with(request.user)
        #msg = convo.send_message(request.user, request.POST['msg'])

        #json = {}
        #json['id'] = convo.id
        #return HttpResponse(simplejson.dumps(json),
                            #mimetype="application/json")
