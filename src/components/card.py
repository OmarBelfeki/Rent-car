import flet as ft


class Card(ft.Container):
    def __init__(
        self,
        width: int,
        height: int,
        model: str,
        price: float,
        bgcolor: str,
        image: str,
        #on_click: Callable
    ):
        self.__width = width
        self.__height = height
        self.__model = model
        self.__price = price
        self.__bgcolor = bgcolor
        self.__image = image
        #self.__on_click = on_click
        super().__init__()
        #self.bgcolor = self.__bgcolor
        #self.width = page.window.width * 0.9
        self.height = 180
        self.border_radius = ft.border_radius.all(value=10)
        #self.padding = ft.padding.only(top=20, left=20)
        self.on_click = lambda e: [
            e.page.session.set("micanic", {
                "header_title": "Cars",
                "image": self.__image,
                "models": self.__model,
                "price": self.__price,
                "bgcolor": self.__bgcolor,
                "back": "/"
            }),
            e.page.go("/detail")
        ]

        self.model = ft.Text(
            value=self.__model,
            color=ft.Colors.WHITE,
            font_family="PoppinsSemiBold",
            size=24,
            style=ft.TextStyle(letter_spacing=-0.5),
        )

        self.price = ft.Text(
            value=f"${self.__price}/day",
            color=ft.Colors.WHITE,
            font_family="PoppinsRegular",
            size=14,
            top=40
        )

        self._image = ft.Image(
            src=self.__image,
            scale=0.9,
            top=45,
            left=140,
        )

        self.content = ft.Stack(
            controls=[
                ft.Container(
                    bgcolor=self.__bgcolor,
                    width=self.__width * 0.9,
                    border_radius=ft.border_radius.all(value=10),
                    padding = ft.padding.only(top=20, left=20),
                    height=130,
                    content=ft.Stack(
                        controls=[
                            self.model,
                            self.price,
                            ft.IconButton(
                                icon=ft.Icons.STAR_OUTLINE,
                                icon_color=ft.Colors.WHITE,
                                style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT),
                                top=65,
                                left=-6,
                                on_click=lambda e: [
                                    setattr(e.control, "icon", ft.Icons.STAR if e.control.icon == ft.Icons.STAR_OUTLINE else ft.Icons.STAR_OUTLINE),
                                    e.control.update()
                                ]
                            )
                        ]
                    )
                ),
                self._image
            ]
        )
