from rest_framework.test import APITestCase


# La clase APITestCase sirve para hacer caso de test como unittest
class EtiquetasTestCase(APITestCase):
    def test_crear_etiqueta_success(self):
        # hago la peticion a mi backend con cierta data en el body
        request = self.client.post('/gestion/etiquetas', data={
            'nombre': 'Frontend'
        })
        print(request.data)
        # comparo que el estado de respuesta sea un 201
        self.assertEqual(request.status_code, 201)
        # assertEqual > afirmamos que el primer parametro debera ser igual que el segundo

        self.assertEqual(1, 1)

    def test_listar_etiquetas_success(self):
        request = self.client.get('/gestion/etiquetas')
        print(request.data)
        self.assertEqual(1, 1)
