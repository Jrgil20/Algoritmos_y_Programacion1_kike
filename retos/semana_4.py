"""
=============================================================
 RETO SEMANA 4 – Validador de Contraseña Segura
=============================================================

ENUNCIADO:
  Lee una contraseña ingresada por el usuario y evalúa si es
  "Segura", "Media" o "Débil" según criterios combinando
  operadores lógicos (and, or, not) sobre tipos primitivos.

RESTRICCIONES:
  - Segura : longitud ≥ 10  AND  tiene dígito  AND  tiene
             mayúscula  AND  tiene minúscula  AND  tiene símbolo.
  - Media  : al menos 3 de los 5 criterios anteriores se cumplen.
  - Débil  : menos de 3 criterios cumplidos.
  - No uses librerías externas; solo str y operadores built-in.

PISTA TÉCNICA:
  any(c.isdigit() for c in pwd)  →  bool de "tiene dígito".
  Suma los bool (True == 1) para contar cuántos criterios pasa:
  puntaje = sum([crit1, crit2, crit3, crit4, crit5]).
=============================================================
"""

SIMBOLOS = set("!@#$%^&*()_+-=[]{}|;':\",./<>?")

# ── Entrada ──────────────────────────────────────────────────
pwd = input("Ingresa tu contraseña: ")

# ── Criterios (cada uno es bool) ─────────────────────────────
tiene_longitud = len(pwd) >= 10
tiene_digito = any(c.isdigit() for c in pwd)
tiene_mayuscula = any(c.isupper() for c in pwd)
tiene_minuscula = any(c.islower() for c in pwd)
tiene_simbolo = any(c in SIMBOLOS for c in pwd)

puntaje: int = sum([
    tiene_longitud,
    tiene_digito,
    tiene_mayuscula,
    tiene_minuscula,
    tiene_simbolo,
])

# ── Clasificación con operadores lógicos ─────────────────────
if puntaje == 5:
    nivel = "🔒 Segura"
elif puntaje >= 3:
    nivel = "⚠️  Media"
else:
    nivel = "❌ Débil"

# ── Salida ───────────────────────────────────────────────────
print(f"\nContraseña: {'*' * len(pwd)}")
print(f"  Longitud ≥ 10  : {tiene_longitud}")
print(f"  Tiene dígito   : {tiene_digito}")
print(f"  Tiene mayúscula: {tiene_mayuscula}")
print(f"  Tiene minúscula: {tiene_minuscula}")
print(f"  Tiene símbolo  : {tiene_simbolo}")
print(f"  Puntaje        : {puntaje}/5")
print(f"  Nivel          : {nivel}")
