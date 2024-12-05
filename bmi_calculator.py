import tkinter as tkinter
from tkinter import ttk

# creating an object
root = tkinter.Tk()

# setting title and geometry
root.title("BMI Calculator")
root.geometry("470x380+300+200")

# background color for window
root.config(bg="#f0f0f0")  # Set light background color


# BMI Calculation
def bmi():
    try:
        Height = float(h.get())
        Weight = float(w.get())
        m = Height / 100  # converting height into meter
        B = round(float(Weight / m ** 2), 1)  # calculating
        label.config(text=B)  # displaying

        # conditions
        if B <= 18.5:
            label1.config(text="Underweight")
        elif (B > 18.5) and (B <= 25):
            label1.config(text="Normal")
        elif (B > 25) and (B <= 30):
            label1.config(text="Overweight")
        else:
            label1.config(text="Health is at risk!\n Need to lose")
    except ValueError:
        label.config(text="Invalid Input")
        label1.config(text="Please enter valid numbers")


# Heading label
top = tkinter.Label(root, text="BMI CALCULATOR", font=("arial", 25, "bold"), width=25, bd=5, bg="white")
top.place(x=0, y=10)

# Entry widget for height
height = tkinter.StringVar()
weight = tkinter.StringVar()

h_label = tkinter.Label(root, text="Height (cm)", font=("arial", 12), bg="#f0f0f0", fg="black")
h_label.place(x=35, y=70)
h = tkinter.Entry(root, textvariable=height, width=15, font=("arial", 20), bg="white", fg="black", bd=2,
                  justify="center")
h.place(x=35, y=100)

# Entry widget for weight
w_label = tkinter.Label(root, text="Weight (kg)", font=("arial", 12), bg="#f0f0f0", fg="black")
w_label.place(x=255, y=70)
w = tkinter.Entry(root, textvariable=weight, width=15, font=("arial", 20), bg="white", fg="black", bd=2,
                  justify="center")
w.place(x=255, y=100)

# button for report
tkinter.Button(root, text="Report", width=15, height=2, font=("Arial", 10, "bold"), bg="#1f6e68", fg="white",
               command=bmi).place(x=150, y=160)

# label widget for showing calculated BMI (centered below the Report button)
label = tkinter.Label(root, font=("arial", 20, "bold"), bg="white", fg="black")
label.place(x=180, y=220)

# Label widget for showing message (centered below BMI value)
label1 = tkinter.Label(root, font=("arial", 12, "bold"), bg="white", fg="black", width=30)
label1.place(x=35, y=270)

# event loop
root.mainloop()
