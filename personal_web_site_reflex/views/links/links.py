import reflex as rx
import personal_web_site_reflex.constants as const
from personal_web_site_reflex.components.link_buttun import link_button
from personal_web_site_reflex.components.title import title
from personal_web_site_reflex.styles.styles import Size



def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch", 
            "AI Live Broadcasts",
            "icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            "Medium", 
            "Personal blog",
            "icons/medium.svg",
            const.BLOG_MEDIUM_URL
        ),
        link_button(
            "LinkedIn", 
            "Profesional Profile",
            "icons/linkedin.svg",
            const.LINKEDIN_URL
        ),
        link_button(
            "GitHub", 
            "Code Portfolio", 
            "icons/github.svg",
            const.GITHUB_URL
        ),
        link_button(
            "YouTube", 
            "Programming tutorials", 
            "icons/youtube.svg",
            const.YOUTUBE_ELIA_URL
        ),
        title("Contacto"),
        link_button(
            "Email",
            const.EMAIL,
            "icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=Size.DEFAULT.value,
    )