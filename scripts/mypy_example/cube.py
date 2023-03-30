def cube(x: int) -> int:
	return x*x*x

def Hola(name: str) -> str:
    return 'Hola ' + name	

def Hola2(name):
    return 'Hola ' + name	




if __name__ == "__main__":
	
	a = cube(2)

	print(a)

	b = cube(3.0)   # Esto no da error en Python, mypy si lo captura

	print(b)

	print(Hola('Juan'))
	print(Hola2(3)) # Esto da un error de concatenación

	print(Hola(3)) # Esto da un error de concatenación, y además mypy lo captura
	