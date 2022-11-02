import numpy as np

print("Klk manin, mira, ten redi' el numero de barras, numero de nodos y numero de grados de libertad")
print("Cuantas barras hay?")
nB = input()
print("Cuantos nodos hay?")
nN = input()
print("Cuantos grados de libertad hay?")
nGl = input()

nB = int(nB)
nN = int(nN)
nGl = int(nGl)

N = nN*nGl

h = 1 #para las matrices
H = []
while h < nB + 1:
	H.append(h)
	h = h + 1

matdct = {}
for i in H:
	matdct['K%s' % i] = np.zeros([2*nGl, 2*nGl], dtype = float)

mat2dct = {}
for i in H:
	mat2dct['K%sa' % i] = np.zeros([2*nGl], dtype = int)


for i in H:
	print("Para K{}".format(i))
	I = 0
	while I < 2*nGl:
		J = 0
		while J < 2*nGl:
			print(f'Elemento {I + 1} {J + 1}')
			matdct['K%s' % i][I][J] = float(input())
			J = J + 1
		I = I + 1

for i in H:
	print("Para K{}A".format(i))
	I = 0
	while I < 2*nGl:
		print(f'Elemento {I + 1}')
		mat2dct['K%sa' % i][I] = float(input())
		I = I + 1


K = np.zeros([N, N], dtype = float)
for i in H:
	n = 0
	while n < N + 1:
		m = 0
		while m < N + 1:
			try:
				K[mat2dct['K%sa' % i][n] - 1][mat2dct['K%sa' % i][m] - 1] = \
				K[mat2dct['K%sa' % i][n] - 1][mat2dct['K%sa' % i][m] - 1] + \
				matdct['K%s' % i][n][m]
			except:
				pass
			m = m + 1
		n = n + 1

print(K)
