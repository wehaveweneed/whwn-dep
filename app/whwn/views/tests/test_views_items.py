#from django.test import TestCase
#from whwn.factories import UserFactory, ItemFactory

#class ItemsViewsTestCase(TestCase):

    ##def setUp(self):
        ##self.user = UserFactory.create(
                    ##username="tester",
                    ##password="tester",
                    ##email="tester@tester.com"
                ##)
        ##self.client.login(username="tester", password="tester")
        ##items = [ItemFactory.create(owner=self.user) for x in xrange(0, 9)]


    ##def test_items_view(self):
        ##resp = self.client.get('/items/')
        ##self.assertEqual(resp.status_code, 200)
        ##self.assertTrue('items' in resp.context)
    
    ##def test_item_view(self):
        ##item_id = items[0].item_id
        ##resp = self.client.get('/items/%s' % item_id)
        ##self.assertEqual(resp.status_code, 200)
        ##self.assertEqual(resp['Content-Type'], 'application/json')

    ##def test_item_details_view(self):
        ##resp = self.client.get('/items/details/1')
        ##self.assertEqual(resp.status_code, 200)
        ##self.assertTrue('item' in resp.context)
        ##self.assertTrue('can_edit' in resp.context)

    ##def test_item_matches_view(self):
        ##raise NotImplementedError('This needs to get done.')

    ##def test_item_heatmap_view(self):
        ##raise NotImplementedError('This needs to get done.')

    ##def test_item_heatmap_data_view(self):
        ##raise NotImplementedError('This needs to get done.')

