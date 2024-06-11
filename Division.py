num1=float(input("Ingrese el numero dividendo: "))
num2=float(input("Ingrese el numero divisor: "))

if num2==0:
    print("Error de division por Cero (0).")
else:
    div_result=num1/num2
    print(f"Division {num1} / {num2} = {div_result}")