import logging
import flet as ft
import warnings

warnings.filterwarnings(action="ignore")
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("flet_core").setLevel(logging.INFO)

from views.splash import Splash
from views.detail import Detail
from views.home import Home


def main(page: ft.Page) -> None:
    page.window.width = 355
    page.window.height = 680
    page.window.always_on_top = True
    page.padding = 0
    page.margin = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    print(page.width, page.height)
    page.fonts = {
        "PoppinsSemiBold": "/fonts/poppins/Poppins-SemiBold.ttf",
        "PoppinsRegular": "/fonts/poppins/Poppins-Regular.ttf",
    }
    page.theme = ft.Theme(
        system_overlay_style=ft.SystemOverlayStyle(
            status_bar_color=ft.Colors.WHITE
        )
    )
    def router(_) -> None:
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(Splash(page))
            case "/home":
                page.views.append(Home(page))
            case "/detail":
                page.views.append(Detail(page))
            case _:
                page.views.append(Splash(page))
        page.update()

    page.on_route_change = router
    page.update()
    page.go("/")


ft.app(main, assets_dir="assets")
