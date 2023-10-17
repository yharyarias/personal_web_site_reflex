import reflex as rx
from personal_web_site_reflex.components.navbar import navbar
from personal_web_site_reflex.views.header.header import header
from personal_web_site_reflex.views.links.links import links
from personal_web_site_reflex.components.footer import footer

class State(rx.State):
    """The app state."""

    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
        )


# Add state and page to the app.
app = rx.App() # Run our app -> generate an app with Reflex
app.add_page(index) # Add pages
app.compile() # Compile our app
