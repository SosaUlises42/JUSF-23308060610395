import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Eventos"
    page.horizontal_alignment = "CENTER"
    page.bgcolor = "#0B1440"
    
    titulo = ft.Text(
        value="Agenda Digital",
        size=40,
        color=ft.Colors.WHITE,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    )

    div = ft.Divider(height=10, thickness=2, color=ft.Colors.WHITE)

    subtitle = ft.Text(
        value="Ingresa aqui los datos",
        size=25,
        color=ft.Colors.WHITE,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    )
    
    eventtoN = ft.TextField(
        label="Evento",
        hint_text="Ingresa aqui tu Evento",
        value="",
        max_length=50,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.WHITE_10,
        border_color=ft.Colors.WHITE,
        on_change=lambda e: print(e.control.value),
        on_submit=lambda e: print("Enter presionado")
    )

    select = ft.Dropdown(
        label="Tipo de evento",
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLACK,
        border_color=ft.Colors.WHITE,
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunion"),
        ]
    )
    
    mod = ft.Text(
        value="Modalidad",
        size=20,
        color=ft.Colors.WHITE,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    )
    
    mod2 = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Presencial", label="Presencial", label_style = ft.TextStyle(color = "white")),
            ft.Radio(value="Virtual", label="Virtual", label_style = ft.TextStyle(color = "white")),
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        expand=True),
        value="Presencial",
        on_change=lambda e: print(f"Seleccionado: {e.control.value}")
    )
    
    pregunta = ft.Text(
        value="Requiere Inscripcion Previa",
        size=20,
        color=ft.Colors.WHITE,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    )
    
    grupo = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Si", label="Si", label_style = ft.TextStyle(color = "white")),
            ft.Radio(value="No", label="No", label_style = ft.TextStyle(color = "white")),
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        expand=True),
        value="No",
        on_change=lambda e: print(f"Seleccionado: {e.control.value}")
    )
    
    duracion = ft.Text(
        value="Duracion del evento (En horas)",
        size=20,
        color=ft.Colors.WHITE,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    )
    
    slider = ft.Slider(
        min=0,
        max=8,
        divisions=8,
        value=1,
        label="{value}",
        on_change=lambda e: print(f"Seleccionado: {e.control.value}")
    )

    reg = ft.Row(
        controls=[
            ft.Column([
                subtitle,
                eventtoN,
                select,
                mod,
                mod2,
                pregunta,
                grupo,
                duracion,
                slider
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER),
            ft.Column([ft.Image(
                src="https://pixelz.cc/wp-content/uploads/2023/12/open-ai-chat-gpt-logo-uhd-4k-wallpaper.jpg",
                width=800,
                height=500,
                border_radius=ft.BorderRadius.all(10),
                repeat=ft.ImageRepeat.NO_REPEAT
            )],
            width = 800,
            alignment=ft.MainAxisAlignment.END)
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        spacing=10,
        wrap=False
    )

    div2 = ft.Divider(height=10, thickness=2, color=ft.Colors.WHITE)

    subtitle2 = ft.Text(
        value="Descripcion del evento",
        size=25,
        color=ft.Colors.WHITE,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    )

    
    page.add(
        titulo,
        div,
        reg,
        div2,
        subtitle2
    )


ft.run(main)