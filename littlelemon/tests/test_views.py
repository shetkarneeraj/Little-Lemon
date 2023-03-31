from django.test import TestCase, Client
from restaurant.models import Menu
from django.http import JsonResponse
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    
    def setup(self):
        self.client = Client()
        
        Menu.objects.create(title='Banku', price= 23, inventory=5 )
    
    def test_getall(self):
        response = self.client.get('/menu')
        data = Menu.objects.get(title='Banku', price= 23, inventory=5)
        response_data = JsonResponse(response)
        expected_data = MenuSerializer(data)
        self.assertEquals(response_data, expected_data)
        

