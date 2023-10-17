import reflex as rx
from personal_web_site_reflex.components.link_buttun import link_buttun

def links() -> rx.Component:
    return rx.vstack(
        link_buttun("LinkedIn", "https://www.linkedin.com/in/yharyarias/"),
        link_buttun("X", "https://twitter.com/yharyarias5"),
        link_buttun("GitHub", "https://github.com/yharyarias"),
        link_buttun("YouTube", "https://youtube.com/@yharyarias596?si=AHoi4ApDd-hJkSIi")
    )