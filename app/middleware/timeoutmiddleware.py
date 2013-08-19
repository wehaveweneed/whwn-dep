import datetime
import django


class TimeoutMiddleware(object):

    def process_request(self, request):
        if request.user.is_authenticated():
            if 'lastRequest' in request.session:
                elapsedTime = datetime.datetime.now() - \
                    request.session['lastRequest']
                if elapsedTime.seconds > 1200:
                    del request.session['lastRequest']
                    django.contrib.auth.logout(request)

            request.session['lastRequest'] = datetime.datetime.now()
        else:
            if 'lastRequest' in request.session:
                del request.session['lastRequest']

        return None
