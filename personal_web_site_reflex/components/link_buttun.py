import reflex as rx
import personal_web_site_reflex.styles.styles as styles
from personal_web_site_reflex.styles.styles import Size as Size
from personal_web_site_reflex.styles.styles import Color as Color

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, styles=styles.button_body_style),
                    align_items="start",
                    spacing=Size.SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width="100%"
                
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )
