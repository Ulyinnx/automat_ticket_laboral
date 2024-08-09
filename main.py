import flet as ft

# IMPORTACION DE MODULOS
import contenedor_arriba
import contenedor_izquierda
import contenedor_informativo
import colors_app

def main(page: ft.Page):

# TITULO---------------------------------------------------------------------------------------------------------------
    page.title = contenedor_arriba.app_name

## SETEO DE CONFIGURACIONES---------------------------------------------------------------------------------------------
    # page.window_focused = True
    page.bgcolor = colors_app.bg_page_color
    page.window.width = 600
    page.window.height = 510
    page.window.resizable = False

## INICIO DE COMPLEMENTOS/CONTROLES-------------------------------------------------------------------------------------

    page.overlay.append(contenedor_informativo.calendario_inicio)
    page.overlay.append(contenedor_informativo.calendario_fin)

    page.overlay.append(contenedor_informativo.banner)

    page.overlay.append(contenedor_informativo.picador_doc_carga_1)
    page.overlay.append(contenedor_informativo.picador_doc_carga_2)
    page.overlay.append(contenedor_informativo.picador_doc_guarda)

    page.update()

    layout_principal = ft.Column(
        controls=[
            ft.Row(controls=[contenedor_arriba.c_up]),
            ft.Row(controls=[contenedor_izquierda.c_side, contenedor_informativo.c_central])
        ],
        expand=1,
    )

    page.add(layout_principal)

ft.app(target=main)

