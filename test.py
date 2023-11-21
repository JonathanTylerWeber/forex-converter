from unittest import TestCase
from app import app

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont_show_debug_toolbar']

class FlaskTests(TestCase):
    def test_start_page(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Currency Converter</h1>', html)

    def test_convert_page(self):
        with app.test_client() as client:
            form_data = {
            'from-currency': 'USD',
            'to-currency': 'USD',
            'amount': '100'
            }   
            res = client.post('/convert', data=form_data)
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<p>100 USD</p>', html)
