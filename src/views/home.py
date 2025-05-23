import flet as ft

from .big_cars import BigCars
from .bikes import Bikes
from .cars import Cars

class Home(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.bgcolor = ft.Colors.WHITE
        self.padding = 0
        self.spacing = 0
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.car = Cars(width=page.window.width, height=page.window.height)
        self.big_car = BigCars(width=page.window.width, height=page.window.height)
        self.bike = Bikes(width=page.window.width, height=page.window.height)


        self.navigation_bar = ft.NavigationBar(
            animation_duration=3000,
            on_change=self.on_change,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.DIRECTIONS_CAR,
                    label="Cars",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FIRE_TRUCK,
                    label="Big Cars",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.PEDAL_BIKE,
                    label="Bikes",
                )
            ]
        )

        self.appbar = ft.AppBar(
            title=ft.Text(
                value="Cars",
                color=ft.Colors.BLACK,
                font_family="PoppinsSemiBold",
                weight=ft.FontWeight.BOLD,
                size=20,
                style=ft.TextStyle(
                    letter_spacing=-0.5,
                    height=22.5
                ),
            ),
            elevation_on_scroll=0,
            bgcolor=ft.Colors.WHITE,
            center_title=True,
        )

        self.con = ft.Container(
            content=self.car,
            alignment=ft.alignment.center
        )

        self.controls = [
            self.con
        ]

    def on_change(self, e: ft.ControlEvent) -> None:
        print(type(e.data))
        match e.data:
            case "0":
                self.con.content = self.car
                self.appbar.title.value = "Cars"
            case "1":
                self.con.content = self.big_car
                self.appbar.title.value = "Big Cars"
            case "2":
                self.con.content = self.bike
                self.appbar.title.value = "Bikes"

        self.con.update()
        self.appbar.title.update()
