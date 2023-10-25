import reflex as rx
from personal_web_site_reflex.components.link_icon import link_icon
from personal_web_site_reflex.components.info_text import info_text
from personal_web_site_reflex.styles.styles import Size as Size


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Yhary Arias", size="xl"),
            rx.vstack(
                rx.heading(
                    "Yhary Arias", 
                    size="lg"
                ),
                rx.text(
                    "@yharyarias",
                    margin_top="0px !important"
                ),
                rx.hstack(
                    link_icon("https://www.linkedin.com/in/yharyarias/"),
                    link_icon("https://twitter.com/yharyarias5"),
                    link_icon("https://github.com/yharyarias")
                ),
                align_items="start"
            ),
            spacing=Size.BIG.value,
        ),
        rx.flex(
            info_text("+3", "years of experience"),
            rx.spacer(),
            info_text("+3", "years of experience"),
            rx.spacer(),
            info_text("+3", "years of experience"),
            width="100%"
        ),
        rx.text("""I'm machine learning engineer. 
        I love what I do. I'm constantly learning. 
        You will realize that I have other skills 
        by taking a look at my repo"""),
        spacing=Size.BIG.value,
        align_items="start"
    )
