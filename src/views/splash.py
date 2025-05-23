from typing import Optional, Callable

import flet as ft

slides: list[dict] = [
    {
        "image": "/images/splash/1.png",
        "title": "Find Your Vehicle",
        "text": "Find the perfect vehicle for every\noccasion!",
    },
    {
        "image": "/images/splash/Beep Beep Sightseeing.png",
        "title": "Your dream Car",
        "text": "Rent the car you’ve always\nwanted to drive.!"
    },
    {
        "image": "/images/splash/Beep Beep Fast Delivery.png",
        "title": "Small Ones Too!",
        "text": "Rent a small vehicle for those\nshort distances"
    },
    {
        "image": "/images/splash/Beep Beep Location.png",
        "title": "Find Our Stations",
        "text": "Find your nearest station to rent\nyour car!"
    },
]


class Splash(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/splash"

        self.bgcolor = ft.Colors.WHITE
        self.width = page.window.width
        self.height = page.window.height

        self.header = ft.AppBar(
            title=ft.Text(
                value="Beepy",
                color=ft.Colors.BLACK,
                font_family="PoppinsSemiBold",
                weight=ft.FontWeight.BOLD,
                size=20,
                style=ft.TextStyle(
                    letter_spacing=-0.5,
                    height=22.5
                ),
            ),
            bgcolor=ft.Colors.WHITE,
            center_title=True
        )

        c1 = ft.Container(
            content=self.slide(page, **slides[0]),
            alignment=ft.alignment.center,
            width=200,
            height=200,
        )
        c2 = ft.Container(
            content=self.slide(page, **slides[1]),
            alignment=ft.alignment.center,
            width=200,
            height=200,
        )
        c3 = ft.Container(
            content=self.slide(page, **slides[2]),
            alignment=ft.alignment.center,
            width=200,
            height=200,
        )
        c4 = ft.Container(
            content=self.slide(page, **slides[3]),
            alignment=ft.alignment.center,
            width=200,
            height=200,
        )

        c = ft.AnimatedSwitcher(
            c1,
            width=self.width,
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=ft.AnimationCurve.EASE,
            switch_out_curve=ft.AnimationCurve.EASE,
        )

        def fade(e):
            if c.content == c1:
                c.content = c2
            elif c.content == c2:
                c.content = c3
            elif c.content == c3:
                c.content = c4
            elif c.content == c4:
                c.content = c1
            c.update()

        self.btns = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.btn("skip", route="/home"),
                self.btn("continue", route="/home"),
                self.btn("next", click=fade),

            ]
        )

        self.controls = [
            self.header,
            c,
            ft.Divider(height=60, color=ft.Colors.TRANSPARENT),
            self.btns

        ]

    def btn(self, value: str, route: Optional[str] = None, click: Optional[Callable] = None) -> ft.Container:
        return ft.Container(
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=self.height * 0.3),
            content=ft.CupertinoButton(
                content=ft.Text(
                    value=value,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.WHITE,
                    style=ft.TextStyle(letter_spacing=0.4),
                    width=100,
                    size=15
                ),
                height=60,
                width=self.width * 0.29,
                bgcolor="#fa7f35",
                alignment=ft.alignment.center,
                on_click=click if click else lambda e: e.page.go(route)
            )
        )

    def slide(
            self,
            page: ft.Page,
            image: str,
            title: str,
            text: str,
            pag: bool = False
    ) -> ft.Column:
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.Image(
                    src=image,
                    height=300,
                    fit=ft.ImageFit.CONTAIN,
                    width=page.window.width,
                    scale=1.5,
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
                    size=23,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.RIGHT,
                    style=ft.TextStyle(
                        letter_spacing=-0.5,
                    ),
                ),
                ft.Container(
                    margin=ft.margin.symmetric(horizontal=-40),
                    content=ft.Text(
                        value=text,
                        size=16,
                        weight=ft.FontWeight.W_400,
                        width=self.width,
                        text_align=ft.TextAlign.CENTER
                    )
                )
            ]
        )
