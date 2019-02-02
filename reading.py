import PyPDF2 
import math

totalBuy=0
totalSell=0
winnings = 0
def main():
    fname = input("input filename:\n")
    filename = fname+".pdf"
    #print(filename)
    readingTheFile(filename)
    

def readingTheFile(filename):

    pdfFileObj = open(filename, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    numPages = pdfReader.numPages
    print("numPages: ",numPages)
    for i in range(numPages):
        print("pageNum/total: ",i,"/",numPages)
        pageObj = pdfReader.getPage(i)
        text = pageObj.extractText()
        if "Gross Winnings:" in text:
            name="winnings"
            line=" "
            ind = text.index("Gross Winnings:")
            for i in range(ind, ind+100):
                line+= text[i]
            money = "0"
            #print(line)
            if "$" in line:
                print(line)
                moneyIndex = line.index("$")
                for i in range(moneyIndex+1,moneyIndex+7):
                    money += line[i]
                themoney=""
                num=0
                while not "." in money[num]:
                    if "," in money[num]:
                        num+=1
                    else:
                        themoney += money[num]
                        num+=1
                    newMoney = int(themoney)
                    val(name,newMoney)

        if "00 Proceeds:" in text:
            #print("Index of Proceeds: ",text.index("Proceeds"))
            name="sell"
            ind = text.index("00 Proceeds:")
            #print(text[ind-1])
            line= " "
            for i in range(ind,ind+100):
                line+= text[i]
            money = "0"
            #print(line)
            if "$" in line:
                print(line)
                moneyIndex = line.index("$")
                for i in range(moneyIndex+1,moneyIndex+7):
                    money += line[i]
                themoney=""
                num=0
                while not "." in money[num]:
                    if "," in money[num]:
                        num+=1
                    else:
                        themoney += money[num]
                        num+=1
                #print("themoney: ",themoney)
                newMoney = int(themoney)
                val(name,newMoney)

            
        if "Cost and Basis" in text:
            name = "buy"
            ind = text.index("Cost and Basis:.")
            line= " "
            for i in range(ind,ind+80):
                line+= text[i]
            money = "0"
            if "$" in line:
                #print(line)
                moneyIndex = line.index("$")
                for i in range(moneyIndex+1,moneyIndex+7):
                    money += line[i]
                themoney=""
                num=0
                while not "." in money[num]:
                    if "," in money[num]:
                        num+=1
                    else:
                        themoney += money[num]
                        num+=1
                newMoney = int(themoney)
                val(name,newMoney)
        

    pdfFileObj.close()
    fileDone()
    

def fileDone():
    print("\n\n")
    print("total Buy: $", totalBuy)
    print("total Sell: $",totalSell)
    totalDif = totalBuy - totalSell
    print("total profit/loss: $",totalDif)
    print("winnings: ", winnings)
    print("\n\n")


def val(name,money):
    global totalBuy
    global totalSell
    global winnings
    if name == "buy":
        totalBuy+= money
       
    if name == "sell":
        totalSell+=money
    if name =="winnings":
        winnings+= money

main()