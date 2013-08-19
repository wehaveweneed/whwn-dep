from django.test import TestCase

from whwn.factories import MessageFactory
from whwn.models import Message

class MessageTestCase(TestCase):

    def test_soft_delete(self):
        m = MessageFactory.create()
        self.assertFalse(m.deleted)
        
        m.delete()
        self.assertNotEqual(m, None)
        self.assertTrue(m.deleted)

    def test_bulk_soft_delete(self):
        m1 = MessageFactory.create()
        m2 = MessageFactory.create()
        ms = Message.objects.all()

        ms.delete()
        
        self.assertNotEqual(m1, None)
        self.assertNotEqual(m2, None)

        # Refresh the objects from the database
        m1 = Message.objects.get(id=m1.pk)
        m2 = Message.objects.get(id=m2.pk)

        self.assertTrue(m1.deleted)
        self.assertTrue(m2.deleted)
