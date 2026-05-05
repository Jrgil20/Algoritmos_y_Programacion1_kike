"""
=============================================================
 RETO SEMANA 1 – Conversor de Unidades de Temperatura
=============================================================

ENUNCIADO:
  Lee el nombre del usuario y una temperatura en grados Celsius.
  Muestra la temperatura convertida a Fahrenheit y Kelvin con
  2 decimales, saludando al usuario por nombre.

RESTRICCIONES:
  - La temperatura puede ser cualquier número real (float).
  - El nombre puede contener espacios (usa input() directamente).
  - No se requiere manejo de errores; asume entradas válidas.

PISTA TÉCNICA:
  F = C * 9/5 + 32   |   K = C + 273.15
  Usa float() para convertir el input y f-strings con :.2f para
  el formateo.
=============================================================
"""

# ── Entrada ──────────────────────────────────────────────────
nombre = input("Ingresa tu nombre: ")
celsius = float(input("Temperatura en Celsius: "))

# ── Proceso ──────────────────────────────────────────────────
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

# ── Salida ───────────────────────────────────────────────────
print(f"\nHola, {nombre}!")
print(f"{celsius:.2f} °C  =  {fahrenheit:.2f} °F  =  {kelvin:.2f} K")
