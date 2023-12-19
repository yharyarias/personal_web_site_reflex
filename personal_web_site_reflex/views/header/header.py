import reflex as rx
import personal_web_site_reflex.constants as const
from personal_web_site_reflex.components.link_icon import link_icon
from personal_web_site_reflex.components.info_text import info_text
from personal_web_site_reflex.styles.styles import Size as Size
from personal_web_site_reflex.styles.colors import TextColor as TextColor
from personal_web_site_reflex.styles.colors import Color as Color


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Yhary Arias",
                size="xl",
                src="avatar.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2xp",
                border="4xp",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Yhary Arias",
                    size="lg"
                ),
                rx.text(
                    "@yharyarias",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    link_icon(
                        "icons/x.svg",
                        const.TWITCH_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    )
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
