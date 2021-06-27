from motorInferencia import inferencia
from Perguntas import Perguntas

def main():
	cp = Perguntas()
	respostas = []
	print(cp.perguntas[0])

	for pergunta in cp.perguntas[1:]: 
		respostas.append(input(pergunta).upper())
	print("Seu dinossauro é um: {}".format(inferencia(respostas[0],respostas[1],respostas[2])))
	

if __name__ == '__main__':
	main()