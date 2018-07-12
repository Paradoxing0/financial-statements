class IncomeStatement(object):
    def __init__(self, revenue, cogs, depreciation, salaries_exp, sell_admin_exp, interest_exp, tax_rate, dividends,
                 gain_loss):
        self.revenue = revenue
        self.cogs = cogs
        self.depreciation = depreciation
        self.salaries_exp = salaries_exp
        self.sell_admin_exp = sell_admin_exp
        self.interest_exp = interest_exp
        self.tax_rate = tax_rate
        self.dividends = dividends
        self.gain_loss = gain_loss

    def gross_income(self):
        return(self.revenue - self.cogs)

    def operating_income(self):
        return self.gross_income(self)-(self.depreciation+self.salaries_exp+self.sell_admin_exp)

    def net_income(self):
        if self.gain_loss != 0:
            return (self.operating_income(self) - (self.interest_exp) + (self.gain_loss)) * (1 - self.tax_rate)
        else:
            return (self.operating_income(self) - (self.interest_exp)) * (1 - self.tax_rate)

    def retained_earning(self):
        return self.net_income(self) - self.dividends

class StatementOfEquity(object):
    def __init__(self, common_stock, paidin_cap):
        self.common_stock = common_stock
        self.paidin_cap = paidin_cap

class BalanceSheet(object):
    class Assets(object):
        def __init__(self, cash, account_receivables, short_inv, ppe, acc_dep, long_inv, mixlist):
            self.cash = cash
            self.account_receivables = account_receivables
            self.short_inv = short_inv
            self.ppe = ppe
            self.acc_dep = acc_dep
            self.long_inv = long_inv
            self.mixlist = mixlist

        def nppe(self):
            return self.ppe - self.acc_dep

        def total(self):
            return(self.cash+self.account_receivables+self.short_inv
                   +self.ppe-self.acc_dep+self.long_inv)

    class Liabilities(object):
        def __init__(self, notes_payables, accounts_payables, accurals, bonds):
            self.notes_payables = notes_payables
            self.accounts_payables = accounts_payables
            self.accurals = accurals
            self.bonds = bonds

        def total(self):
            return(self.notes_payables+self.accounts_payables+self.accurals+self.bonds)

    class Equity(object):
        def __init__(self,common_equity,retained_earnings):
            self.common_equity = common_equity
            self.retained_earnings = retained_earnings

        def total(self):
            return(self.common_equity+self.retained_earnings)

    def balanced(self):
        if self.Assets.total(self.Assets) == (self.Equity.total(self.Equity)+
                                              self.Liabilities.total(self.Liabilities)):
            return True
        else:
            return False

class CashFlow(object):
    def __init__(self, cash_begin, acc_recB, acc_recE, short_invB, short_invE, acc_payB, acc_payE, accuralsB,
                 accuralsE, ppePurch, ppeSell, long_invPurch, long_invSell, bondsIss, bondsRed, notesB, notesE,
                 stockIss, stockRed):
        self.cash_begin = cash_begin

        #Operating CFs
        self.acc_recB = acc_recB
        self.acc_recE = acc_recE
        self.short_invB = short_invB
        self.short_invE = short_invE
        self.acc_payB = acc_payB
        self.acc_payE = acc_payE
        self.accuralsB = accuralsB
        self.accuralsE = accuralsE

        #Investing CFs
        self.ppePurch = ppePurch
        self.ppeSell = ppeSell
        self.long_invPurch = long_invPurch
        self.long_invSell = long_invSell

        #Financing CFs (incl. dividends)
        self.bondsIss = bondsIss
        self.bondsRed = bondsRed
        self.notesB = notesB
        self.notesE = notesE
        self.stockIss = stockIss
        self.stockRed = stockRed

    def cashOperations(self):
        i = IncomeStatement
        if i.gain_loss != 0:
            return(i.net_income(i)+i.depreciation-i.gain_loss+(self.acc_recB-self.acc_recE)+
                   (self.short_invB-self.short_invE)
               +(self.acc_payE-self.acc_payB)+(self.accuralsE-self.accuralsB))
        else:
            return (i.net_income(i) + i.depreciation + (self.acc_recB - self.acc_recE) + (
                        self.short_invB - self.short_invE)
                    + (self.acc_payE - self.acc_payB) + (self.accuralsE - self.accuralsB))

    def cashInvesting(self):
        return((self.ppeSell+self.long_invSell)-(self.ppePurch+self.long_invPurch))

    def cashFinancing(self):
        return((self.notesE-self.notesB)+(self.bondsIss-self.bondsRed)+(self.stockIss-self.stockRed))

    def cash_end(self):
        return(self.cash_begin+(self.cashOperations(self)+self.cashInvesting(self)+self.cashFinancing(self)))

    def cash_check(self):
        b = BalanceSheet
        if self.cash_end(self) == b.Assets.cash:
            return True
        else:
            return False

def ISPrint():
    f = IncomeStatement
    print("Income Statement")
    print("Revenue: %s" % f.revenue)
    print("Cost of Goods Sold: %s" % f.cogs)
    print("-------------------------")
    print("Gross Income: %s" % f.gross_income(f))
    print()
    print("Salaries Expense: %s" % f.salaries_exp)
    print("Selling & Administrative Expense: %s" % f.sell_admin_exp)
    print("Depreciation: %s" % f.depreciation)
    print("-------------------------")
    print("Operating Income: %s" % f.operating_income(f))
    print()
    print("Interest Expense: %s" % f.interest_exp)
    print("Tax Rate: %s" % f.tax_rate)
    print("-------------------------")
    print("Net Income: %s" % f.net_income(f))
    print()
    print("Dividends: %s" % f.dividends)
    print("-------------------------")
    print("Retained Earnings: %s" % f.retained_earning(f))

def BSPrint():
    f = BalanceSheet
    print("Balance Sheet")
    print("_____Assets_________________")
    print("Cash: %s" % f.Assets.cash)
    print("Accounts Receivables: %s" % f.Assets.account_receivables)
    print("Short Term Investments: %s" % f.Assets.short_inv)
    print("Net Property, Plant, & Equipment: %s" % f.Assets.nppe(f.Assets))
    print("    Accumulated Depreciation: %s" % f.Assets.acc_dep)
    print("    Property, Plant, & Equipment: %s" % f.Assets.ppe)
    print("Long Term Investment: %s" % f.Assets.long_inv)
    print("-------------------")
    print("Total Assets: %s" % f.Assets.total(f.Assets))
    print()
    print("_____Liabilities_______________")
    print("Notes Payables: %s" % f.Liabilities.notes_payables)
    print("Account Payables: %s" % f.Liabilities.accounts_payables)
    print("Accurals: %s" % f.Liabilities.accurals)
    print("Bonds: %s" % f.Liabilities.bonds)
    print("-------------------")
    print("Total Liabilities: %s" % f.Liabilities.total(f.Liabilities))
    print()
    print("_____Equity___________________")
    print("Common Equity: %s" % f.Equity.common_equity)
    print("Retained Earnings: %s" % f.Equity.retained_earnings)
    print("-------------------")
    print("Total Equity: %s" % f.Equity.total(f.Equity))
    print("-------------------")
    print("Total Liabilities & Equity: %s" % (f.Equity.total(f.Equity)+f.Liabilities.total(f.Liabilities)))

def SEPrint():
    f = StatementOfEquity
    g = IncomeStatement
    print("Statement of Equity")
    print("Common Stock (Par): %s" % f.common_stock)
    print("Additional Paid-In Capital: %s" % f.paidin_cap)
    print("-------------------")
    print("Common Equity: %s" % (f.common_stock+f.paidin_cap))
    print()
    print("Retained Earnings: %s" % g.retained_earning(g))
    print("-------------------")
    print("Total Equity: %s" % ((f.common_stock+f.paidin_cap)+g.retained_earning(g)))

def CFPrint():
    f = IncomeStatement
    c = CashFlow

    def change(B, E):
        if B < E:
            return "Increase"
        elif B > E:
            return "Decrease"
        else:
            return "No change"

    print("Statement of Cash Flow")
    print("Net Income: %s" % f.net_income(f))
    print("%s in Account Receivables: %s" % (change(c.acc_recB,c.acc_recE),c.acc_recB-c.acc_recE))
    print("%s in Short Term Investments: %s" % (change(c.short_invB,c.short_invE),c.short_invB-c.short_invE))
    print("%s in Account Payables: %s" % (change(c.acc_payB,c.acc_payE),c.acc_payE-c.acc_payB))
    print("%s in Accurals: %s" % (change(c.accuralsB,c.accuralsE),c.accuralsE-c.accuralsB))
    print("(gain/losses): %s" % f.gain_loss)
    print("     Operating Cash Flows: %s" % c.cashOperations(c))
    print("-----------------------------------------")
    print("Property, Plant, & Equipment Purchases: %s" % c.ppePurch)
    print("Property, Plant, & Equipment Sales: %s" % c.ppeSell)
    print("Long Term Investment Purchases: %s" % c.long_invPurch)
    print("Long Term Investment Sales: %s" % c.long_invSell)
    print("     Investing Cash Flows: %s" % c.cashInvesting(c))
    print("-----------------------------------------")
    print("Bonds Issued: %s" % c.bondsIss)
    print("Bonds Redeemed: %s" % c.bondsRed)
    print("%s in Notes Payables: %s" % (change(c.notesB,c.notesE),c.notesE-c.notesB))
    print("Common Stock Issued: %s" % c.stockIss)
    print("Common Stock Redeemed: %s" % c.stockRed)
    print("     Financing Cash Flows: %s" % c.cashFinancing(c))
    print("-----------------------------------------")
    print("Net Cash: %s" % (c.cashOperations(c)+c.cashInvesting(c)+c.cashFinancing(c)))
    print("Beginning Cash: %s" % c.cash_begin)
    print("End Cash: %s" % c.cash_end(c))

def calc_cash_0():
    h = BalanceSheet
    c = CashFlow
    c.cash_begin = 0
    c.acc_recE = h.Assets.account_receivables
    c.acc_recB = 0
    c.short_invE = h.Assets.short_inv
    c.short_invB = 0
    c.acc_payE = h.Liabilities.accounts_payables
    c.acc_payB = 0
    c.accuralsE = h.Liabilities.accurals
    c.accuralsB = 0
    c.ppePurch = h.Assets.ppe
    c.ppeSell = 0
    c.long_invPurch = h.Assets.long_inv
    c.long_invSell = 0
    c.bondsIss = h.Liabilities.bonds
    c.bondsRed = 0
    c.notesE = h.Liabilities.notes_payables
    c.notesB = 0
    c.stockIss = h.Equity.common_equity
    c.stockRed = 0
    h.Assets.cash = c.cash_end(c)

def new_adj(x):
    f = IncomeStatement
    g = StatementOfEquity
    h = BalanceSheet
    try:
        if (x not in ("Revenue")) is False:
            f.revenue = float(input("Change Revenue: "))
        elif (x not in ("Cost of Goods Sold")) is False:
            f.cogs = float(input("Change Cost of Goods Sold: "))
        elif (x not in ("Salaries Expense")) is False:
            f.salaries_exp = float(input("Change Salaries Expense: "))
        elif (x not in ("Administrative Expense")) is False:
            f.sell_admin_exp = float(input("Change Selling & Administrative Expense: "))
        elif (x not in ("Depreciation")) is False:
            f.depreciation = float(input("Change Depreciation: "))
        elif (x not in ("Interest Expense")) is False:
            f.interest_exp = float(input("Change Interest Expense: "))
        elif (x not in ("Tax Rate")) is False:
            f.tax_rate = float(input("Change Tax Rate: "))
        elif (x not in ("Dividends")) is False:
            f.dividends = float(input("Change Dividends: "))
        elif (x not in ("Common Stock")) is False:
            g.common_stock = float(input("Change Common Stock: "))
        elif (x not in ("Paid-In Capital")) is False:
            g.paidin_cap = float(input("Change Paid-In Capital: "))
        elif (x not in ("Short Term Investment")) is False:
            h.Assets.short_inv = float(input("Change Short Term Investment: "))
        elif (x not in ("Property, Plant, and Equipment")) is False:
            h.Assets.ppe = float(input("Change Property, Plant, and Equipment: "))
        elif (x not in ("Accumulated Depreciation")) is False:
            h.Assets.acc_dep = float(input("Change Accumulated Depreciation: "))
        elif (x not in ("Account Receivables")) is False:
            h.Assets.account_receivables = float(input("Change Account Receivables: "))
        elif (x not in ("Long Term Investment")) is False:
            h.Assets.long_inv = float(input("Change Long Term Investment: "))
        elif (x not in ("Notes Payables")) is False:
            h.Liabilities.notes_payables = float(input("Change Notes Payables: "))
        elif (x not in ("Accounts Payables")) is False:
            h.Liabilities.accounts_payables = float(input("Change Accounts Payables: "))
        elif (x not in ("Accurals")) is False:
            h.Liabilities.accurals = float(input("Change Accurals: "))
        elif (x not in ("Bonds")) is False:
            h.Liabilities.bonds = float(input("Change Bonds: "))
        else:
            print("Sorry. I could not understand your request for an account. Please try again.")
    except ValueError:
        print("There was an error inputting your value. Try again.")

def new():
    f = IncomeStatement
    g = StatementOfEquity
    h = BalanceSheet
    value = []
    text = ["Revenue: ","Cost of Goods Sold: ","Salaries Expense: ","Selling & Administrative Expense: ",
            "Interest Expense: ","Tax Rate: ","Dividends: ","Gain/Loss on Sale of Long Term Assets: ",
            "Common Stock: ","Paid-In Capital: ","Short Term Investment: ","Account Receivables: ",
            "Long Term Investment: ","Notes Payables: ","Accounts Payables: ","Accurals: ","Bonds: "]
    n0 = 17
    n1 = 0
    print("Input the following accounts. Do not leave any blank. If there is no amount, input 0.\n"
          "If you believed that you made an error inputting one of these values you will have an\n"
          "opportunity to fix it later.")
    while n0 > 0:
        try:
            a = float(input(str(text[n1])))
            value.append(a)
            n0 -= 1
            n1 += 1
        except ValueError:
            print("There was an error inputting your value. Try inputting your account again.")

    ppelist = []
    deplist = []
    depratelist = []

    while True:
        try:
            ppenum = int(input("How many different types of Property, Plant, and Equipment will you have?:"))
            n = 1
            if ppenum > 0:
                while ppenum > 0:
                    while True:
                        try:
                            a = float(input("What is the value of purchase?"))
                            break
                        except ValueError:
                            print("There appears to be an error inputting your value. Try again.")
                    while True:
                        try:
                            b = float(input("How much depreciation has it accumulated?"))
                            break
                        except ValueError:
                            print()
                    while True:
                        try:
                            c = float(input("What is the rate of depreciation per year?:"))
                            break
                        except ValueError:
                            print()
                    ppenum -= 1
                    n += 1
                    ppelist.append(a)
                    deplist.append(b)
                    depratelist.append(c)
                break
            else:
                print("That is not an appropriate amount. Try again.")
        except ValueError:
            print()

    h.Assets.mixlist = [[x, y, z] for (x, y, z) in zip(ppelist, deplist, depratelist)]
    f.dividends = sum(deplist)

    f.revenue = value[0]
    f.cogs = value[1]
    f.salaries_exp = value[2]
    f.sell_admin_exp = value[3]
    f.depreciation = sum(depratelist)
    f.interest_exp = value[4]
    f.tax_rate = value[5]
    f.dividends = value[6]
    f.gain_loss = value[7]

    g.common_stock = value[8]
    g.paidin_cap = value[9]

    h.Assets.short_inv = value[10]
    h.Assets.account_receivables = value[11]
    h.Assets.long_inv = value[12]

    h.Liabilities.notes_payables = value[13]
    h.Liabilities.accounts_payables = value[14]
    h.Liabilities.accurals = value[15]
    h.Liabilities.bonds = value[16]

    h.Equity.common_equity = g.common_stock + g.paidin_cap
    h.Equity.retained_earnings = f.retained_earning(f)

    calc_cash_0()

    if h.balanced(h) == False:
        print()
        print("Assets = %s" % h.Assets.total(h.Assets))
        print("Liabilities = %s" % h.Liabilities.total(h.Liabilities))
        print("Equity = %s" % h.Equity.total(h.Equity))
        print("There's no balance. It must be fixed.")
        while True:
            i = input("What do you want to do: print out and analyze one of four financial statements\n"
                      "as is, or do you want to change an account?: ")
            if i == "change":
                x = input("Choose which account to change. (Hint: we highly recommend changing Accumulated Depreciation\n"
                          "for easier adjustment of Assets.")
                new_adj(x)
                calc_cash_0()
                if h.balanced(h) == False:
                    print("Balance Sheet is still not balanced.")
                else:
                    break
            elif i == "print":
                p = input("What do you want to print? ")
                if (p not in ("Balance Sheet")) is False:
                    BSPrint()
                elif (p not in ("Income Statement")) is False:
                    ISPrint()
                elif (p not in ("Statement of Equity")) is False:
                    SEPrint()
                elif (p not in ("Statement of Cash Flows")) is False:
                    CFPrint()
                else:
                    print("I did not understand you. Try again.")
            else:
                print("Sorry. I didn't understand.")


def sample():
    f = IncomeStatement
    g = StatementOfEquity
    h = BalanceSheet

    ppelist = [50, 50, 50, 50]
    deplist = [5, 5, 10, 20]
    depratelist = [1, 1, 1, 2]
    h.Assets.mixlist = [[x, y, z] for (x, y, z) in zip(ppelist, deplist, depratelist)]

    f.revenue = 1000
    f.cogs = 800
    f.salaries_exp = 10
    f.sell_admin_exp = 10
    f.depreciation = sum(depratelist)
    f.interest_exp = 25
    f.tax_rate = 0.4
    f.dividends = 40
    f.gain_loss = 0

    g.common_stock = 150
    g.paidin_cap = 500

    h.Assets.short_inv = 90
    h.Assets.ppe = sum(ppelist)
    h.Assets.acc_dep = sum(deplist) + sum(depratelist)
    h.Assets.account_receivables = 70
    h.Assets.long_inv = 350

    h.Liabilities.notes_payables = 60
    h.Liabilities.accounts_payables = 30
    h.Liabilities.accurals = 10
    h.Liabilities.bonds = 200

    h.Equity.common_equity = g.common_stock + g.paidin_cap
    h.Equity.retained_earnings = f.retained_earning(f)

    calc_cash_0()

while True:
    start = input("Would you like to use a sample set or start a new one from stractch?:\n")
    if start == "new":
        new()
        break
    elif start == "sample":
        sample()
        break
    else:
        print("Sorry. I didn't understand that!")

arcyears = {}
year = 0

def store(year):
    f = IncomeStatement
    g = StatementOfEquity
    h = BalanceSheet
    arcyears[year] = [h.Assets.mixlist,f.revenue,f.cogs,f.salaries_exp,f.sell_admin_exp,f.interest_exp,f.tax_rate,
                   f.dividends,f.gain_loss,g.common_stock,g.paidin_cap,h.Assets.short_inv,h.Assets.account_receivables,
                   h.Assets.long_inv,h.Liabilities.notes_payables,h.Liabilities.accounts_payables,h.Liabilities.accurals,
                   h.Liabilities.bonds]
    year += 1

store(year)

while True:
    option = input("Choose an option (type 'help' for assistance):")
    if (option not in ("print","Print")) is False:
        while True:
            print_op = input("What financial statement would you like printed?:")
            if (print_op not in ("Balance Sheet","balance sheet","Balance sheet")) is False:
                BSPrint()
            elif (print_op not in ("Statement of Equity","statement of equity","Equity","equity")) is False:
                SEPrint()
            elif (print_op not in ("Income Statement","income statement")) is False:
                ISPrint()
            elif (print_op not in ("Statement of Cash Flows","statement of cash flows","Cash Flows",
                                   "cash flows")) is False:
                CFPrint()
            elif (print_op not in ("cancel","Cancel")) is False:
                break
            else:
                print("I did not understand.")
    elif (option not in ("help","Help")) is False:
        print("You can input the following options:")
        print("'print': this option provides the option to print out one of the four financial statements.")
    elif (option not in ("journal entry")):
        pass
    else:
        print("Sorry. The option you put in is not in this system. Try again.")
