import flet as ft


def main(page: ft.Page):
    def mostrar_detalles(e):
        nombre = nombre_input.value
        edad = edad_input.value
        if nombre and edad:
            detalle_text.value = f"Nombre: {nombre}, Edad: {edad}"
            detalle_text.update()
        else:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Advertencia"),
                content=ft.Text("Por favor, introduce el nombre y la edad."),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: page.dialog.close())
                ],
            )
            page.dialog.open = True
            page.update()

    page.title = "Cliente App"

    nombre_input = ft.TextField(label="Nombre")
    edad_input = ft.TextField(label="Edad")
    mostrar_button = ft.ElevatedButton(text="Mostrar Detalles", on_click=mostrar_detalles)
    detalle_text = ft.Text()

    page.add(
        nombre_input,
        edad_input,
        mostrar_button,
        detalle_text,
    )


ft.app(target=main)