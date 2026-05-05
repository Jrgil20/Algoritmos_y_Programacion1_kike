"""
=============================================================
 RETO SEMANA 2 – Calculadora Robusta con Manejo de Errores
=============================================================

ENUNCIADO:
  Construye una calculadora que lea dos números y un operador
  (+, -, *, /) desde la entrada estándar. Maneja explícitamente
  los errores ValueError (entrada no numérica) y
  ZeroDivisionError (división entre cero) con mensajes claros.

RESTRICCIONES:
  - Operadores válidos: +  -  *  /
  - Los operandos son números reales (float).
  - Si el operador no es válido, muestra un mensaje de error
    específico sin lanzar excepción no controlada.

PISTA TÉCNICA:
  Usa bloques try/except anidados o secuenciales.
  Recuerda que int("abc") lanza ValueError; la división entera
  10 // 0 lanza ZeroDivisionError igual que 10 / 0.
=============================================================
"""


def calcular(a: float, operador: str, b: float) -> float | None:
    """Realiza la operación y retorna el resultado o None si falla."""
    if operador == "+":
        return a + b
    if operador == "-":
        return a - b
    if operador == "*":
        return a * b
    if operador == "/":
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return a / b
    raise ValueError(f"Operador '{operador}' no reconocido. Usa: + - * /")


# ── Entrada ──────────────────────────────────────────────────
try:
    a = float(input("Primer número : "))
    operador = input("Operador (+ - * /): ").strip()
    b = float(input("Segundo número: "))

    resultado = calcular(a, operador, b)
    print(f"\nResultado: {a} {operador} {b} = {resultado:.4f}")

except ValueError as e:
    print(f"[Error de valor] {e}")
except ZeroDivisionError as e:
    print(f"[Error de división] {e}")
