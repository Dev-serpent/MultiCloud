# coding: utf-8
import ui
from core.api import login, register_user

class iPadGUI:
    def __init__(self):
        self.user = None
        self.main_view = self.make_login_view()

    def make_login_view(self):
        view = ui.View(name='Login', background_color='white')
        
        username_field = ui.TextField(placeholder='Username')
        username_field.frame = (50, 50, 200, 32)
        view.add_subview(username_field)
        
        password_field = ui.TextField(placeholder='Password', secure=True)
        password_field.frame = (50, 100, 200, 32)
        view.add_subview(password_field)
        
        def login_action(sender):
            username = username_field.text
            password = password_field.text
            try:
                self.user = login(username, password)
                if self.user:
                    self.main_view.close()
                    self.main_view = self.make_main_view()
                    self.main_view.present('sheet')
                else:
                    ui.alert('Login failed.')
            except Exception as e:
                ui.alert(str(e))

        login_button = ui.Button(title='Login', action=login_action)
        login_button.frame = (50, 150, 200, 32)
        view.add_subview(login_button)
        
        return view

    def make_main_view(self):
        view = ui.View(name=f'MultiCloud - {self.user.username}', background_color='white')
        
        # TODO: Add main UI elements
        label = ui.Label(text='Welcome!')
        label.size_to_fit()
        label.center = (view.width * 0.5, view.height * 0.5)
        view.add_subview(label)
        
        return view

    def run(self):
        self.main_view.present('sheet')

if __name__ == '__main__':
    iPadGUI().run()
