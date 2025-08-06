# Create the calculator


def sum(a,b):
  return a + b

def sub(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  if b == 0:
    print("Cannot Divide by Zero !")

  return a / b


while True:
  print(" 🧮 /n This is Simple Calculator 🧮")
  print("1.Addition")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Exit")



  choice = input("Enter Your Choice (1-5): ")

  if choice == '5':

    print("Exiting Calculator. Goodbye!")
    break

  if choice in ('1','2','3','4'):
    try:
      a = int(input("Enter Your First Number: "))
      b = int(input("Enter Your Second Number: "))

      if choice == '1':
        print("Result: ",sum(a,b))

      if choice == '2':
        print("Result: ",sub(a,b))

      if choice == '3':
        print("Result: ",multiply(a,b))

      if choice == '4':
        print("Result: ",divide(a,b))

    except ValueError:
      print("Please Enter Valid Inputs !")


  else:
    print("Invalid Choice !")





