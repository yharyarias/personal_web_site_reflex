import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Yhary Arias", size="xl"),
        rx.text("@yharyarias"),
        rx.text("Hello, my name is Yhary Arias."),
        rx.text("""I'm machine learning engineer. 
        I love what I do. I'm constantly learning. 
        You will realize that I have other skills 
        by taking a look at my repo""")
    )
