rectangulo = []
def rectangulo ( param1,param2,caracter):
	for i in range(param1):
		for g in range(param2):
			print caracter,
		print ""
altura = int(input("introduce la anchura del rectangulo"))
anchura = int(input("que altura tiene el rectangulo"))
caracter = raw_input("en que caracter quiere realizar el rectangulo?")
rectangulo (anchura, altura, caracter)
