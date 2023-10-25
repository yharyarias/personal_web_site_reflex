import reflex as rx
import datetime
from personal_web_site_reflex.styles.styles import Size as Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            "Personal Blog yharyarias",
            href="https://medium.com/@yharystefa",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            f"© {datetime.date.today().year} yharyarias by Yhary Arias. Building software with love from Bucaramanga to the world.",
            font_size=Size.MEDIUM.value,
            margin_top="0px !important"
        ),
        margin_bottom=Size.BIG.value
    )
    