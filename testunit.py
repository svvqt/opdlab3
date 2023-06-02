import unittest
from web import app
class TestApp(unittest.TestCase):

    def setUp(self): # подключаем клиент для тестов
        self.app = app.test_client()

    def test_successful_login(self):  # проверка на вход с правильными логином и паролем
        response = self.app.post('/login', data=dict(login='admin', password='admin228'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Вход успешен !'.encode('utf-8'), response.data)

    def test_wrong_userlogin(self):  # проверка на ввод неправильного логина
        response = self.app.post('/login', data=dict(login='user', password='password'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Пользователь не обнаружен'.encode('utf-8'), response.data)

    def test_wrong_password(self):  # проверка на ввод неправильного пароля
        response = self.app.post('/login', data=dict(login='admin', password='ad'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Неправильный пароль'.encode('utf-8'), response.data)
    
    def test_goto_reg(self): # проверка на переход к регистрации
        response = self.app.get('/regi')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Регистрация'.encode('utf-8'), response.data)

    def test_reg(self):  # проверка регистрации нового пользователя
        response = self.app.post('/registration', data=dict(login='daubi', password='daubi11'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Регистрация'.encode('utf-8'), response.data)

    def test_wrong_reg(self):  # проверка регистрации с использованием имени уже существующего пользователя
        response = self.app.post('/registration', data=dict(login='daubi', password='daubi11'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Имя пользователя занято'.encode('utf-8'), response.data)
    def test_logout(self):  # проверка на выход из аккаунта
        response = self.app.get('/log_out')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Введите логин и пароль'.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()
