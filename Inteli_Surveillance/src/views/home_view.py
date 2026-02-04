import flet as ft
from fletx import Xview
from components.navigationrail import BodyNavigation
from components.videoStream import VideoStreamUI
from components.keypad import  Keypad

class HomeView(Xview):
    def build(self):
        # container to hold dynamic content
        self.content_container = ft.Container(
            expand=True,
            alignment=ft.alignment.top_left,
            content=ft.Container(expand=True,content=ft.Image(src="ads.jpg",fit=ft.ImageFit.CONTAIN))
        )

        #videostreaming
        self.video_ui = VideoStreamUI(self.page,control_btn=self.state.video_control_btn, video_img = self.state.video_image , status = self.state.status)
        # self.state.open_stream()

        def update_content():
            idx = self.state.home_selected_index
            if idx == 0:
                self.content_container.content = ft.Container(expand=True,content=ft.Image(src="ads.jpg",fit=ft.ImageFit.CONTAIN))

            elif idx == 1:
                # container = ft.Row(expand=True,controls=[self.video_ui.build(),ft.Container(expand=True,bgcolor=ft.Colors.BLUE)])
                self.content_container.content = self.video_ui.build(state = self.state)
                self.video_ui.update_time()
                self.page.update()
            elif idx == 3:
                self.content_container.content = ft.Text("Settings Page", size=30)
            elif idx == 2:
                keypad = Keypad(self.state.handle_key)
                self.content_container.content = ft.Container(
                            alignment=ft.alignment.center,
                            expand=True,
                            content=ft.Column(
                                expand=True,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Divider(color=ft.Colors.TRANSPARENT),
                                    ft.Divider(color=ft.Colors.TRANSPARENT),
                                    ft.Divider(color=ft.Colors.TRANSPARENT),

                                    # ft.Text("Intelli Surveillance", color=ft.Colors.BLUE, size=50),
                                    ft.Divider(color=ft.Colors.TRANSPARENT),
                                    ft.Text("Login to access the Setting"),
                                    ft.Divider(color=ft.Colors.TRANSPARENT),

                                    self.state.passwordField,
                                    keypad.build(),

                                ]
                            )
                        )





            else:
                self.content_container.content = ft.Text("Unknown", size=30)
            self.content_container.update()  # only update container

        # wrap original handler to update content
        original_handler = self.state.on_home_nav_change
        def wrapped_nav_change(e):
            original_handler(e)       # update selected_index
            update_content()          # update container content

        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            appbar=ft.AppBar(
                leading=None,
                title=ft.Text(f"Intelli Paddy Classifier  | {self.page.route[1:]}", size=25, color=ft.Colors.WHITE),
                bgcolor=ft.Colors.BLUE,
                automatically_imply_leading=False,
                actions=[
                    ft.IconButton(ft.Icons.LOGOUT_ROUNDED, icon_color=ft.Colors.WHITE,
                                  on_click=lambda e: self.go("/login"), tooltip="Logout"),
                    ft.IconButton(ft.Icons.CLOSE, icon_color=ft.Colors.RED,
                                  tooltip="Logout", on_click=lambda e: self.page.window.close()),
                ]
            ),
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        BodyNavigation(
                            on_change=wrapped_nav_change,
                            selected_index=self.state.home_selected_index
                        ).build(),
                        ft.VerticalDivider(width=1),
                        self.content_container,
                    ]
                )
            ]
        )
