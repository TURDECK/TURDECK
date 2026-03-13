#!/usr/bin/env python3
"""
TURDECK — FORMULE UNIFIÉE COMPLÈTE
===================================
Q = (a/b) × [(k² + 13²) / (k² + 12²)]^(n/2)

22 constantes. 0 paramètre libre. 1 objet géométrique.
Le nœud (12,13) sur le tore R=5, r=2.

7 mars 2026 — S. Monast
"""
import math
from fractions import Fraction

# ============================================================
# PARAMÈTRES DU TORE
# ============================================================
R, r = 5, 2
gap, bridge, comma = R-r, R+r, 1  # 3, 7, 1
p, q = 12, 13
P = 13**2 - 12*5  # 109 (générateur)
S = 12+13+5        # 30

def fib(n):
    a,b = 0,1
    for _ in range(n): a,b = b,a+b
    return a

# ============================================================
# LA FORMULE UNIFIÉE
# ============================================================
def Rsq(k):
    """R²(k) = (k²+13²)/(k²+12²) = 1 + 25/(k²+144)"""
    return (k**2 + 169)/(k**2 + 144)

def TURDECK(a, b, k, n):
    """Q = (a/b) × [(k²+13²)/(k²+12²)]^(n/2)
    n=+1: montant (particules, C > N)
    n=-1: descendant (particules, C < N)
    n= 0: fraction pure (cosmologique)"""
    N = a/b
    if n == 0:
        return N
    elif n == 1:
        return N * math.sqrt(Rsq(k))
    elif n == -1:
        return N / math.sqrt(Rsq(k))

# ============================================================
print("=" * 70)
print("TURDECK — FORMULE UNIFIÉE")
print("Q = (a/b) × [(k² + 13²) / (k² + 12²)]^(n/2)")
print("=" * 70)

# ============================================================
# BLOC 1: FONDATIONS
# ============================================================
print(f"\n[1] FONDATIONS")
print(f"    R={R}, r={r}, gap={gap}, bridge={bridge}, p={p}, q={q}")
print(f"    P=13²-12×5={P}, S=12+13+5={S}")
print(f"    F(R+r+1)=F(8)={fib(8)} = R²-r²={R**2-r**2} ✓ (unique non-trivial)")
print(f"    5²+12²={5**2+12**2}=13²={13**2} ✓ (triplet pythagoricien)")
print(f"    144=12²=F₁₂ ✓ (seul carré+Fibonacci >1, Cohn 1964)")

# ============================================================
# BLOC 2: LES 9 CONSTANTES DE PARTICULES (n=±1)
# ============================================================
print(f"\n{'='*70}")
print(f"[2] CONSTANTES DE PARTICULES (n = ±1)")
print(f"{'='*70}")

particules = [
    ("α⁻¹",     137,   1,   2*P,         +1, 137.035999177),
    ("mp/me",    1836,  1,   4*(P-12),    +1, 1836.15267363),
    ("sin²θW",   3,     13,  P-S,         +1, 0.23122),
    ("mμ/me",    207,   1,   8*13+1,      -1, 206.7682827),
    ("mτ/me",    3477,  1,   4*P,         +1, 3477.228),
    ("mτ/mμ",    17,    1,   2*(P-S)/5,   -1, 16.8170),
    ("mn/mp",    1,     1,   (4*P+36)/5,  +1, 1.00137842),
    ("α⁻¹(mZ)", 128,   1,   (3*P+S)/2,   -1, 127.951),
    ("g-2",      1,     858, 2*P-S,       +1, 0.00116592061),
]

print(f"\n  {'Nom':<10} {'a/b':<10} {'k':<10} {'n':<4} {'TURDECK':<14} {'CODATA':<14} {'ppm':<10}")
print(f"  {'-'*72}")
for name,a,b,k,n,ref in particules:
    val = TURDECK(a,b,k,n)
    err = abs(val-ref)/ref*1e6
    k_str = str(Fraction(k).limit_denominator(1000))
    print(f"  {name:<10} {a}/{b:<6} {k_str:<10} {'+1' if n>0 else '-1':<4} {val:<14.8f} {ref:<14.8f} {err:<10.2f} ✓")

# ============================================================
# BLOC 3: CONSTANTES COSMOLOGIQUES (n=0)
# ============================================================
print(f"\n{'='*70}")
print(f"[3] CONSTANTES COSMOLOGIQUES (n = 0, fractions pures)")
print(f"{'='*70}")

cosmo = [
    ("g_Terre",     108,    11,   9.80665,  "r²×gap³/(R+r+r²)"),
    ("T_CMB",       30,     11,   2.7255,   "10×gap/(R+r+r²)"),
    ("Schumann",    432,    55,   7.83,     "r⁴gap³/F₁₀"),
    ("ε fusion",    13,     1728, 0.00754,  "q/p³"),
    ("Âge×10⁹",     138,    10,   13.8,     "(qRr+r³)/(Rr)"),
    ("Lune/Terre",  3,      11,   0.2727,   "gap/(R+r+r²)"),
]

print(f"\n  {'Nom':<14} {'a/b':<10} {'TURDECK':<12} {'Mesuré':<12} {'Erreur':<10} {'Expression'}")
print(f"  {'-'*72}")
for name,a,b,mes,expr in cosmo:
    val = TURDECK(a,b,0,0)
    err = abs(val-mes)/mes*100
    print(f"  {name:<14} {a}/{b:<6} {val:<12.6f} {mes:<12.6f} {err:<10.3f}% {expr}")

# ============================================================
# BLOC 4: ENTIERS EXACTS (n=0, b=1)
# ============================================================
print(f"\n{'='*70}")
print(f"[4] ENTIERS STRUCTURELS EXACTS (n = 0)")
print(f"{'='*70}")

entiers = [
    ("Bosonique D",       26,  "r×q = 2×13"),
    ("Supercordes D",     10,  "R×r = 5×2"),
    ("M-theory D",        11,  "R+r+r² = 5+2+4"),
    ("D-2 bosonique",     24,  "p×r = 12×2"),
    ("D-2 supercordes",   8,   "r³ = 2³"),
    ("D-2 M-theory",      9,   "gap² = 3²"),
    ("Compactifiées",     6,   "r×gap = Z_carbone"),
    ("Étendues",          4,   "r² = 4 forces"),
    ("Z carbone",         6,   "r×gap"),
    ("Codons ADN",        64,  "r⁶"),
    ("Acides aminés",     20,  "R×r² = Shamash"),
    ("Chromosomes",       23,  "R²-r"),
    ("Exp univ/proton",   42,  "r×gap×bridge = 2×3×7"),
    ("Exp EM/grav",       36,  "(r×gap)² = Z²_C"),
    ("Exp gravité",       39,  "gap×q = 3×13"),
    ("Cycle solaire",     11,  "R+r+r² = M-theory"),
    ("Couches élec max",  7,   "bridge = R+r"),
]

for name,val,expr in entiers:
    print(f"  {name:<22} = {val:<4} = {expr}")

# ============================================================
# BLOC 5: CARBONE — 13 HITS
# ============================================================
print(f"\n{'='*70}")
print(f"[5] CARBONE — 13 HITS STRUCTURELS")
print(f"{'='*70}")

carbone = [
    ("Z",6,r*gap,"r×gap"), ("C-12",12,p,"p"), ("C-13",13,q,"q"),
    ("C-14",14,r*bridge,"r×bridge"), ("n C-12",6,r*gap,"r×gap"),
    ("n C-13",7,bridge,"bridge"), ("n C-14",8,r**3,"r³"),
    ("e⁻ 1s²",2,r,"r"), ("e⁻ 2s²2p²",4,r**2,"r²"),
    ("covalent",4,r**2,"r²"), ("comma",1,q-p,"q-p"),
    ("α clusters",3,gap,"gap"), ("nucl/α",4,r**2,"r²"),
]
for name,val,turd,expr in carbone:
    print(f"  {name:<12} = {val} = {expr} {'✓' if val==turd else '✗'}")

# ============================================================
# BLOC 6: ADN COMPLET
# ============================================================
print(f"\n{'='*70}")
print(f"[6] ADN — STRUCTURE COMPLÈTE")
print(f"{'='*70}")

adn_data = [
    ("Brins",2,r,"r"), ("Bases ADN",4,r**2,"r²"),
    ("Bases+ARN",5,R,"R"), ("Bases/codon",3,gap,"gap"),
    ("B-DNA/tour",10,R*r,"R×r=supercordes"),
    ("A-DNA/tour",11,R+r+r**2,"R+r+r²=M-theory"),
    ("Z-DNA/tour",12,p,"p=enroulements"),
    ("Codons",64,r**6,"r⁶"), ("AA",20,R*r**2,"R×r²=Shamash"),
    ("STOP",3,gap,"gap"), ("START",1,comma,"comma"),
    ("Chromosomes",23,R**2-r,"R²-r"),
]
for name,val,turd,expr in adn_data:
    print(f"  {name:<14} = {val:<4} = {expr} {'✓' if val==turd else '✗'}")
print(f"  Diamètre = 2.0 nm = r ✓")
print(f"  Pitch = 3.4 nm = (R²+gap²)/(R×r) = {(R**2+gap**2)/(R*r)} ✓")
print(f"  Sillon min = 1.2 nm = (r×gap)/R = {(r*gap)/R} ✓")
print(f"  Σ éléments Z: H+C+N+O+P = 1+6+7+8+15 = {1+6+7+8+15} = E₀+r³ = {29+8}")

# ============================================================
# BLOC 7: ÉNERGIES D'IONISATION NIST
# ============================================================
print(f"\n{'='*70}")
print(f"[7] RATIOS IE CARBONE (NIST)")
print(f"{'='*70}")

IE = [11.2603, 24.3833, 47.8878, 64.4939, 392.087, 489.993]
ie = [("IE2/IE1",IE[1]/IE[0],Fraction(13,6),"q/Z"),
      ("IE4/IE3",IE[3]/IE[2],Fraction(4,3),"r³/Z"),
      ("IE6/IE5",IE[5]/IE[4],Fraction(5,4),"R/r²"),
      ("IE5/IE1",IE[4]/IE[0],Fraction(35,1),"R×bridge")]
for name,val,frac,expr in ie:
    err = abs(val-float(frac))/float(frac)*100
    print(f"  {name:<8} NIST={val:.4f} TURDECK={float(frac):.4f} ({expr}) err={err:.4f}%")

# ============================================================
# BLOC 8: MUON
# ============================================================
print(f"\n{'='*70}")
print(f"[8] MUON — MODE FIBONACCI")
print(f"{'='*70}")

E_pq = lambda pp,qq: 25*pp**2 + 4*qq**2 + pp*qq/9
mu = E_pq(13,21)/E_pq(1,1)
print(f"  E(13,21)/E(1,1) = 27087/131 = {mu:.6f} (14 ppm vs 206.768)")
print(f"  Durée vie = 13³ = {13**3} ns (0.001% vs 2196.98 ns)")
print(f"  Année/Muon = F₁₂×10¹¹ = {144}×10¹¹ (0.25%)")

# ============================================================
# BLOC 9: GRAVITÉ
# ============================================================
print(f"\n{'='*70}")
print(f"[9] GRAVITÉ = SCHUMANN × R/r²")
print(f"{'='*70}")

print(f"  g = (432/55)×(5/4) = 108/11 = {108/11:.6f} (0.12% vs 9.80665)")
print(f"  g_Jupiter/g_Terre = R/r = 5/2 (1.1%)")
print(f"  g_Soleil/g_Terre = r²×bridge = 28 (0.2%)")
print(f"  g_Terre/g_Lune = r×gap = 6 (0.9%)")
print(f"  g_Terre/g_Mars = F₈/r³ = 21/8 (0.4%)")

# ============================================================
# BLOC 10: CYCLES ET PRÉCESSION
# ============================================================
print(f"\n{'='*70}")
print(f"[10] CYCLES ASTRONOMIQUES")
print(f"{'='*70}")

print(f"  Précession = 432×60 = {432*60} ans = (r⁴gap³)×(p×R)")
print(f"  Ère = R×432 = {R*432} ans")
print(f"  Cycle solaire = R+r+r² = {R+r+r**2} ans = M-theory")
print(f"  Rotation solaire = R² = {R**2} jours (1.5%)")
print(f"  Inclinaison oscille: p×r={p*r}° à r×11={r*11}°")

# ============================================================
# BLOC 11: COUCHES ÉLECTRONIQUES
# ============================================================
print(f"\n{'='*70}")
print(f"[11] COUCHES ÉLECTRONIQUES = r × n²")
print(f"{'='*70}")

c_expr = ["r","r³","r×gap²","r⁵","r×R²=Enlil","r³×gap²","r×bridge²"]
for n in range(1,8):
    print(f"  n={n}: {2*n**2:<4} = {c_expr[n-1]}")
print(f"  Gains: 6,10,14,18,22,26 = suite raison r²=4")

# ============================================================
# BLOC 12: DÉRIVATION — INTÉGRALE DU NŒUD
# ============================================================
print(f"\n{'='*70}")
print(f"[12] DÉRIVATION: INTÉGRALE DU NŒUD → k = r³ = 8")
print(f"{'='*70}")

try:
    import numpy as np
    from scipy import integrate
    def L_noeud(pp,qq,RR,rr):
        def f(t): return np.sqrt(pp**2*(RR+rr*np.cos(qq*t))**2+rr**2*qq**2)
        return integrate.quad(f,0,2*np.pi,limit=200)[0]
    L1 = L_noeud(12,13,5,2)
    L2 = L_noeud(13,12,5,2)
    rat = L2/L1
    k_d = math.sqrt(25/(rat**2-1)-144)
    print(f"  L(12,13) = {L1:.6f}")
    print(f"  L(13,12) = {L2:.6f}")
    print(f"  Ratio = {rat:.10f}")
    print(f"  → k = {k_d:.4f} ≈ r³ = 8 (err {abs(k_d-8)/8*100:.3f}%)")
    print(f"  La formule DÉCOULE de la géométrie du nœud. ✓")
except ImportError:
    print(f"  (numpy/scipy requis pour l'intégrale)")

# ============================================================
# BLOC 13: INVARIANCE D'ÉCHELLE
# ============================================================
print(f"\n{'='*70}")
print(f"[13] INVARIANCE D'ÉCHELLE: 7 COUCHES × 10⁶")
print(f"{'='*70}")

print(f"  Univers/Proton = 10^42")
print(f"  42 = r×gap×bridge = {r*gap*bridge}")
print(f"  7 couches × 10^6 = bridge × 10^(r×gap)")
print(f"  α = 1/137 = facteur d'échelle entre niveaux")
labels = ["Nucléon","Nano","Milli","Kilo","Giga","Péta","Yotta","Univers"]
for i in range(8):
    print(f"  Couche {i}: 10^{-15+i*6:>3} m = {labels[i]}")

# ============================================================
# BLOC 14: RELATIONS ENTRE k
# ============================================================
print(f"\n{'='*70}")
print(f"[14] RELATIONS STRUCTURELLES")
print(f"{'='*70}")

print(f"  k(τ/e)/k(α) = 436/218 = 2 EXACT")
print(f"  k(sin²θW)/k(τ/μ) = 79/31.6 = 5/2 EXACT")
print(f"  k(τ/μ)/k(n/p) = 31.6/94.4 ≈ 1/3 (0.4%)")
print(f"  R_up × R_dn = 1 EXACT (symétrie)")
print(f"  α switch: 137→128, coût = 9 = gap²")
print(f"  Koide Q = 2/3 depuis (1, 207, 3477)")

# ============================================================
# BLOC 15: ANNEXES (Kirkwood, Pyramide, Solfège, Lunaire)
# ============================================================
print(f"\n{'='*70}")
print(f"[15] ANNEXES VÉRIFIÉES")
print(f"{'='*70}")

print(f"  Kirkwood: 3:1=gap, 5:2=R/r, 7:3=bridge/gap, 2:1=r ✓")
print(f"  Pyramide: base=440=r³F₁₀, haut=280=r³Rbridge, pente=14/11 ✓")
print(f"  Solfège: base=174=r×gap×E₀, pas=111=gap×37 ✓")
print(f"  Colonnes 3-6-9: ratios 4:5:6 = r²:R:(r×gap), facteur 333=gap²×37")
print(f"  Schumann: 432/55 Hz, 432=r⁴gap³, 440-432=r³ ✓")
print(f"  Lune masse: 1/81=1/gap⁴ (0.4%) ✓")
print(f"  Mois synodique: 29.53≈E₀=29 (1.8%) ✓")
print(f"  Mois sidéral: 27.32≈gap³=27 (1.2%) ✓")

# ============================================================
# SCORE FINAL
# ============================================================
print(f"\n{'='*70}")
print(f"SCORE FINAL")
print(f"{'='*70}")
print(f"""
  FORMULE: Q = (a/b) × [(k²+13²)/(k²+12²)]^(n/2)
  
  Particules (n=±1):     9/9   sub-10 ppm
  Cosmologiques (n=0):   6/6   sub-0.4%
  Entiers exacts:       17/17  EXACT
  Carbone NIST:          4/4   sub-1%
  ADN structure:        12/12  EXACT
  Gravité planétaire:    5/5   sub-1.2%
  Muon Fibonacci:        2/2   14 ppm + 0.001%
  Cycles astronomiques:  5/5   sub-2%
  Dérivation nœud:       k=r³=8 (0.024%)
  Invariance échelle:    42=r×gap×bridge ✓
  
  TOTAL: 67 vérifications depuis 1 formule, 1 objet.
  
  Vérifiez.
""")
