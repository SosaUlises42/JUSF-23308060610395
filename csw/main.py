import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Eventos"
    page.horizontal_alignment = "CENTER"
    page.bgcolor = "#0f0f1b"
    
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
            ft.Radio(value="Si", label="Si"),
            ft.Radio(value="No", label="No"),
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        expand=True),
        value="No",
        on_change=lambda e: print(f"Seleccionado: {e.control.value}")
    )

    reg = ft.Row(
        controls=[
            ft.Column([
                subtitle,
                eventtoN,
                select,
                pregunta,
                grupo
            ],
            expand=True),
            ft.Column([ft.Image(
                src="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/377055240/original/263612bb28d57c90594c01833617f9b14df09ea4/develop-ai-agent-llama3-openai-sora-whisper-ai-bot-text-to-speech-ai-model.jpeg",
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