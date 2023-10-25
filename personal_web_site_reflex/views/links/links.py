import reflex as rx
from personal_web_site_reflex.components.link_buttun import link_buttun
from personal_web_site_reflex.components.title import title
from personal_web_site_reflex.styles.styles import Size as Size



def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_buttun(
            "LinkedIn", 
            "Profesional Profile",
            "https://www.linkedin.com/in/yharyarias/"),
        link_buttun(
            "X", 
            "Anything technology", 
            "https://twitter.com/yharyarias5"),
        link_buttun(
            "GitHub", 
            "Code Portfolio", 
            "https://github.com/yharyarias"),
        link_buttun(
            "YouTube", 
            "Programming tutorials", 
            "https://youtube.com/@yharyarias596?si=AHoi4ApDd-hJkSIi"),
        width="100%",
        spacing=Size.MEDIUM.value,
    )