"""
=============================================================
 RETO SEMANA 5 – Calculadora de Costo de Envío
=============================================================

ENUNCIADO:
  Dado el peso (kg) y la distancia (km) de un paquete, calcula
  el costo de envío usando constantes predefinidas de tarifa y
  un descuento escalonado según el monto total antes de impuesto.

RESTRICCIONES:
  - Peso  : 0.1 ≤ peso ≤ 500 kg (float).
  - Distancia: 1 ≤ distancia ≤ 10 000 km (float).
  - Las CONSTANTES no deben modificarse en el flujo del programa.

PISTA TÉCNICA:
  Combina múltiples expresiones en una sola línea usando
  operadores aritméticos y el operador ternario de Python:
      descuento = DCTO_15 if subtotal > 200 else (DCTO_10 if subtotal > 100 else 0)
  COSTO_BASE, TARIFA_KG, TARIFA_KM, IVA, DCTO_10, DCTO_15
  son todas constantes (convención: MAYÚSCULAS).
=============================================================
"""

# ── Constantes ───────────────────────────────────────────────
COSTO_BASE: float = 5.00       # tarifa mínima por envío (USD)
TARIFA_KG: float = 0.80        # USD por kilogramo
TARIFA_KM: float = 0.05        # USD por kilómetro
IVA: float = 0.16              # 16 %
DCTO_10: float = 0.10          # 10 % de descuento
DCTO_15: float = 0.15          # 15 % de descuento

# ── Entrada ──────────────────────────────────────────────────
peso = float(input("Peso del paquete (kg) : "))
distancia = float(input("Distancia de envío (km): "))

# ── Proceso (expresiones combinadas con constantes) ───────────
subtotal: float = COSTO_BASE + (TARIFA_KG * peso) + (TARIFA_KM * distancia)

porcentaje_descuento: float = (
    DCTO_15 if subtotal > 200
    else (DCTO_10 if subtotal > 100 else 0.0)
)

descuento: float = subtotal * porcentaje_descuento
base_gravable: float = subtotal - descuento
iva_monto: float = base_gravable * IVA
total: float = base_gravable + iva_monto

# ── Salida ───────────────────────────────────────────────────
print("\n========= Resumen de Envío =========")
print(f"  Peso          : {peso} kg")
print(f"  Distancia     : {distancia} km")
print(f"  Subtotal      : ${subtotal:.2f}")
print(f"  Descuento ({porcentaje_descuento * 100:.0f}%): -${descuento:.2f}")
print(f"  Base gravable : ${base_gravable:.2f}")
print(f"  IVA (16%)     : +${iva_monto:.2f}")
print(f"  TOTAL         : ${total:.2f}")
print("====================================")
