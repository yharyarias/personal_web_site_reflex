import reflex as rx
from personal_web_site_reflex.styles.styles import Size as Size


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(title, font_weight="bold", color="blue"),
        f" {body}", font_size=Size.MEDIUM.value
    )