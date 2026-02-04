from tkinter import XView

import flet as ft
from fletx import Xview
from components.keypad import  Keypad


class LoginView(Xview):


    def build(self):
        keypad = Keypad(self.state.handle_key)

        # return ft.Container(
        #             alignment=ft.alignment.center,
        #             # expand=True,
        #             content=ft.Column(
        #                 expand=True,
        #                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #                 controls=[
        #                     ft.Text("Intelli Surveillance", color=ft.Colors.BLUE, size=50),
        #                     # ft.Divider(color=ft.Colors.TRANSPARENT),
        #                     ft.Text("Login to access the system"),
        #                     self.state.passwordField,
        #                     keypad.build(),
        #                 ]
        #             )
        #         )


        return ft.View(
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            vertical_alignment= ft.MainAxisAlignment.CENTER,
            spacing=20,
            # padding=200,

            controls= [
                ft.Container(
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Column(
                        expand=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Divider(color=ft.Colors.TRANSPARENT),
                            ft.Divider(color=ft.Colors.TRANSPARENT),
                            ft.Divider(color=ft.Colors.TRANSPARENT),

                            ft.Text("Intelli Surveillance", color=ft.Colors.BLUE, size=50),
                            ft.Divider(color=ft.Colors.TRANSPARENT),
                            ft.Text("Login to access the system"),
                            ft.Divider(color=ft.Colors.TRANSPARENT),

                            self.state.passwordField,
                            keypad.build(),

                        ]
                    )
                ),

                ft.Text(
                    value="All right reserved.  2025 @ School of Industrial Training and Education, powered by RangoonX",
                    text_align=ft.TextAlign.CENTER
                )
            ],
            floating_action_button=ft.FloatingActionButton(icon=ft.Icons.EXIT_TO_APP,on_click=lambda e: self.page.window.close()),
        )