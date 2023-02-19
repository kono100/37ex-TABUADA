#37. Elabore um programa que exiba automaticamente a tabuada de um número informado pelo
#usuário. Sugestão: faça manualmente (lápis/caneta) uma tabuada, entenda o que se repete,
#para depois fazer a programação do for.
tabuada=int(input("Qual Tabuada Voce Quer? "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )