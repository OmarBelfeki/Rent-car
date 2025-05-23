import flet as ft

slides: list[dict] = [
    {
        "id": 1,
        "image": "https://picsum.photos/200/200?1",
        "title": "Find Your Vehicle",
        "text": "Find the perfect vehicle for every\noccasion!"
    },
    {
        "id": 2,
        "image": "https://picsum.photos/200/200?2",
        "title": "Find Your Vehicle",
        "text": "Find the perfect vehicle for every\noccasion!"
    },
    {
        "id": 3,
        "image": "https://picsum.photos/200/200?3",
        "title": "Find Your Vehicle",
        "text": "Find the perfect vehicle for every\noccasion!"
    },
    {
        "id": 4,
        "image": "https://picsum.photos/200/200?4",
        "title": "Find Your Vehicle",
        "text": "Find the perfect vehicle for every\noccasion!"
    }
]


class Swiper(ft.Container):
    def __init__(
            self,
            page: ft.Page,
            width: int,
            height: int
    ) -> None:
        self.__width = width
        self.__height = height
        super().__init__()
        self.swiper: float = 0.0
        self.width = page.window.width
        self.height = page.window.height
        self.bgcolor = "white"



        self.swipe = ft.Row(
            width=page.window.width,
            scroll=ft.ScrollMode.HIDDEN,
            on_scroll=self.scroll,
            controls=[
                self.slide(
                    image=slides[i].get("image"),
                    title=slides[i].get("title"),
                    text=slides[i].get("text"),
                )
                for i in range(len(slides))
            ]
        )

        self.swi = ft.Container(
            width=50,
            height=50,
            bgcolor="black",
            alignment=ft.alignment.center,
            margin=ft.margin.only(left=100),
        )

        self.content = ft.Column(
            [
                self.swi,
                self.swipe
            ]
        )

    def scroll(self, e: ft.OnScrollEvent) -> None:
        if e.event_type == "user":
            self.swiper = e.pixels
            print("direction", e.direction)
        if e.event_type == "update":
            if e.pixels > self.swiper:
                self.swi.margin = ft.margin.only(right=e.pixels)
                self.swi.update()
            if e.pixels < self.swiper:
                self.swi.margin = ft.margin.only(right=e.pixels)
                self.swi.update()

    def slide_update(self, e: ft.DragUpdateEvent) -> None:
        print(e.local_x)
        if self.swiper > 100:
            if e.local_x > self.swiper:
                self.swi.margin = ft.margin.only(right=e.local_x)
            if e.local_x < self.swiper:
                self.swi.margin = ft.margin.only(left=e.local_x)
        else:
            if e.local_x < self.swiper:
                self.swi.margin = ft.margin.only(right=e.local_x)
            if e.local_x > self.swiper:
                self.swi.margin = ft.margin.only(left=e.local_x)
        self.swi.update()



    def slide(
            self,
            image: str,
            title: str,
            text: str,
            pag: bool = False
    ) -> ft.Column:
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(
                    src=image,
                    width=self.__width,
                    height=300,
                    fit=ft.ImageFit.CONTAIN,
                    border_radius=ft.border_radius.all(10),

                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=2,
                    controls=[
                        ft.Container(
                            key="i",
                            bgcolor="#fa7f35" if pag else "#fed9c2",
                            width=12,
                            height=3.86,
                            border_radius=ft.border_radius.all(value=15)
                        ),
                        ft.Container(
                            key="i",
                            bgcolor="#fa7f35" if pag else "#fed9c2",
                            width=12,
                            height=3.86,
                            border_radius=ft.border_radius.all(value=15)
                        ),
                        ft.Container(
                            key="i",
                            bgcolor="#fa7f35" if pag else "#fed9c2",
                            width=12,
                            height=3.86,
                            border_radius=ft.border_radius.all(value=15)
                        ),
                        ft.Container(
                            key="i",
                            bgcolor="#fa7f35" if pag else "#fed9c2",
                            width=12,
                            height=3.86,
                            border_radius=ft.border_radius.all(value=15)
                        )
                    ]
                ),
                ft.Text(
                    value=title,
                    font_family="PoppinsSemiBold",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    style=ft.TextStyle(
                        letter_spacing=-0.5,
                    ),
                ),
                ft.Text(
                    value=text,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                )
            ]
        )
