import flet as ft

import colors_app


import time
import os

container_base_2 = ft.Container(
    content=ft.Text(
        value= "- Panel Informativo - ",
        size= 15,
        font_family="Calibri Light",
        color= colors_app.title_color),
    alignment=ft.alignment.center,
    width=600,
    height=35,
    border_radius=15,
    bgcolor= ft.colors.BLUE_GREY_600
)

container_base = ft.Container(
    alignment=ft.alignment.center,
    width=600,
    height=31,
    border_radius=15,
    # bgcolor= ft.colors.BLUE_GREY_600
)

######---------------------------------------------------------

progres_bar_eject = ft.ProgressBar(value= 0,
                                   width=400,
                                   color=ft.colors.BLUE_400,
                                   disabled= True)
tex_eject =ft.Text(
        value= "- Proceso Finalizado -",
        size= 15,
        font_family="Calibri Light",
        disabled= False)

con_eject = ft.Container(
    content= progres_bar_eject,
    bgcolor=colors_app.cont_sec_color,
    alignment=ft.alignment.center,
    width=600,
    height=31,
    border_radius=15,
    offset=ft.transform.Offset(-2, 0),
    animate_offset=ft.animation.Animation(500),
    opacity= 1,
    animate_opacity= ft.animation.Animation(duration= 1000),
    shadow=ft.BoxShadow(
        spread_radius=0.5,
        blur_radius=1,
        color=colors_app.cont_sec_shadow_color,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID
    ),
)
con_eject_finish = ft.Container(
    content= tex_eject,
    bgcolor=colors_app.cont_sec_color,
    alignment=ft.alignment.center,
    width=600,
    height=31,
    border_radius=15,
    offset=ft.transform.Offset(-2, 0),
    animate_offset=ft.animation.Animation(500),
    opacity= 1,
    shadow=ft.BoxShadow(
        spread_radius=0.5,
        blur_radius=1,
        color=colors_app.cont_sec_shadow_color,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID
    ),
)
def show_banner_click(e):
    banner.content = ft.Text(e)
    banner.open = True
    banner.update()

def close_banner(e):
    banner.open = False
    banner.update()

banner = ft.Banner(
    bgcolor=ft.colors.RED_400,
    leading=ft.Icon(
        ft.icons.WARNING_AMBER_ROUNDED,
        color=ft.colors.BLACK54,
        size=40),
    content=ft.Text("Error"),
    force_actions_below=True,
    actions=[
        ft.TextButton("Cerrar",
                      on_click=close_banner),
    ],
)

def animate_eject_error(e):
    progres_bar_eject.color = ft.colors.RED_500
    progres_bar_eject.update()
    time.sleep(0.5)
    con_eject_finish.offset= ft.transform.Offset(0,0)    # con_eject_finish.update()
    con_eject_finish.update()
    show_banner_click(e)


def animate_eject_2(e):
    progres_bar_eject.color = ft.colors.GREEN_500
    progres_bar_eject.update()
    time.sleep(0.5)
    con_eject_finish.offset= ft.transform.Offset(0,0)    # con_eject_finish.update()
    con_eject_finish.update()


def animate_eject(e):
    if con_carga_path_1.offset == ft.transform.Offset(0, 0) and con_carga_path_2.offset == ft.transform.Offset(0, 0):
        if input_text_boleto.value != '' and con_guarda_path.offset == ft.transform.Offset(0, 0):
            if con_eject.offset == ft.transform.Offset(-2,0):
                con_eject.offset = ft.transform.Offset(0, 0)
                con_eject.update()
                time.sleep(0.8)

            import random
            numeros = [10,15, 20, 30, 35, 40, 50, 55, 60, 70, 80, 85, 90]
            valor_aleatorio = random.choice(numeros)
            for i in range(0, valor_aleatorio):
                progres_bar_eject.value = i * 0.01
                time.sleep(0.05)
                progres_bar_eject.update()
            try:
                import procesa_tickets
                procesa_tickets.fun_procesa_tickets(
                    carga_1 = carga_path_1.value,
                    carga_2 = carga_path_2.value,
                    guarda = guarda_path.value,
                    vboleto = input_text_boleto.value)
                for i in range(valor_aleatorio, 101):
                    progres_bar_eject.value = i * 0.01
                    time.sleep(0.05)
                    progres_bar_eject.update()

                time.sleep(0.8)
                animate_eject_2(e)

            except Exception as e:

                for i in range(valor_aleatorio, 101):
                    progres_bar_eject.value = i * 0.01
                    time.sleep(0.05)
                    progres_bar_eject.update()

                animate_eject_error(e)
                tex_eject.value = "- Error durante el proceso -"
                tex_eject.update()



######---------------------------------------------------------
def animate_vboleto_2(e):
    valor_boleto.opacity = 0 if valor_boleto.opacity == 1 else 1
    valor_boleto.update()
    time.sleep(0.3)
    valor_boleto.opacity = 1 if valor_boleto.opacity == 0 else 0
    valor_boleto.update()


def animate_vboleto(e):
    valor_boleto.offset = ft.transform.Offset(0, 0)
    valor_boleto.update()

input_text_boleto = ft.TextField(
    hint_text="Valor Boleto (solo números)",
    content_padding= 10,
    text_size= 13,
    text_align= "CENTER",
    color = ft.colors.BLACK54,
    border_color= "transparent",
    on_submit= animate_vboleto_2,
)

valor_boleto = ft.Container(
    content= input_text_boleto,
    bgcolor=colors_app.cont_sec_color,
    alignment=ft.alignment.center,
    width=600,
    height=31,
    border_radius=15,
    offset=ft.transform.Offset(-2, 0),
    animate_offset=ft.animation.Animation(500),
    opacity= 1,
    animate_opacity= ft.animation.Animation(duration= 500),
    shadow=ft.BoxShadow(
        spread_radius=0.5,
        blur_radius=1,
        color=colors_app.cont_sec_shadow_color,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID
    )
)



# ------------------------------------------  CARGA / GUARDA - FUNCIONES--------------------------------------------
carga_path_2 = ft.Text("N/A", size=10, color="Black")
carga_path_1 = ft.Text("N/A", size=10, color="Black")
guarda_path = ft.Text("N/A", size=10, color="Black")

def path_picador_2(e: ft.FilePickerResultEvent):
    carga_2 = None
    try:
        carga_2 = os.path.basename(e.files[0].path)
        carga_path_2.value = carga_2
        carga_path_2.update()
    except: None

def path_picador_1(e: ft.FilePickerResultEvent):
    carga = None
    guarda = None
    try:
        carga_1 = os.path.basename(e.files[0].path)
        carga_path_1.value = carga_1
        carga_path_1.update()
    except: None
    try:
        guarda = os.path.basename(e.path)
        guarda_path.value = guarda
        guarda_path.update()
    except: None


def animate_carga_2(e):
    if con_carga_path_2.offset == ft.transform.Offset(-2,0):
        con_carga_path_2.offset = ft.transform.Offset(0, 0)
        con_carga_path_2.update()
    return path_picador_2(e)
def animate_carga_1(e):
    if con_carga_path_1.offset == ft.transform.Offset(-2,0):
        con_carga_path_1.offset = ft.transform.Offset(0, 0)
        con_carga_path_1.update()
    # elif con_carga_path_2.offset == ft.transform.Offset(-2,0):
    #     con_carga_path_2.offset = ft.transform.Offset(0, 0)
    #     con_carga_path_2.update()
    return path_picador_1(e)
def animate_guarda(e):
    if con_guarda_path.offset == ft.transform.Offset(-2,0):
        con_guarda_path.offset = ft.transform.Offset(0, 0)
        con_guarda_path.update()
    return path_picador_1(e)

con_carga_path_2 = ft.Container(
    content=carga_path_2,
    bgcolor=colors_app.cont_sec_color,
    alignment=ft.alignment.center,
    width=600,
    height=30,
    border_radius=15,
    offset=ft.transform.Offset(-2, 0),
    animate_offset=ft.animation.Animation(500),
    shadow=ft.BoxShadow(
        spread_radius=0.5,
        blur_radius=1,
        color=colors_app.cont_sec_shadow_color,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID
    ),
)

con_carga_path_1 = ft.Container(
    content=carga_path_1,
    bgcolor=colors_app.cont_sec_color,
    alignment=ft.alignment.center,
    width=600,
    height=30,
    border_radius=15,
    offset=ft.transform.Offset(-2, 0),
    animate_offset=ft.animation.Animation(500),
    shadow=ft.BoxShadow(
        spread_radius=0.5,
        blur_radius=1,
        color=colors_app.cont_sec_shadow_color,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID
    ),
)

con_guarda_path = ft.Container(
    content=guarda_path,
    bgcolor=colors_app.cont_sec_color,
    alignment=ft.alignment.center,
    width=600,
    height=30,
    border_radius=15,
    offset=ft.transform.Offset(-2, 0),
    animate_offset=ft.animation.Animation(500),
    shadow=ft.BoxShadow(
        spread_radius=0.5,
        blur_radius=1,
        color=colors_app.cont_sec_shadow_color,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID
    ),
)
picador_doc_carga_2 = ft.FilePicker(on_result=animate_carga_2)
picador_doc_carga_1 = ft.FilePicker(on_result=animate_carga_1)
picador_doc_guarda = ft.FilePicker(on_result=animate_guarda)

# ------------------------------------------  DATE - FUNCIONES    ------------------------------------------------------
tex_date_inicio = ft.Text("N/A", size=10, color="Black")
tex_date_fin = ft.Text("N/A", size=10, color="Black")

def date_funcion(e: ft.FilePickerResultEvent):
    inicio = None
    fin = None
    try:
        inicio = calendario_inicio.value.date()
        tex_date_inicio.value = inicio
        tex_date_inicio.update()
    except: None
    try:
        fin = calendario_fin.value.date()
        tex_date_fin.value = fin
        tex_date_fin.update()
    except: None



def animate_date_inicio(e):
    if con_date_inicio.offset == ft.transform.Offset(-2,0):
        con_date_inicio.offset = ft.transform.Offset(0, 0)
        con_date_inicio.update()
    return date_funcion(e)

def animate_date_fin(e):
    if con_date_fin.offset == ft.transform.Offset(-2,0):
        con_date_fin.offset = ft.transform.Offset(0, 0)
        con_date_fin.update()
    return date_funcion(e)

con_date_inicio = ft.Container(
    content=tex_date_inicio,
    bgcolor=colors_app.cont_sec_color,
    alignment=ft.alignment.center,
    width=600,
    height=30,
    border_radius=15,
    offset=ft.transform.Offset(-2, 0),
    animate_offset=ft.animation.Animation(500),
    shadow=ft.BoxShadow(
        spread_radius=0.5,
        blur_radius=1,
        color=colors_app.cont_sec_shadow_color,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID
    ),
)
con_date_fin = ft.Container(
    content=tex_date_fin,
    bgcolor=colors_app.cont_sec_color,
    alignment=ft.alignment.center,
    width=600,
    height=30,
    border_radius=15,
    offset=ft.transform.Offset(-2, 0),
    animate_offset=ft.animation.Animation(500),
    shadow=ft.BoxShadow(
        spread_radius=0.5,
        blur_radius=1,
        color=colors_app.cont_sec_shadow_color,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID
    ),
)

calendario_inicio = ft.DatePicker(
    on_change=animate_date_inicio, on_dismiss= None)

calendario_fin = ft.DatePicker(
    on_change=animate_date_fin, on_dismiss= None)

## CONTENEDOR CENTRAL INFO ---------------------------------------------------------------------------------------------

info_central= \
    ft.Column(
        controls= [
            container_base_2,
            con_date_inicio,
            con_date_fin,
            con_carga_path_1,
            con_carga_path_2,
            con_guarda_path,
            valor_boleto,
            con_eject,
            con_eject_finish,
        ],
        expand= True
    )

c_central = ft.Container(
    bgcolor=colors_app.cont_color,
    width= 350,
    height = 400,
    border_radius= 15,
    padding=ft.padding.symmetric(10, 10),
    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=5,
        color=colors_app.cont_shadow_color,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.SOLID,
    ),
    content= info_central,
)
