import flet as ft
from fletx import Xview

key_name = "password"

class PasswordStorage:

    def __init__(self,page : ft.Page):
        self.page = page


    def get_password(self, key= key_name) -> list | None:
        return self.page.client_storage.get(key)

    def update_password(self,key = key_name, value = int) -> bool:
        passwords = self.get_password()
        passwords.append(value)
        return True