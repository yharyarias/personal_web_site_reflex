import reflex as rx
from personal_web_site_reflex.components.navbar import navbar
from personal_web_site_reflex.components.footer import footer
from personal_web_site_reflex.views.header.header import header
from personal_web_site_reflex.views.links.links import links
import personal_web_site_reflex.styles.styles as styles
from personal_web_site_reflex.styles.styles import Size as Size


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value
            )
        ),
        footer()
    )

app = rx.App()
app.add_page(index) 
app.compile()  
