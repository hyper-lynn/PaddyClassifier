import flet as ft
from fletx import Xview

class Keypad(Xview):
    def __init__(self, on_key_press=None):
        self.on_key_press = on_key_press
        self.keys = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["Enter", "0", "⌫"]
        ]
        self.char = []
    def build(self):
        rows = []
        row_keys: list[str]
        for row_keys in self.keys:
            row = ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton(
                        key,
                        bgcolor=ft.Colors.BLUE_100,
                        color=ft.Colors.BLACK,
                        width=90,
                        height=90,
                        on_click=lambda e, k=key: self.key_pressed(k)
                    ) for key in row_keys




                ],
                spacing=10
            )
            rows.append(row)

        return ft.Column(
            controls=rows,
            spacing=5,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )

    def key_pressed(self, key):

        if self.on_key_press:
            self.on_key_press(key)  # call the method passed from MainState
        return None