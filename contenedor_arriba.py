
# BARRA ARRIBA (TITULO)------------------------------------------------------------------------------------------
import flet as ft
import colors_app

app_name = "Laboral - RRHH"

c_up = ft.Container(
    bgcolor=colors_app.bg_title_color,
    width= 560,
    height = 40,
    border_radius= 10,
    padding= ft.padding.symmetric(10, 10),
    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=5,
        color=colors_app.cont_titlle_shadow,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID,
    ),
    content= ft.Text(
        value= app_name,
        size= 15,
        font_family="Calibri Light",
        color= colors_app.title_color),
    alignment= ft.alignment.center,
    visible= True
)
