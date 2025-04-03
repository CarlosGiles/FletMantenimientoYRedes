# FletMantenimientoYRedes/src/interfaz.py

import flet as ft
import threading
import os
from mantenimiento import (
    borrar_temp_windows,
    borrar_temp_local,
    configurar_dhcp,
    configurar_ip_estatica,
    vaciar_papelera
)

def main(page: ft.Page):
    page.icon = "assets/tech_icon.png"
    page.title = "Mantenimiento y Configuración de Red"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.DARK # si no se agrega toma el del sistema

    # Configuración de la ventana
    page.window_maximized = False
    page.window_resizable = False
    page.window_width = 800
    page.window_height = 600
    page.window_min_width, page.window_max_width = 800, 800
    page.window_min_height, page.window_max_height = 600, 600

    # Texto para mostrar resultados
    resultado_text = ft.Text(value="", selectable=True)

    # Funciones de callback (en hilos)
    def on_borrar_temp_windows(e):
        def run():
            mensaje = borrar_temp_windows()
            resultado_text.value = mensaje
            page.update()
        threading.Thread(target=run).start()

    def on_borrar_temp_local(e):
        def run():
            mensaje = borrar_temp_local()
            resultado_text.value = mensaje
            page.update()
        threading.Thread(target=run).start()

    def on_configurar_dhcp(e):
        def run():
            mensaje = configurar_dhcp("Wi-Fi")
            resultado_text.value = mensaje
            page.update()
        threading.Thread(target=run).start()

    def on_configurar_ip_hogar(e):
        def run():
            mensaje = configurar_ip_estatica(
                "Wi-Fi", "192.168.1.200", "255.255.255.0", "192.168.1.254", "192.168.1.250"
            )
            resultado_text.value = mensaje
            page.update()
        threading.Thread(target=run).start()

    def on_configurar_ip_oficina(e):
        def run():
            mensaje = configurar_ip_estatica(
                "Ethernet", "192.168.100.200", "255.255.255.0", "192.168.100.1", "8.8.8.8"
            )
            resultado_text.value = mensaje
            page.update()
        threading.Thread(target=run).start()

    def on_vaciar_papelera(e):
        def run():
            mensaje = vaciar_papelera()
            resultado_text.value = mensaje
            page.update()
        threading.Thread(target=run).start()

    # Manejador de evento para cierre de ventana
    def on_window_event(e):
        if e.data == "close":
            page.window_destroy()
    
    page.on_window_event = on_window_event

    # Estilo de botón para un aspecto más limpio
    button_style = {
        "width": 450,
        "bgcolor": "#1E1E1E",
        "color": "white",
        "style": ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            elevation=0,
            side=ft.BorderSide(1, "white24"),
        ),
    }

    # Título principal
    titulo = ft.Text(
        "Mantenimiento y Configuración de Red", 
        size=24, 
        weight=ft.FontWeight.BOLD
    )

    # Botones con estilo uniforme y texto alineado a la izquierda
    botones = [
        ft.ElevatedButton(
            content=ft.Row(
                [ft.Text("1. Eliminar archivos temporales (C:\\Windows\\Temp)")],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            on_click=on_borrar_temp_windows,
            width=450,
            bgcolor="#1E1E1E",
            color="white",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                elevation=0,
                side=ft.BorderSide(1, "white24"),
            )
        ),
        ft.ElevatedButton(
            content=ft.Row(
                [ft.Text("2. Eliminar archivos temporales locales (%LOCALAPPDATA%\\Temp)")],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            on_click=on_borrar_temp_local,
            width=450,
            bgcolor="#1E1E1E",
            color="white",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                elevation=0,
                side=ft.BorderSide(1, "white24"),
            )
        ),
        ft.ElevatedButton(
            content=ft.Row(
                [ft.Text("3. Configurar IP dinámica (DHCP)")],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            on_click=on_configurar_dhcp,
            width=450,
            bgcolor="#1E1E1E",
            color="white",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                elevation=0,
                side=ft.BorderSide(1, "white24"),
            )
        ),
        ft.ElevatedButton(
            content=ft.Row(
                [ft.Text("4. Asignar IP estática - Hogar (192.168.1.200)")],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            on_click=on_configurar_ip_hogar,
            width=450,
            bgcolor="#1E1E1E",
            color="white",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                elevation=0,
                side=ft.BorderSide(1, "white24"),
            )
        ),
        ft.ElevatedButton(
            content=ft.Row(
                [ft.Text("5. Asignar IP estática - Oficina (192.168.100.200)")],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            on_click=on_configurar_ip_oficina,
            width=450,
            bgcolor="#1E1E1E",
            color="white",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                elevation=0,
                side=ft.BorderSide(1, "white24"),
            )
        ),
        ft.ElevatedButton(
            content=ft.Row(
                [ft.Text("6. Vaciar Papelera de reciclaje")],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            on_click=on_vaciar_papelera,
            width=450,
            bgcolor="#1E1E1E",
            color="white",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                elevation=0,
                side=ft.BorderSide(1, "white24"),
            )
        ),
    ]

    # Columna izquierda con opciones
    columna_opciones = ft.Column(
        controls=[titulo, ft.Divider()] + botones + [ft.Divider(), resultado_text],
        spacing=10,
        expand=True,
        alignment=ft.MainAxisAlignment.START,
    )

    # Contenedor para la imagen alineada con los botones
    contenedor_imagen = ft.Container(
        content=ft.Image(
            src="src/assets/tech.png",
            width=300,
            height=300,
            fit=ft.ImageFit.CONTAIN
        ),
        alignment=ft.alignment.top_center,  # Alineación superior
        margin=ft.margin.only(top=40),      # Margen superior para alinear con botones
        opacity=0.7,                        # Añadida transparencia a la imagen
    )

    # Row principal que contiene ambos elementos
    layout = ft.Row(
        controls=[
            # Columna opciones a la izquierda
            ft.Container(
                content=columna_opciones,
                expand=6,
                padding=10
            ),
            # Imagen a la derecha
            ft.Container(
                content=contenedor_imagen,
                expand=4,
                padding=10,
                alignment=ft.alignment.top_center  # Alineación superior
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.START  # Alineación superior para toda la fila
    )

    # Contenedor principal con padding
    main_container = ft.Container(
        content=layout,
        expand=True,
        padding=15,
        bgcolor="#121212"
    )

    page.add(main_container)
    page.update()