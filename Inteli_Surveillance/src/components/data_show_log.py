# datashow_log.py
import flet as ft
from controllers.cameraController import CameraController

class ShowDataLog:
    def __init__(self, ):
        self.result = ft.Text("Unknown", size=20, weight="bold")

    def on_classify(self, e):
        print("classify")
        self.state.classfiy()
        self.label = self.state.paddy_data
        self.result.value = self.label
        self.result.update()

    def build(self,state):
        self.state = state
        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.Divider(),
                ft.Row(
                    [
                        ft.Text("Result:", size=30),
                        self.result
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30
                ),
                ft.Divider(),
                ft.ElevatedButton(
                    "Capture & Predict",
                    width=300,
                    height=50,
                    on_click=self.on_classify
                )
            ]
        )
