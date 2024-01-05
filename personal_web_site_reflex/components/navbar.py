import reflex as rx
import personal_web_site_reflex.styles.styles as styles
from personal_web_site_reflex.styles.styles import Size
from personal_web_site_reflex.styles.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("Yhary", color=Color.PRIMARY.value),
            rx.span("Arias", color=Color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
