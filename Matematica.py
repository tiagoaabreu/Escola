from statistics import mean,median,mode

dados = [ 5.39, 
  5.69, 
  5.91,
  5.24,
  5.10,
  5.94,
  5.20,
  5.53,
  5.10,
  5.93,
  5.23,
  5.78,
  5.63,
  5.60,
  5.47,
  5.38,
  5.87,
  5.18,
  5.14,
  5.23,
  5.99,
  5.22,
  5.13,
  5.07,
  5.82
]
mediana = median(dados)
media = mean(dados)
moda = mode(dados)

print("Mediana é de: "+str(mediana)+'\n' ,"Moda é de: "+str(moda)+'\n','Media é de: '+str(media))
