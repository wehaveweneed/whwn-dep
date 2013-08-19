from django.contrib.auth.models import User
from django.db import models
from whwn.models import Team
from whwn.models.abstract import Timestamps, SoftDeletable


class Message(Timestamps, SoftDeletable):
    """ Keeps track of conversation between the system and users """

    class Meta:
        app_label = "whwn"
        get_latest_by = "created_at"
        ordering = ["created_at"]

    author = models.ForeignKey(User)
    contents = models.TextField(verbose_name='Message', default="")
    flagged = models.BooleanField(default=False)
    team = models.ForeignKey(Team)
