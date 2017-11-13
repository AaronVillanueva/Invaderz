#enconding: UTF-8
import matplotlib.pyplot as plot

def main():
    entrada= open("quijote.txt","r",encoding="UTF-8")
    datos=entrada.read()
    entrada.close()

    contadores={}

    for letra in datos:
        if letra.isalpha():
            if letra in contadores:
                contadores[letra]+=1
            else:
                contadores[letra]=1
    print(contadores)

    listaLetras=[]
    listaFrecuecia=[]

    for t in contadores.items():
        listaLetras.append(t[0])
        listaFrecuecia.append(t[1])

    x=list(range(len(listaLetras)))
    plot.plot(x,listaFrecuecia)
    plot.show()

    salida=open("frecuencias.txt","w",encoding="utf-8")
    salida.write("Letra\tFrecuencia\n")
    for t in contadores.items():
        salida.write(t[0]+ "\t\t" + str(t[1]) + "\n")

    salida.close()

main()
