from tkinter import *
from tkinter import messagebox

# main
root = Tk()
# window size
root.geometry("700x500")
# window title
root.title("Sick Form")
# window background
root.config(bg="skyblue")

frame = Frame(root)



#The layout of The Sick Class

# sickness code placement and label
MSickID = Label(root, text = "SicknessCode", bg="skyblue")
MSickID.pack(side = LEFT)
MSickID.place(x = 20, y = 20)

# sick entry and placement
sick_entry = Entry(root, bd =1, bg="yellow")
sick_entry.pack(side = RIGHT)
sick_entry.place(x = 300, y = 20)

# treatment label and placement
MDurationOfTreatment = Label(root, text = "Duration of Treatment", bg="skyblue")
MDurationOfTreatment.pack(side =LEFT )
MDurationOfTreatment.place(x = 20, y= 80)

# weeks/monthly label and placement
weeks_monthly = Label(root, text = "Weekly/Months", bg="skyblue")
weeks_monthly.pack(side = RIGHT)
weeks_monthly.place(x = 380, y = 80)

# amount due entry and placement
due_entry = Entry(root, bd =1, width = 8, bg="yellow")
due_entry.pack(side =RIGHT)
due_entry.place(x = 300, y = 80)

# doctors practice number label and placement
MDoctorsID = Label(root, text="Doctors Practice Number", bg="skyblue")
MDoctorsID.pack(side = LEFT)
MDoctorsID.place(x = 20, y = 150)

# entry and placement for doctors practice number
doc_entry = Entry(root, bd =1, bg="yellow")
doc_entry.pack(side = RIGHT)
doc_entry.place(x = 300, y =150)

# label and placement for scan/consultation fee
scan_fee = Label(root, text = "Scan/Consultation Fee", bg="skyblue")
scan_fee.pack(side = LEFT)
scan_fee.place(x = 20, y = 190)

# entry and placement for scan/consultation fee
scan_entry = Entry(root, bd =1, bg="yellow")
scan_entry.pack(side = RIGHT)
scan_entry.place(x = 301, y = 190)

# label and placement for the amount paid
amount_paid = Label(root, bg="skyblue")
amount_paid.pack(side = LEFT)
amount_paid.place(x = 20, y = 260)

# type of variable
var = StringVar()

# The Calculations for the Sick Class
class Sick():
    def sickness(self):
        self.MSickID = MSickID
        self.MDurationOfTreatment = MDurationOfTreatment
        self.MDoctorsID = MDoctorsID
        self.medcancer = 400
        self.medinflu = 350.50

# Calculating Cancer
def sickness():
    if var.get() == "Cancer":
        if int(scan_entry.get()) > 600:
            messagebox.showinfo("Message", "Sorry we cannot treat you") # Error message will display
        elif int(scan_entry.get()) < 600:
           cancer_answer = int(scan_entry.get()) + 400
           amount_paid.config(text="Amount Paid For Treatment: " + str(cancer_answer))

    if var.get() == "Influenza": # Calculating Influenza
        if int(scan_entry.get()) >= 600:
            influ_answer = 350.50 + int(scan_entry.get())
            amount_paid.config(text="AmountPaidForTreatment: " + str(influ_answer))
        elif int(scan_entry.get()) < 600:
            influ_answer = 350.50 + int(scan_entry.get())
            discount = (influ_answer * (2/100)) + influ_answer # Calculating the discount recieve
            messagebox.showinfo("Message", "2% discount")
            amount_paid.config(text="Amount Paid For Treatment: "  + str(discount)) #discount will be included in the calculation



# radio button for cancer
radbtn1 = Radiobutton(root, text = "Cancer" , variable = var, value ="Cancer", bg="skyblue") # Radiobutton for Cancer
radbtn1.pack(side = LEFT)
radbtn1.place(x = 20, y= 220)

# radio button for Influenza
radbtn2 = Radiobutton(root, text = "Influenza", variable = var, value = "Influenza", bg="skyblue")# Radiobutton for Influenza
radbtn2.pack(side = LEFT)
radbtn2.place(x = 20, y= 240)

# calculate button
cal_btn = Button(root, text = "Calculate", command = sickness, bg="yellow") # Calculates the amount paid for treatment once pushed
cal_btn.pack(side = LEFT)
cal_btn.place(x = 20, y = 300)

# Function on the clear all button
def clear_all():
    sick_entry.delete(0,END)
    due_entry.delete(0,END)
    doc_entry.delete(0,END)
    scan_entry.delete(0,END)

clear_btn = Button(root, text = "Clear", command = clear_all, bg="yellow") # this button is to clear information on the window
clear_btn.pack(side = RIGHT)
clear_btn.place(x = 300, y = 300)


# to run the program
root.mainloop()
