from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from MainGame import calculate_net_salary

class SalaryCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Salary Calculator")

        self.gross_salary_label = Label(master, text="Gross Salary:")
        self.gross_salary_label.pack()

        self.gross_salary_entry = Entry(master)
        self.gross_salary_entry.pack()

        self.tax_class_label = Label(master, text="Tax Class (1, 3, 5):")
        self.tax_class_label.pack()

        self.tax_class_entry = Entry(master)
        self.tax_class_entry.pack()

        self.has_children_label = Label(master, text="Has Children (True/False):")
        self.has_children_label.pack()

        self.has_children_entry = Entry(master)
        self.has_children_entry.pack()

        self.church_tax_label = Label(master, text="Church Tax (True/False):")
        self.church_tax_label.pack()

        self.church_tax_entry = Entry(master)
        self.church_tax_entry.pack()

        self.calculate_button = Button(master, text="Calculate", command=self.calculate_salary)
        self.calculate_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def calculate_salary(self):
        try:
            gross_salary = float(self.gross_salary_entry.get())
            tax_class = int(self.tax_class_entry.get())
            has_children = self.has_children_entry.get().lower() == 'true'
            church_tax = self.church_tax_entry.get().lower() == 'true'

            salary_info = calculate_net_salary(
                gross_salary=gross_salary,
                tax_class=tax_class,
                has_children=has_children,
                church_tax=church_tax
            )

            result = f"Net Salary: {salary_info['net_salary']} €\n" \
                     f"Social Contributions: {salary_info['social_contributions']} €\n" \
                     f"Income Tax: {salary_info['income_tax']} €\n" \
                     f"Solidarity Tax: {salary_info['solidarity_tax']} €"
            self.result_label.config(text=result)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid input values.")

def main():
    root = Tk()
    app = SalaryCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()