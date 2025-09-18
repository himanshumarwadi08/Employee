import pandas as pd
import matplotlib.pyplot as mt

df = pd.read_csv("Employee.csv")

def education():
    row = df["Education"].value_counts()
    lab = ["Bachelors","Masters","PHD"]

    color = ["#00FFF7","#FF00B7","#00FF00"]

    result = mt.pie(row,labels=lab,colors=color,autopct="%1.1f%%")
    mt.title("Distribution of Employee Education Levels")

    mt.show()


def gender():
    gen = df["Gender"].value_counts()
    gen_lab = ["Male","Female"] 
    colors = ["#FFD700", "#FF69B4"]

    mt.pie(gen, labels=gen_lab, colors=colors, autopct="%1.1f%%")
    mt.title("Gender Distribution")
    mt.show()

def join_year():

    join_counts = df["JoiningYear"].value_counts().sort_index()
    years = join_counts.index
    counts = join_counts.values

    mt.bar(years, counts, color="#00D9FF")
    mt.xlabel("Joining Year")
    mt.ylabel("Number of Employees")
    mt.title("Employee Joining Year Distribution")

    mt.show()

def city():
    join_city = df["City"].value_counts()
    city_value=["Bangalore","Pune","New Delhi"]
    color = ["#59FF00","#00C2F2","#BF09A7"]
    mt.title("Distribution of Employee's work on City")

    mt.pie(join_city,labels=city_value,autopct="%1.1f%%",colors=color)

    mt.show()

def info():
    print("Employee Dataset Information : ")
    print()
    print(df.info())
    print()
    print("Calculating Numerical Column in Dataset : ")
    print()
    print(df.describe())

while True:
    choice = input("Enter a Choice :\n1 = Employee's Education\n2 = Employee's Gender\n3 = Employee's Joining Year\n4 = Employee's Work on City\n5 = DataSet Information\n").strip()
    if(choice == '0'):
        print("Good Bye!")
        break
    choices = list(set(choice.split()))
    for choice in choices:
        if(choice == '1'):
            education()
        elif(choice == '2'):
            gender()
        elif(choice == '3'):
            join_year()
        elif(choice == '4'):
            city()
        elif(choice == '5'):
            info()
        else:
            print()
            print("----------------------------------------------")
            print("Please enter a valid Choice")
            print("Exit a program to press a ' 0 ' ")
            print("----------------------------------------------")
