# Fault-Analysis-of-a-Power-System-
import cmath
import math

# ============================================================
# FAULT ANALYSIS OF A POWER SYSTEM
# Using Symmetrical Components
# ============================================================

print("=" * 60)
print("       POWER SYSTEM FAULT ANALYSIS")
print("=" * 60)

# ------------------------------------------------------------
# INPUT DATA
# ------------------------------------------------------------

# Prefault voltage in per unit
V_prefault = 1.0

# Sequence impedances in per unit
Z1 = complex(0.20, 0.60)   # Positive sequence impedance
Z2 = complex(0.20, 0.60)   # Negative sequence impedance
Z0 = complex(0.05, 0.20)   # Zero sequence impedance

# Fault impedance in per unit
Zf = complex(0.0, 0.0)

# ------------------------------------------------------------
# UTILITY FUNCTIONS
# ------------------------------------------------------------

def polar(z):
    """Return magnitude and angle in degrees."""
    magnitude = abs(z)
    angle = math.degrees(cmath.phase(z))
    return magnitude, angle


def display_current(name, current):
    mag, angle = polar(current)
    print(f"{name:<10} = {mag:.4f} ∠ {angle:.2f}° p.u.")


# ------------------------------------------------------------
# 1. THREE-PHASE FAULT
# ------------------------------------------------------------

def three_phase_fault():
    print("\n" + "-" * 60)
    print("1. THREE-PHASE FAULT")
    print("-" * 60)

    # Fault current
    Ia = V_prefault / (Z1 + Zf)

    # For a balanced 3-phase fault:
    # Ib = a^2 Ia
    # Ic = a Ia

    a = cmath.exp(1j * 2 * math.pi / 3)

    Ib = a**2 * Ia
    Ic = a * Ia

    display_current("Ia", Ia)
    display_current("Ib", Ib)
    display_current("Ic", Ic)

    return Ia, Ib, Ic


# ------------------------------------------------------------
# 2. SINGLE LINE-TO-GROUND FAULT
# ------------------------------------------------------------

def lg_fault():
    print("\n" + "-" * 60)
    print("2. SINGLE LINE-TO-GROUND (LG) FAULT")
    print("-" * 60)

    # For an A-G fault:
    #
    # I1 = I2 = I0
    #
    # Ia = 3I0

    I1 = V_prefault / (Z1 + Z2 + Z0 + 3 * Zf)

    I2 = I1
    I0 = I1

    Ia = I0 + I1 + I2
    Ib = 0
    Ic = 0

    display_current("I0", I0)
    display_current("I1", I1)
    display_current("I2", I2)

    print("\nPhase currents:")
    display_current("Ia", Ia)
    display_current("Ib", Ib)
    display_current("Ic", Ic)

    return Ia, Ib, Ic


# ------------------------------------------------------------
# 3. LINE-TO-LINE FAULT
# ------------------------------------------------------------

def ll_fault():
    print("\n" + "-" * 60)
    print("3. LINE-TO-LINE (LL) FAULT")
    print("-" * 60)

    # For a B-C fault:
    #
    # I0 = 0
    # I1 = V / (Z1 + Z2 + Zf)
    # I2 = -I1

    a = cmath.exp(1j * 2 * math.pi / 3)

    I1 = V_prefault / (Z1 + Z2 + Zf)
    I2 = -I1
    I0 = 0

    # Phase currents
    Ia = I0 + I1 + I2

    Ib = I0 + (a**2) * I1 + a * I2
    Ic = I0 + a * I1 + (a**2) * I2

    print("Sequence currents:")
    display_current("I0", I0)
    display_current("I1", I1)
    display_current("I2", I2)

    print("\nPhase currents:")
    display_current("Ia", Ia)
    display_current("Ib", Ib)
    display_current("Ic", Ic)

    return Ia, Ib, Ic


# ------------------------------------------------------------
# 4. DOUBLE LINE-TO-GROUND FAULT
# ------------------------------------------------------------

def llg_fault():
    print("\n" + "-" * 60)
    print("4. DOUBLE LINE-TO-GROUND (LLG) FAULT")
    print("-" * 60)

    # For a B-C-G fault:
    #
    # Calculate equivalent impedance of Z2 and Z0
    # in parallel.

    Z_parallel = (Z2 * Z0) / (Z2 + Z0)

    I1 = V_prefault / (Z1 + Z_parallel + Zf)

    # Voltage at fault point
    V1 = V_prefault - I1 * Z1

    I2 = -V1 / Z2
    I0 = -V1 / Z0

    a = cmath.exp(1j * 2 * math.pi / 3)

    # Phase currents
    Ia = I0 + I1 + I2

    Ib = I0 + (a**2) * I1 + a * I2

    Ic = I0 + a * I1 + (a**2) * I2

    print("Sequence currents:")
    display_current("I0", I0)
    display_current("I1", I1)
    display_current("I2", I2)

    print("\nPhase currents:")
    display_current("Ia", Ia)
    display_current("Ib", Ib)
    display_current("Ic", Ic)

    return Ia, Ib, Ic


# ============================================================
# MAIN PROGRAM
# ============================================================

three_phase_fault()
lg_fault()
ll_fault()
llg_fault()

print("\n" + "=" * 60)
print("             FAULT ANALYSIS COMPLETED")
print("=" * 60)
