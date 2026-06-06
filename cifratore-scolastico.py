def cifrare(frase, chiave):
	risultato = ''
	for lettera in frase:
		if 'a'<= lettera <= 'z': 
			cod = ord(lettera) + chiave
			if cod > ord('z'):
				cod = cod - 26
			risultato = risultato + chr(cod)
		else:
			risultato += lettera
   
	print(f"Frase cifrata: {risultato}")
	return risultato

def decifrare(frase, chiave):
	risultato = ''
	for lettera in frase:
		if 'a' <= lettera <= '<':
			cod = ord(lettera) - chiave
			if cod < ord('a'):
				cod += 26
			risultato += chr(cod)
		else:
			risultato += lettera
	print(f"Frase decifrata: {risultato}")
	return risultato


def bruteforce(frase):
	print("=== BruteForce ===")
	for chiave in range(1,27):
		risultato = ''
		for lettera in frase:
			if "a"<= lettera <="z":
				cod = ord(lettera) - chiave
				if cod < ord('a'):
					cod = cod + 26
				risultato = risultato + chr(cod)
			else:
				risultato += lettera
		print(f"chiave: {chiave}, frase decifrata: {risultato}")
				

			
def main():
	print("=== Cifrario di Cesare ===")
	print()

	scelta = input("cosa vuoi fare? (c/d/b): ").lower()

	if scelta == "c":
		frase = input("inserisci la tua frase: ").lower()
		chiave = int(input("inserisci la tua chiave: "))
		cifrare(frase, chiave)
	elif scelta == "d":
		frase = input("inserisci la tua frase: ").lower()
		chiave = int(input("inserisci la tua chiave: "))
		decifrare(frase, chiave)
	elif scelta == "b":
		frase = input("inserisci la tua frase: ").lower()
		bruteforce(frase)

	else:
         print("Selezione non valida. Riavviare e inserire selezione corretta")
	
 	
if __name__ == "__main__":
	main()
