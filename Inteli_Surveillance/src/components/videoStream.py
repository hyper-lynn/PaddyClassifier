
import flet as ft
from datetime import datetime
import time
from controllers.cameraController import *
from components.data_show_log import  ShowDataLog
class VideoStreamUI:
    def  __init__(self,master : ft.Page , video_img, status , control_btn   ):
        super().__init__()
        self.master = master
        # self.state = state
        self.status = status
        self.video_img = video_img
        # --- UI ELEMENTS ---
        self.time_text = ft.Text(value="", size=20)

        self.start_video_btn = control_btn
        
        
        self.showdata = ShowDataLog()
        
        

    def build(self,state):
        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.START,
            expand=True,
            spacing=10,
            controls=[
                self.time_text,
                ft.Divider(),
                ft.Row(controls=[ft.Text("State : " , color=ft.Colors.GREEN),self.status]),
                self.start_video_btn,
                # self.state,
                # self.video_img,
                ft.Row(expand=True, spacing=10,controls=[ft.Container(expand=2,content=self.video_img),ft.VerticalDivider(),self.showdata.build(state = state)]),

            ],
        )




    # ------------------- TIME -------------------
    def update_time(self):
        while True:
            now = datetime.now()
            formatted_time = now.strftime("%I:%M:%S %p")
            formatted_date = now.strftime("%A, %B %d, %Y")
            self.time_text.value = f"{formatted_date} | {formatted_time}"
            try:
                self.master.update()
            except RuntimeError:
                break
            time.sleep(1)
