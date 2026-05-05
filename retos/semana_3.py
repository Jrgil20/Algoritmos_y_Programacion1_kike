"""
=============================================================
 RETO SEMANA 3 – Estadísticas de una Secuencia Numérica
=============================================================

ENUNCIADO:
  Lee N números reales desde la entrada (N lo da el usuario).
  Calcula e imprime: mínimo, máximo, promedio, suma y un valor
  booleano que indique si TODOS los números son positivos.

RESTRICCIONES:
  - 1 ≤ N ≤ 1000  (entero positivo).
  - Cada número es un float arbitrario.
  - No uses las funciones built-in min()/max() ni statistics;
    calcula los valores manualmente para practicar aritmética.

PISTA TÉCNICA:
  Inicializa minimo = maximo = primer_número.
  El booleano "todos_positivos" parte en True y se vuelve False
  con una sola expresión: todos_positivos = todos_positivos and (x > 0).
  Tipos involucrados: int (N, índice), float (valores), bool.
=============================================================
"""

# ── Entrada ──────────────────────────────────────────────────
n = int(input("¿Cuántos números vas a ingresar? "))
numeros: list[float] = []

for i in range(1, n + 1):
    valor = float(input(f"  Número {i}: "))
    numeros.append(valor)

# ── Proceso ──────────────────────────────────────────────────
minimo = numeros[0]
maximo = numeros[0]
suma = 0.0
todos_positivos = True

for x in numeros:
    suma += x
    if x < minimo:
        minimo = x
    if x > maximo:
        maximo = x
    todos_positivos = todos_positivos and (x > 0)

promedio = suma / n

# ── Salida ───────────────────────────────────────────────────
print(f"\n--- Estadísticas de {n} número(s) ---")
print(f"  Mínimo  : {minimo}")
print(f"  Máximo  : {maximo}")
print(f"  Suma    : {suma:.4f}")
print(f"  Promedio: {promedio:.4f}")
print(f"  ¿Todos positivos? {todos_positivos}")
