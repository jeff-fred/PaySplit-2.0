#Create the PaySplitter application
import matplotlib.pyplot as plt
from tkinter import *
import funcs



class PaySplitter:
    """Will take a income and split it into the percentages specified."""
    
    def __init__(self):
        """Initialize application and widgets"""
        self.root = Tk()

        #window settings
        self.win_size = "500x300"
        self.bg_color = "lightgray"
        self.title = "PaySplitter"

        #create window and center it
        funcs.create_window(self.root, self.title, self.bg_color)
        funcs.center_window(self.root, self.win_size)

        #create window grid system
        columns = 0
        while columns <= 2:
            self.root.columnconfigure(columns, weight=1)
            columns += 1
        
        rows = 2
        while rows <= 8:
            self.root.rowconfigure(rows, weight=1)
            rows += 1

        ##mutable widgets
            #mutable labels
        self.savAmountLbl = Label(self.root, text="------", bg=self.bg_color)
        self.invAmountLbl = Label(self.root, text="------", bg=self.bg_color)
        self.spdAmountLbl = Label(self.root, text="------", bg=self.bg_color)
            #entries
        self.paycheck = Entry(self.root)
        self.savingsAmnt = Entry(self.root)
        self.investingAmnt = Entry(self.root)
        self.spendingAmnt = Entry(self.root)


        #data management
        self.numbers = []
        self.percentages = [1]
        
        #chart data
        self.c1 = 100
        self.c2 = 100
        self.c3 = 100

        #fill window with immutable widgets
        self.setup_widgets()

        self.root.mainloop()


    def setup_widgets(self):
        """Set up the immutable labels, and grid the mutable"""
        Label(self.root,text="Split your paycheck any way your heart desires!",
                        font=("Cambria", 13, "bold italic"), 
                        bg="lightgray",
                        fg="black", 
                        pady=5, padx=5, 
                        bd=2, 
                        relief="groove").grid(row=0, columnspan=3, pady=10)

        Label(self.root,text="Place the amount of your paycheck and what percentage you'd like to split it into.", 
                        bg="lightgray", 
                        fg="black", 
                        font=("Times", 10, "underline italic")).grid(row=1, columnspan=3)

        Label(self.root,text="Paycheck Amount", 
                        bg="lightgray",
                        font=("Cambria",12,"bold")).grid(row=2, columnspan=2)

        Label(self.root,text="Category", 
                        bg="lightgray", 
                        font=("Cambria",10,"bold italic")).grid(row=3, column=0)

        Label(self.root,text="Percentage", 
                        bg="lightgray", 
                        font=("Cambria",10,"bold italic")).grid(row=3, column=1)

        Label(self.root,text="Amount", 
                        bg="lightgray", 
                        font=("Cambria",10,"bold italic")).grid(row=3, column=2)

        Label(self.root,text="Savings", 
                        bg="lightgray").grid(row=4, column=0)

        Label(self.root,text="Investing", 
                        bg="lightgray").grid(row=5, column=0)

        Label(self.root,text="Spending",
                        bg="lightgray").grid(row=6, column=0)

        #grid the mutable objects
        self.savAmountLbl.grid(row=4, column=2)
        self.invAmountLbl.grid(row=5, column=2)
        self.spdAmountLbl.grid(row=6, column=2)

        self.paycheck.grid(row=2, column=2)
        self.savingsAmnt.grid(row=4, column=1)
        self.investingAmnt.grid(row=5, column=1)
        self.spendingAmnt.grid(row=6, column=1)

        #Button setup
        Button(
            self.root,
            text="CALCULATE",
            font=("Times",10,"bold"),
            fg="red",
            command=self.calculate
        ).grid(row=7, column=1)  

        Button(
            self.root,
            text="PIE CHART",
            font=("Times", 10, "bold"),
            bg="white",
            command=self.graph_results
        ).grid(row=7, column=2)


    def calculate(self):
        """Calculate percentage amount of the original pay and display it on the mutable labels"""
        #have to check if the values given are valid
        if self.check_values():
            global savingTotal, investingTotal, spendingTotal
            savingTotal = str(round(self.numbers[0]*self.percentages[0], 2))
            investingTotal = str(round(self.numbers[0]*self.percentages[1], 2))
            spendingTotal = str(round(self.numbers[0]*self.percentages[2], 2))

            self.c1 = savingTotal
            self.c2 = investingTotal
            self.c3 = spendingTotal

            self.savAmountLbl.configure(text=savingTotal)
            self.invAmountLbl.configure(text=investingTotal)
            self.spdAmountLbl.configure(text=spendingTotal)  
        else:
            pass

   
    def check_values(self):
        """Check if the entries are integer or float values"""

        try:
            self.numbers.clear()
            self.percentages.clear()

            #append entry values into list to modify
            self.numbers.extend([float(self.paycheck.get()),
                                float(self.savingsAmnt.get()),
                                float(self.investingAmnt.get()),
                                float(self.spendingAmnt.get())])


            #append float percentages into self.percentages
            for i in range(1,4):
                self.percentages.append(self.numbers[i] * 0.01)

            #declaration of variables for later use
            self.paycheckAmnt = self.numbers[0]
            self.savingsPcnt = round(self.percentages[0], 2)
            self.investingPcnt = round(self.percentages[1], 2)
            self.spendingPcnt = round(self.percentages[2], 2)
            
            #check to see if the percentages add up to 100
            if sum((self.numbers[1], self.numbers[2], self.numbers[3])) == 100:
                #let the loop end
                return True
            else:
                funcs.errorBox("Percentages Error.")
                self.savingsAmnt.delete(0, "end")
                self.investingAmnt.delete(0, "end")
    
                self.spendingAmnt.delete(0, "end")

                self.savAmountLbl.configure(text="------")
                self.invAmountLbl.configure(text="------")
                self.spdAmountLbl.configure(text="------")


        except:
            if ValueError:
                self.numbers.clear()
                self.percentages.clear()

                funcs.errorBox("Invalid Integers.")
                #delete all entry values
                self.paycheck.delete(0, "end")
                self.savingsAmnt.delete(0, "end")
                self.investingAmnt.delete(0, "end")
    
                self.spendingAmnt.delete(0, "end")

                #change amount values
                self.savAmountLbl.configure(text="------")
                self.invAmountLbl.configure(text="------")
                self.spdAmountLbl.configure(text="------")

    def graph_results(self):
        data = [savingTotal, investingTotal, spendingTotal]
        labeling = ["Savings", "Investing", "Spending"]
        colors = ['yellowgreen', 'gold', 'lightskyblue']

        plt.pie(data, labels=labeling, colors=colors)
        plt.show()
        
        

if __name__ == "__main__":
    PaySplitter()
