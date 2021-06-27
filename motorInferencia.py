
def inferencia(herbivoro, adorno, grande):
	if herbivoro == "S":
		if adorno == "S":
			if grande == "S":
				return "Triceratops"
			else:
				return "Paquicefalossauro"
		else:
			if grande == "S":
				return "Diplodocus"
			else:
				return "Galiminius"
	else:
		if adorno == "S":
			if grande == "S":
				return "Carnotauro"
			else:
				return "Dilofossauro"
		else:
			if grande == "S":
				return "Tiranossauro"
			else:
				return "Velociraptor"