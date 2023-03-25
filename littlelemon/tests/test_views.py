from django.test import TestCase
from restaurant.models import MenuItem
from django.urls import reverse
import json
from restaurant.serializers import MenuItemSerializer

# Test for MenuItemView
class MenuItemViewTest(TestCase):
    def setUp(self) -> None:
        MenuItem.objects.create(title="fried fish", price="7.50", inventory="50")       
        MenuItem.objects.create(title="chicken roll", price="4.50", inventory="60")
        
    def test_get_all(self):
        retrieved_object = MenuItem.objects.all()

        serialized_object = MenuItemSerializer(retrieved_object, many=True)

        response = self.client.get(reverse('menu-items')) 
        
        self.assertEqual(response.data, serialized_object.data)
        
        # Another method to test view data.
        
        # serialized_object = json.loads(json.dumps(serialized_object.data))      
        # response = str(response.content, 'UTF-8')
        # response = json.loads(response)
        
        # self.assertEqual(response, serialized_object)
        
