import flet as ft



class Detail(ft.View):
    def __init__(
            self,
            page: ft.Page,
    ):
        super().__init__()
        self.route = "/detail"
        self.bgcolor = ft.Colors.WHITE
        self.padding = 0
        self.spacing = 0

        self.cars: dict = page.session.get("micanic")
        #print(self.cars)

        self.carsa = {
            "id": 1,
            "model": "Classic Car",
            "price": 34,
            "bgcolor": "#b67853",
            "image": "/images/cars/Beep Beep Medium Vehicle.png"
        }

        self.__header = ft.AppBar(
            title=ft.Text(
                value=self.cars.get("header_title"),
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
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK_IOS_SHARP,
                on_click=lambda e: e.page.go(self.cars.get("back"))
            )

        )

        self.__image = ft.Container(
            image=ft.DecorationImage(
                src=self.cars.get("image"),
                fit=ft.ImageFit.CONTAIN,
            ),
            width=page.window.width,
            height=300
        )

        self.__bottom_sheet = ft.Container(
            bgcolor=self.cars.get("bgcolor"),
            height=360,
            width=page.window.width,
            border_radius=ft.border_radius.horizontal(left=20, right=20),
            content=ft.Container(
                padding=ft.padding.only(top=40, left=25, right=25, bottom=25),
                content=ft.Column(
                    spacing=2,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text(
                                    value=self.cars.get("models"),
                                    color=ft.Colors.WHITE,
                                    font_family="PoppinsSemiBold",
                                    size=40,
                                    style=ft.TextStyle(letter_spacing=-1)
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.STAR_OUTLINE,
                                    icon_color=ft.Colors.WHITE,
                                    icon_size=30,
                                    style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT),
                                    on_click=lambda e: [
                                        setattr(e.control, "icon", ft.Icons.STAR if e.control.icon == ft.Icons.STAR_OUTLINE else ft.Icons.STAR_OUTLINE),
                                        e.control.update()
                                    ]
                                )
                            ]
                        ),
                        ft.Text(
                            value=f"${self.cars.get('price')}/day",
                            color=ft.Colors.WHITE,
                            size=25,
                            font_family="PoppinsRegular",
                        ),
                        ft.Divider(height=15, color=ft.Colors.TRANSPARENT),
                        ft.Text(
                            value="Description",
                            color=ft.Colors.WHITE,
                            size=25,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            value="Wanna ride the coolest sport car in the\nworld?",
                            color=ft.Colors.WHITE,
                            size=18,
                            text_align=ft.TextAlign.LEFT
                        ),
                        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                        ft.CupertinoButton(
                            content=ft.Text(
                                value="Book Now",
                                color=ft.Colors.BLACK,
                                font_family="PoppinsSemiBold",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                style=ft.TextStyle(letter_spacing=-1),

                            ),
                            width=page.window.width,
                            height=50,
                            bgcolor=ft.Colors.WHITE
                        )
                    ]
                )
            )
        )


        self.controls = [
            self.__header,
            self.__image,
            self.__bottom_sheet
        ]
