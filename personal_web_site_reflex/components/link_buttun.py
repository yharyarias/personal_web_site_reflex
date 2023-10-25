import reflex as rx
import personal_web_site_reflex.styles.styles as styles

def link_buttun(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_forward",
                    width=styles.Size.BIG.value,
                    height=styles.Size.DEFAULT.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, styles=styles.button_body_style),
                    align_items="start"
                )
                
            )
        ),
        href=url,
        is_external=True,
        width="100%"

    )