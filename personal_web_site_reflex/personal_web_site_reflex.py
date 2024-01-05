import reflex as rx
import personal_web_site_reflex.styles.styles as styles
from personal_web_site_reflex.components.navbar import navbar
from personal_web_site_reflex.components.footer import footer
from personal_web_site_reflex.views.header.header import header
from personal_web_site_reflex.views.links.links import links
from personal_web_site_reflex.styles.styles import Size


# class State(rx.State):
#     pass


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title="YharyArias | Soy Machine Learning y profe de programación",
    description="Hola, mi nombre es Yhary Arias. Soy ingeniera de sistemas, magister en AI, creadora de ELIA y a veces profe de programación.",
    image="logo_blanco.png"
)
app.compile()
