import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            "Personal Blog yharyarias",
            href="https://medium.com/@yharystefa",
            is_external=True
            ),
        rx.text(f"© {datetime.date.today().year} yharyarias by Yhary Arias. Building software with love from Bucaramanga to the world.")
    )