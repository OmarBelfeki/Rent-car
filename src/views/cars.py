import flet as ft


cars: list[dict] = [
    {
        "id": 1,
        "model": "Classic Car",
        "price": 34,
        "bgcolor": "#b67853",
        "image": "/images/cars/Beep Beep Medium Vehicle.png"
    },
    {
        "id": 2,
        "model": "Sport Car",
        "price": 55,
        "bgcolor": "#60b5f4",
        "image": "/images/cars/Beep Beep Medium Vehicle-1.png"
    },
    {
        "id": 3,
        "model": "Flying Car",
        "price": 500,
        "bgcolor": "#8382c2",
        "image": "/images/cars/Beep Beep Medium Vehicle-2.png"
    },
    {
        "id": 4,
        "model": "Electric Car",
        "price": 45,
        "bgcolor": "#2a3640",
        "image": "/images/cars/Beep Beep Medium Vehicle-3.png"
    },
]


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
                "back": "/home"
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


class Cars(ft.Container):
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        super().__init__()
        self.bgcolor = ft.Colors.WHITE
        self.width = self.__width
        self.height = self.__height


        self.content = ft.Container(
            margin=ft.margin.only(bottom=150),
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                height=self.__height * 1.9,
                controls=[
                    Card(
                        width=self.__width,
                        height=self.__height,
                        model=i.get("model"),
                        price=i.get("price"),
                        bgcolor=i.get("bgcolor"),
                        image=i.get("image"),

                    )
                    for i in cars
                ]
            )
        )
