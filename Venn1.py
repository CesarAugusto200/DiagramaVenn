import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Tema Generos de Juegos mas jugados
# Librerira Usada matplotlib-venn

terror=100
accion=100
aventura=90


accion_Aventura=50
accion_Terror=50
aventura_Terror=50
accion_aventura_terror=10
#venn3 es para que aparesca los 3 circulos y para que aparescan 2 solo se cambia el 3 por 2 y solo apareceran los 2 circulos
venn3(subsets=(terror,accion,aventura,accion_Aventura,accion_Terror,aventura_Terror,accion_aventura_terror),
      set_labels=("Accion","Aventura","Terror"))

plt.title("Diagrama De Venn De Generos De Videojuegos Mas Jugados")
plt.show()