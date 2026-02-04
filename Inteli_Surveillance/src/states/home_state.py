from fletx import Xstate

class HomeState(Xstate):
    def __init__(self, page):
        super().__init__(page)
        self.selected_index = 0

    def on_nav_change(self, e):
        self.selected_index = e.control.selected_index
        print("Selected:", self.selected_index)
        self.update()
