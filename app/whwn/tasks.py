from django.contrib.sites.models import Site
from django.conf import settings

from celery import task

@task(ignore_result=True)
def notify_matches(post, site):
    from whwn.models import NotificationMessage
    matches = post.matches()

    def match_text(item, match, site, public=False): 
        if public:
            text = """
                Hello! We've found someone that has something similar to 
                what you need: %(post)s\n
                The contact information for this person should be in the following:
                %(description)s
            """ % {'post': item.name, 'description': match.description}

        else: 
            text = """
                You have a new match for %(post)s.\n
                Check it out at %(site)s%(url)s\n
                Sincerely,\n
                The Team
            """ % {'post': item.name, 
                   'url': match.get_absolute_url(),
                   'site': site.domain}
        return text

    matches = map(lambda x: x._get_object(), matches)
    special = post.owner.username == "whwn-public" and not post.is_needed

    for match in matches:
        contents = match_text(match, post, site, special)
        message = NotificationMessage(sender=match.owner, 
            notify_type=NotificationMessage.NEW_MATCH, contents=contents)
        message.send()
