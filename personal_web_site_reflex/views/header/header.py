import reflex as rx
import datetime
import personal_web_site_reflex.constants as const
from personal_web_site_reflex.styles.styles import Size
from personal_web_site_reflex.styles.colors import Color, TextColor
from personal_web_site_reflex.components.link_icon import link_icon
from personal_web_site_reflex.components.info_text import info_text



def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Yhary Arias",
                size="xl",
                src="avatar.png",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
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
                        "icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    
                    spacing=Size.LARGE.value
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.flex(
            info_text(
                f"{experience()}+", 
                "years of experience"
            ),
            rx.spacer(),
            info_text(
                "+10", 
                "AI projects developed"
            ),
            rx.spacer(),
            info_text(
                "+100", 
                "followers"
            ),
            width="100%"
        ),
        rx.text(
            f"""I'm machine learning engineer. 
            I love what I do. I'm constantly learning. 
            You will realize that I have other skills 
            by taking a look at my repo""",
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )

def experience() -> int:
    return datetime.date.today().year - 2020
