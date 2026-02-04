import flet as ft
from fletx import Xapp, route

from states.main_state import MainState
from views.home_view import HomeView
from views.login_view import LoginView


def main(page: ft.Page) -> None:
    page.title = "School of Industrial Training & Education"
    page.theme_mode = "light"
    page.window.full_screen = True
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.window.center()

    # Initialize Xapp with MainState
    app = Xapp(
        page=page,
        init_route="/home",
        state=MainState,
        routes=[
            route(route="/login", view=LoginView),
            route(route="/home", view=HomeView),
        ]
    )

    # Stop all threads when the page closes
    def on_close(e):
        if hasattr(app.state, "video_running"):
            app.state.video_running = False

    page.on_close = on_close



ft.app(main, view=ft.AppView.FLET_APP, assets_dir="assets")



#
# def add(x:int,y:int)-> int:
#     return x+y
#
# data = add(x=1,y=2)
# print(data)






