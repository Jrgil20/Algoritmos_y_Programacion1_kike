"""
=============================================================
 RETO SEMANA 6 – Clasificador de Triángulos
=============================================================

ENUNCIADO:
  Lee los tres lados de un triángulo e indica: (a) si los lados
  forman un triángulo válido, (b) el tipo por lados
  (equilátero/isósceles/escaleno) y (c) el tipo por ángulos
  (rectángulo/obtusángulo/acutángulo).

RESTRICCIONES:
  - Cada lado es un número real positivo > 0.
  - Usa la desigualdad triangular para validar.
  - Clasifica por ángulos usando el teorema de Pitágoras
    extendido: c² vs a² + b² (donde c es el lado mayor).

PISTA TÉCNICA:
  Ordena los lados con sorted() para identificar el hipotenusa.
  Para ángulos: c² == a²+b² → rectángulo,
                c² >  a²+b² → obtusángulo,
                c² <  a²+b² → acutángulo.
  Encadena if/elif/else anidados sin repetir lógica.
=============================================================
"""

# ── Entrada ──────────────────────────────────────────────────
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

# ── Validación: desigualdad triangular ───────────────────────
es_valido = (a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (b > 0) and (c > 0)

if not es_valido:
    print("\n❌ Los lados NO forman un triángulo válido.")
else:
    # ── Clasificación por lados ───────────────────────────────
    if a == b == c:
        tipo_lados = "Equilátero"
    elif a == b or b == c or a == c:
        tipo_lados = "Isósceles"
    else:
        tipo_lados = "Escaleno"

    # ── Clasificación por ángulos (teorema de Pitágoras) ─────
    lados_ordenados = sorted([a, b, c])
    x, y, z = lados_ordenados          # z es el lado mayor

    c2 = z ** 2
    ab2 = x ** 2 + y ** 2

    if c2 == ab2:
        tipo_angulo = "Rectángulo"
    elif c2 > ab2:
        tipo_angulo = "Obtusángulo"
    else:
        tipo_angulo = "Acutángulo"

    # ── Salida ────────────────────────────────────────────────
    print(f"\n✅ Triángulo válido con lados {a}, {b}, {c}")
    print(f"  Tipo por lados  : {tipo_lados}")
    print(f"  Tipo por ángulos: {tipo_angulo}")
