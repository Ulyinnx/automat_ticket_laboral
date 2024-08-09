import flet as ft

import contenedor_informativo
import colors_app

date_button_inicio = ft.ElevatedButton(
    "Inicio",
    icon=ft.icons.CALENDAR_MONTH,
    on_click=lambda _: contenedor_informativo.calendario_inicio.pick_date(),
    expand=True,
    color= colors_app.tex_button_color,
    bgcolor= colors_app.bg_button_color,
    icon_color= colors_app.icon_button_color,
    disabled= True
)
date_button_fin = ft.ElevatedButton(
    "Final ",
    icon=ft.icons.CALENDAR_MONTH,
    on_click=lambda _: contenedor_informativo.calendario_fin.pick_date(),
    expand=True,
    color=colors_app.tex_button_color,
    bgcolor=colors_app.bg_button_color,
    icon_color=colors_app.icon_button_color,
    disabled= True

)

# #### BOTON CARGA / GUARDA #### #

carga_doc_button_1 = ft.ElevatedButton(
    " Cargar Tickets",
    icon=ft.icons.UPLOAD_FILE,
    on_click=lambda _: contenedor_informativo.picador_doc_carga_1.pick_files(),
    expand=True,
    color=colors_app.tex_button_color,
    bgcolor=colors_app.bg_button_color,
    icon_color=colors_app.icon_button_color
)

carga_doc_button_2 = ft.ElevatedButton(
    " Cargar Nomina",
    icon=ft.icons.UPLOAD_FILE,
    on_click=lambda _: contenedor_informativo.picador_doc_carga_2.pick_files(),
    expand=True,
    color=colors_app.tex_button_color,
    bgcolor=colors_app.bg_button_color,
    icon_color=colors_app.icon_button_color
)

guarda_doc_button = ft.ElevatedButton(
    "Guardar ",
    icon=ft.icons.SAVE_AS_OUTLINED,
    on_click=lambda _: contenedor_informativo.picador_doc_guarda.save_file(),
    expand=True,
    color=colors_app.tex_button_color,
    bgcolor=colors_app.bg_button_color,
    icon_color=colors_app.icon_button_color
)

valor_boleto_button = ft.ElevatedButton(
    "Valor Boleto",
    expand=True,
    icon=ft.icons.DIRECTIONS_BUS_ROUNDED,
    on_click= contenedor_informativo.animate_vboleto,
    color=colors_app.tex_button_color,
    bgcolor=colors_app.bg_button_color,
    icon_color=colors_app.icon_button_color
    )


eject_button = ft.ElevatedButton(
    "Ejecutar",
    expand=True,
    icon=ft.icons.PLAY_CIRCLE_FILLED_OUTLINED,
    on_click= contenedor_informativo.animate_eject,
    color=colors_app.tex_button_color,
    bgcolor=colors_app.bg_button_color,
    icon_color=colors_app.icon_button_color
    )


#BARRA IZQUIERDA CON BOTONERA (LAYOUT)----------------------------------------------------------------------------------

b_side = ft.Column(
    controls= [
        ft.Row(
            controls= [ft.ElevatedButton(
                "Reporte",
                expand= True,
                color=colors_app.tex_button_color,
                bgcolor=colors_app.bg_button_color,
                icon_color=colors_app.icon_button_color
            )]
        ),
        ft.Row(
            controls=[date_button_inicio]
        ),
        ft.Row(
            controls=[date_button_fin]
        ),
        ft.Row(
            controls=[carga_doc_button_1]
        ),
        ft.Row(
            controls=[carga_doc_button_2]
        ),
        ft.Row(
            controls=[guarda_doc_button]
        ),
        ft.Row(
            controls= [valor_boleto_button]
        ),
        ft.Row(
            controls=[eject_button]
        )
    ],
    expand= True
)

c_side = ft.Container(
    bgcolor=colors_app.cont_color,
    width=200,
    height=400,
    border_radius=10,
    padding=ft.padding.symmetric(10, 10),
    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=5,
        color=colors_app.cont_shadow_color,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID,
    ),
    content= b_side
)
