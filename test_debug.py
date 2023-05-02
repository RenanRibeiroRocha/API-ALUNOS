from unittest import TestCase
from .app import app

class test_debug(TestCase):

    
    def test_login(self):
        # Teste credencial correta
        response = self.app.post('/', data=dict(nome='usuario.teste', senha='teste@123'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    if __name__ == "__main__":
        TestCase.main()