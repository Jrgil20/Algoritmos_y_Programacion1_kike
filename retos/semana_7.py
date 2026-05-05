"""
=============================================================
 RETO SEMANA 7 – Adivina el Número Oculto
=============================================================

ENUNCIADO:
  El programa genera un número oculto aleatorio entre 1 y 100.
  El usuario tiene máximo 7 intentos para adivinarlo; con cada
  intento recibe una pista (mayor/menor). Usa break al acertar
  y continue para saltar entradas no numéricas sin gastar intento.

RESTRICCIONES:
  - Intentos máximos: 7 (for loop con range).
  - Entradas no enteras deben manejarse con try/except sin
    consumir un intento (continue).
  - Al terminar el bucle sin acierto, revela el número oculto.

PISTA TÉCNICA:
  for intento in range(1, MAX_INTENTOS + 1):
      try: guess = int(input(...))
      except ValueError: continue        # no gasta intento
      if guess == objetivo: ...; break
  La variable `acertado` (bool) fuera del bucle indica si hubo
  victoria; el bloque for/else de Python puede reemplazarla.
=============================================================
"""

import random

# ── Constantes ───────────────────────────────────────────────
LIMITE_INF: int = 1
LIMITE_SUP: int = 100
MAX_INTENTOS: int = 7

# ── Generación del número oculto ─────────────────────────────
objetivo: int = random.randint(LIMITE_INF, LIMITE_SUP)

print(f"🎯 Adivina el número oculto entre {LIMITE_INF} y {LIMITE_SUP}.")
print(f"   Tienes {MAX_INTENTOS} intentos. ¡Buena suerte!\n")

intentos_usados: int = 0

for intento in range(1, MAX_INTENTOS + 1):
    try:
        guess = int(input(f"Intento {intento}/{MAX_INTENTOS} → "))
    except ValueError:
        print("  ⚠️  Ingresa un número entero válido (intento no contado).")
        continue                         # no consume el intento

    intentos_usados += 1

    if guess < LIMITE_INF or guess > LIMITE_SUP:
        print(f"  ⚠️  Fuera de rango. Ingresa entre {LIMITE_INF} y {LIMITE_SUP}.")
    elif guess == objetivo:
        print(f"\n🎉 ¡Correcto! Adivinaste en {intentos_usados} intento(s).")
        break
    elif guess < objetivo:
        print("  📈 El número oculto es MAYOR.")
    else:
        print("  📉 El número oculto es MENOR.")
else:
    # Se ejecuta cuando el for termina sin break (sin acierto)
    print(f"\n😞 Se acabaron los intentos. El número oculto era {objetivo}.")
