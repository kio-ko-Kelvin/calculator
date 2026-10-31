
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Calculator")
app.geometry("500x700")
app.resizable(False, False)


# =====================================
# MAIN APPLICATION FRAME
# =====================================

mainframe = ctk.CTkFrame(
    app,
    corner_radius=15
)

mainframe.pack(
    padx=15,
    pady=15,
    fill="both",
    expand=True
)


# =====================================
# DISPLAY FRAME
# =====================================

display_frame = ctk.CTkFrame(
    mainframe,
    height=130,
    corner_radius=10
)

display_frame.pack(
    padx=10,
    pady=10,
    fill="x"
)

display_frame.pack_propagate(False)


# Expression display
expression_label = ctk.CTkLabel(
    display_frame,
    text="",
    font=("Arial", 18),
    anchor="e"
)

expression_label.pack(
    padx=15,
    pady=(15, 0),
    fill="x"
)


# Result display
result_label = ctk.CTkLabel(
    display_frame,
    text="0",
    font=("Arial", 35, "bold"),
    anchor="e"
)

result_label.pack(
    padx=15,
    pady=(5, 10),
    fill="x"
)


# =====================================
# BUTTON FRAME
# =====================================

button_frame = ctk.CTkFrame(
    mainframe,
    corner_radius=10
)

button_frame.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)


# Configure button grid
for column in range(4):
    button_frame.grid_columnconfigure(
        column,
        weight=1
    )

for row in range(5):
    button_frame.grid_rowconfigure(
        row,
        weight=1
    )


# Calculator button layout
buttons = [
    ["AC", "±", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "⌫", "="]
]


# Create buttons
for row_index, row in enumerate(buttons):

    for column_index, value in enumerate(row):

        button = ctk.CTkButton(
            button_frame,
            text=value,
            font=("Arial", 22, "bold"),
            corner_radius=10,
            command=lambda: None
        )

        button.grid(
            row=row_index,
            column=column_index,
            padx=5,
            pady=5,
            sticky="nsew"
        )


# =====================================
# APPLICATION EXECUTION
# =====================================

app.mainloop()
