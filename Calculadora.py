print("********************")
print("CALCULADORA")
print("********************")
n1 = input("Insira o primeiro numero: ")
n2 = input("Insira o segundo numero: ")
op = input ("Selecione a operação desejada: 1 (soma), 2 (subtração), 3 (multiplicação), 4 (divisão), 5 (potênciação): ")

if op == "1":
    resultado = int(n1) + int(n2)

elif op == "2":
    resultado = int(n1) - int(n2)

elif op == "3":
    resultado = int(n1) * int(n2)

elif op == "4":
    resultado = int(n1) / int(n2)

elif op == "5":
    resultado = int(n1) ** int(n2)    
    
else: 
    print("Operação inválida!")    

print("O resultado da operação é igual a: " + str (resultado))