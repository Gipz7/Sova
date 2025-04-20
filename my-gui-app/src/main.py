from tkinter import Tk, Label, Entry, Button, StringVar
from gui import calculate_net_salary_gui

def main():
    root = Tk()
    root.title("Salary Calculator")

    # Create GUI components
    Label(root, text="Gross Salary:").grid(row=0, column=0)
    gross_salary_var = StringVar()
    Entry(root, textvariable=gross_salary_var).grid(row=0, column=1)

    Label(root, text="Tax Class:").grid(row=1, column=0)
    tax_class_var = StringVar()
    Entry(root, textvariable=tax_class_var).grid(row=1, column=1)

    Label(root, text="Has Children (True/False):").grid(row=2, column=0)
    has_children_var = StringVar()
    Entry(root, textvariable=has_children_var).grid(row=2, column=1)

    Label(root, text="Church Tax (True/False):").grid(row=3, column=0)
    church_tax_var = StringVar()
    Entry(root, textvariable=church_tax_var).grid(row=3, column=1)

    result_var = StringVar()
    Label(root, textvariable=result_var).grid(row=5, columnspan=2)

    def calculate_salary():
        gross_salary = float(gross_salary_var.get())
        tax_class = int(tax_class_var.get())
        has_children = has_children_var.get() == 'True'
        church_tax = church_tax_var.get() == 'True'
        
        salary_info = calculate_net_salary_gui(gross_salary, tax_class, has_children, church_tax)
        result_var.set(f"Net Salary: {salary_info['net_salary']} €")

    Button(root, text="Calculate", command=calculate_salary).grid(row=4, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()