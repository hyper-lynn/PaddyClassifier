import flet as ft
class BodyNavigation(ft.Control):
    def __init__(self, on_change=None, selected_index=0):
        super().__init__()
        self.on_change = on_change
        self.selected_index = selected_index

    def build(self):
        return ft.NavigationRail(
            selected_index=self.selected_index,
            on_change=self.on_change,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=80,
            bgcolor=ft.Colors.TRANSPARENT,


            destinations=[
                ft.NavigationRailDestination(icon=ft.Icons.DASHBOARD, label="Dashboard",selected_icon=ft.Icons.DASHBOARD_OUTLINED),
                ft.NavigationRailDestination(icon=ft.Icons.VIDEO_CAMERA_FRONT, label="Classifier"),
                ft.NavigationRailDestination(icon=ft.Icons.SETTINGS, label="Settings"),
                # ft.NavigationRailDestination(icon=ft.Icons.TELEGRAM, label="Alarm"),

            ],
        )
