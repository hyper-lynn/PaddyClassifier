import flet as ft
from fletx import Xstate
from controllers.Storage import PasswordStorage
from controllers.cameraController import CameraController

class MainState(Xstate):
    def __init__(self, page):
        super().__init__(page)

        self.txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100,max_length=4)
        self.passwordField = ft.TextField( password=True,
                                          width=350,
                                          text_align=ft.TextAlign.CENTER,text_style=ft.TextStyle(size=30,))

        self.home_selected_index = 0

        #video src
        self.selected_camera_index = 0
        self.video_running = False
        self.video_image = ft.Image(expand=True,fit=ft.ImageFit.COVER,visible=False)
        self.video_control_btn = ft.ElevatedButton(text="Start VideoStream", on_click= lambda e: self.open_stream(e))
        self.status = ft.Text(value="Video Streaming is not starting yet")
        self.paddy_data = ""
        
        self.cameraStream = CameraController(state = self.page,image=self.video_image, src=0,)
        
        
    def classfiy(self):
        print("main state -> classify")
        lable = self.cameraStream.classifiy()
        self.paddy_data = lable

    def minus_click(self, e):
        self.txt_number.value = str(int(self.txt_number.value) - 1)
        self.update()

    def plus_click(self, e):
        self.txt_number.value = str(int(self.txt_number.value) + 1)
        self.update()

    def handle_key(self,key):
        passStorage = PasswordStorage(page=self.page)

        if key == "Enter":
            if int(self.passwordField.value) in passStorage.get_password():
                print("pass")
                self.go("/home")
            else:
                self.page.open(ft.SnackBar(ft.Text("Wrong Password"),bgcolor=ft.Colors.RED,dismiss_direction=ft.DismissDirection.UP))
                self.page.update()
        elif key == "⌫":
            self.passwordField.value = self.passwordField.value[:-1]
        else:
            self.passwordField.value += key
        self.page.update()
        return None

    def on_home_nav_change(self, e):
        self.home_selected_index = e.control.selected_index
        print("Home selected:", self.home_selected_index)
        self.page.update()

    # Camera selection
    def toggle_video(self, e=None):
        self.video_running = not self.video_running
        self.update()

    def change_camera(self, cam_index: int):
        self.selected_camera_index = cam_index
        self.update()

    def close_stream(self,e):
        self.status.value = "Video streaming is stopped"
        self.status.update()
        self.status.value = "Video streaming is closed"
        self.status.update()
        self.video_control_btn.text = "Start VideoStream"
        self.video_control_btn.on_click = self.open_stream
        self.video_control_btn.update()
        self.page.update()
        self.video_image.visible = False
        self.cameraStream.stop()


    def open_stream(self,e):
        """start_stream"""
        print("camera is started")
        self.status.value = "Video streaming is initialized"
        self.status.update()
        self.page.update()
        self.cameraStream.start()
        self.video_running = True
        self.status.value = "Video streaming is running"
        self.status.update()
        self.video_control_btn.text = "Stop VideoStream"
        self.video_control_btn.on_click = self.close_stream
        self.video_control_btn.update()
        self.video_image.visible = True
        self.page.update()


    



