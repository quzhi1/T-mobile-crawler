from operator import add


class Bill:
    """A bill for each month"""

    def __init__(self, monStr, totalInput, personalAdditionalArray):
        assert (len(personalAdditionalArray) == 5)
        self.mon = monStr
        self.total = totalInput
        self.personalAdditional = personalAdditionalArray

        regular = (self.total - sum(self.personalAdditional)) / len(self.personalAdditional)
        self.personal = [x + regular for x in self.personalAdditional]

    def getPersonalArray(self):
        return self.personal

    def printSummary(self):
        personalStr = ["%.2f" % x for x in self.personal]
        print(self.mon + " bills: \n")
        print("Zhi: " + personalStr[0])
        print("Yang: " + personalStr[1])
        print("Yuting: " + personalStr[2])
        print("Zhiyao: " + personalStr[3])
        print("Jie: " + personalStr[4])
        print("\n\n")


# augBill = Bill("Aug", 180.5, [36.08, 10.06, 0.00, 7.96, 1.80])
# septBill = Bill("Sept", 192.01, [36.08, 10.00, 0.20, 0.00, 0.00])
#octBill = Bill("Oct", 180.82, [36.08, 10.00, 0.00, 0.00, 0.00])
#novBill = Bill("Nov", 180.60, [36.08, 10.00, 0.00, 1.00, 0.00])
decBill = Bill("Dec", 181.51, [36.08, 10.00, 0.00, 0.00, 0.00])
janBill = Bill("Mar", 206.54, [36.08, 10.00, 0.00, 0.00, 0.00])
febBill = Bill("Mar", 181.22, [36.08, 10.00, 0.00, 0.00, 0.00])
marBill = Bill("Mar", 184.49, [36.08, 10.00, 0.00, 0.00, 0.00])

# augBill.printSummary();
# septBill.printSummary();
#octBill.printSummary();
#novBill.printSummary();

for i in range(5):
    decArray = decBill.getPersonalArray()
    janArray = janBill.getPersonalArray()
    febArray = febBill.getPersonalArray()
    marArray = marBill.getPersonalArray()
    print("%.2f" % (decArray[i] + janArray[i] + febArray[i] + marArray[i]))
