import reflex as rx
import datetime
import personal_web_site_reflex.constants as const
from personal_web_site_reflex.styles.styles import Size as Size
from personal_web_site_reflex.styles.colors import Color as Color
from personal_web_site_reflex.styles.colors import TextColor as TextColor



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo_blanco.png",
            height=Size.VERY_BIG.value
        ),
        rx.link(
            rx.box(
                f"© 2020-{datetime.date.today().year} ",
                rx.span("yharyarias by Yhary Arias", color=Color.PRIMARY.value),           
                "v1."
            ),
            href=const.LINKEDIN_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "BUILDING SOFTWARE WITH LOVE FROM BUCARAMANGA TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )
    