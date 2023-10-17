import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Yhary Arias",
            heihgt="40xp"
        ), 
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        z_index="999" 
    )
