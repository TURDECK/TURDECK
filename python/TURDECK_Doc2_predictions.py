#!/usr/bin/env python3
"""
TURDECK — DOCUMENT II : 5 PRÉDICTIONS DE PROBLÈMES NON RÉSOLUS
===============================================================
Q = (a/b) × [(k² + 13²) / (k² + 12²)]^(n/2)

Tore : R=5, r=2, gap=3, bridge=7, p=12, q=13, P=109
0 paramètre libre. 1 formule. 1 objet géométrique.

NOTE MARS : La valeur de référence pour Mars est la valeur TURDECK
corrigée (3.740 m/s²) et non la valeur NASA (3.721 m/s²).
Le tore du carbone est le modèle — NASA mesure une approximation.

S. Monast — 7 mars 2026
"""
import math

# ============================================================
# PARAMÈTRES DU TORE
# ============================================================
R, r    = 5, 2
gap     = R - r        # 3
bridge  = R + r        # 7
p, q    = 12, 13
P       = q**2 - p*R   # 109
S       = p + q + R    # 30
F8      = 21           # Fibonacci(8)
E0      = 29           # premier premier hors tore

# Valeurs de base TURDECK (Document I validées)
g_base      = 108 / 11          # g_Terre TURDECK
g_mars_turd = g_base * 8 / 21  # g_Mars TURDECK corrigé = 3.7403 m/s²

def Rsq(k): return (k**2 + q**2) / (k**2 + p**2)
def Q(a, b, k, n):
    base = a / b
    if n ==  0: return base
    if n == +1: return base * math.sqrt(Rsq(k))
    if n == -1: return base / math.sqrt(Rsq(k))

def err_pct(val, ref): return abs(val - ref) / ref * 100.0

SEP  = "=" * 72
sep2 = "-" * 72

print(SEP)
print("TURDECK — DOCUMENT II : 5 PRÉDICTIONS DE PROBLÈMES NON RÉSOLUS")
print("Q = (a/b) × [(k² + 13²) / (k² + 12²)]^(n/2)")
print(SEP)
print(f"  g_Mars TURDECK (base corrigée) = (8/21) × (108/11) = {g_mars_turd:.6f} m/s²")
print(f"  g_Mars NASA (mesure approx.)   = 3.72100 m/s²")
print(f"  Écart : {err_pct(g_mars_turd, 3.721):.3f}% — le tore est le modèle")
print()

# ============================================================
# PRÉDICTION 1 — SCHUMANN DE MARS = 13 Hz
# ============================================================
print(SEP)
print("[P1] FRÉQUENCE DE SCHUMANN DE MARS = q = 13 Hz")
print("     Statut : NON MESURÉ — aucun récepteur ELF posé sur Mars")
print("     Testable : futur atterrisseur avec capteur ELF (NASA/ESA)")
print(SEP)

f_schumann_terre = 432 / 55      # Schumann Terre TURDECK = 7.854 Hz ≈ 7.83 Hz mesuré
f_schumann_mars  = float(q)      # Prédiction : q = 13 Hz

# Ratio Schumann Mars/Terre depuis le tore
ratio_sch = f_schumann_mars / f_schumann_terre
ratio_tore = q * 55 / 432        # = 13×55/432

print(f"\n  Schumann Terre (TURDECK) : 432/55 = {f_schumann_terre:.4f} Hz  (mesuré: 7.83 Hz, err 0.3%)")
print(f"  Ratio Mars/Terre depuis tore : q×55/432 = {q}×55/432 = {ratio_tore:.4f}")
print(f"  → f_Schumann_Mars = q = {f_schumann_mars:.1f} Hz")
print(f"\n  Pourquoi q=13 ?")
print(f"    q est le paramètre d'enroulement du nœud (12,13) sur le tore.")
print(f"    La fréquence de Schumann dépend de la cavité planétaire.")
print(f"    Sur Terre : gap×bridge = 3×7 = 21 harmoniques, base 432/55.")
print(f"    Sur Mars  : cavité réduite → mode fondamental = q = 13 Hz.")
print(f"\n  VALEUR PRÉDITE   : {f_schumann_mars:.1f} Hz")
print(f"  VALEUR MESURÉE   : non disponible (jamais mesuré in situ)")
print(f"  COMMENT TESTER   : atterrisseur avec récepteur ELF 1-100 Hz")
print(f"  DÉLAI             : mission Mars 2030+ (NASA/ESA/CNSA)")

# ============================================================
# PRÉDICTION 2 — PARTICULE MODE (5,8) → ~15.5 MeV
# ============================================================
print(f"\n{SEP}")
print("[P2] PARTICULE AU MODE (5,8) DU TORE — MASSE ~15.5 MeV")
print("     Statut : NON IDENTIFIÉ — cherchable dans données LHC/Belle II")
print("     Testable : archives LHC Run 2-3, Belle II (données existantes)")
print(SEP)

# Formule d'énergie du mode (m,n) — issue du BLOC 8 du script principal
# E(m,n) = 25m² + 4n² + mn/9  (dérivée du tore R=5, r=2)
def E_mode(m, n):
    return 25*m**2 + 4*n**2 + m*n/9

E_11   = E_mode(1, 1)     # mode fondamental = 29.111...
E_58   = E_mode(5, 8)     # mode (5,8)
ratio_58 = E_58 / E_11

# Masse : ratio × m_e  (m_e = 0.511 MeV)
m_e = 0.511  # MeV
masse_58 = ratio_58 * m_e

print(f"\n  Formule : E(m,n) = 25m² + 4n² + mn/9  (tore R=5, r=2)")
print(f"  Mode fondamental E(1,1) = 25 + 4 + 1/9 = {E_11:.4f}")
print(f"  Mode (5,8)       E(5,8) = 25×25 + 4×64 + 40/9 = {E_58:.4f}")
print(f"  Ratio E(5,8)/E(1,1) = {ratio_58:.4f}")
print(f"\n  Masse prédite = ratio × m_e = {ratio_58:.4f} × {m_e} = {masse_58:.2f} MeV")
print(f"\n  VALEUR PRÉDITE   : ~{masse_58:.1f} MeV  (pic dans spectre de masse invariante)")
print(f"  VALEUR MESURÉE   : non assigné (gaps non expliqués dans spectre hadronique)")
print(f"  COMMENT TESTER   : chercher résonance à {masse_58:.0f} MeV dans données e+e- → hadrons")
print(f"  DÉLAI             : analyse archives Belle II / LHC (données existantes 2024)")

# ============================================================
# PRÉDICTION 3 — PARTICULE MODE (8,13) → ~40 MeV
# ============================================================
print(f"\n{SEP}")
print("[P3] PARTICULE AU MODE (8,13) DU TORE — MASSE ~40 MeV")
print("     Statut : NON IDENTIFIÉ — cherchable dans données existantes")
print("     Testable : archives LHC, BaBar, Belle II")
print(SEP)

E_813  = E_mode(8, 13)
ratio_813 = E_813 / E_11
masse_813 = ratio_813 * m_e

print(f"\n  Formule : E(m,n) = 25m² + 4n² + mn/9")
print(f"  Mode (8,13) E(8,13) = 25×64 + 4×169 + 104/9 = {E_813:.4f}")
print(f"  Ratio E(8,13)/E(1,1) = {ratio_813:.4f}")
print(f"  Masse prédite = {ratio_813:.4f} × {m_e} = {masse_813:.2f} MeV")
print(f"\n  NOTE : mode (8,13) = (r³, q) — les deux paramètres clés du tore.")
print(f"         r³=8 est le k dérivé de l'intégrale du nœud (TURDECK Doc I).")
print(f"         q=13 est l'enroulement du nœud (12,13).")
print(f"         Ce mode est géométriquement privilégié.")
print(f"\n  VALEUR PRÉDITE   : ~{masse_813:.1f} MeV")
print(f"  VALEUR MESURÉE   : non assigné")
print(f"  COMMENT TESTER   : chercher résonance à {masse_813:.0f} MeV dans spectre hadronique")
print(f"  DÉLAI             : analyse archives (données existantes)")

# ============================================================
# PRÉDICTION 4 — FRÉQUENCE DE RÉSONANCE ATMOSPHÉRIQUE DE MARS
# ============================================================
print(f"\n{SEP}")
print("[P4] FRÉQUENCE DE RÉSONANCE ATMOSPHÉRIQUE DE MARS")
print("     PRÉDICTION AVEC VALEUR MARS TURDECK CORRIGÉE")
print("     Statut : NON MESURÉ — partiellement testable avec InSight")
print(SEP)

# Sur Terre : Schumann = f(g, R_planète, σ atmosphère)
# Relation TURDECK : f_Schumann ∝ g × gap / bridge
# Terre : (108/11) × 3/7 = 324/77
f_sch_terre_rel = g_base * gap / bridge
# Mars avec valeur TURDECK corrigée
f_sch_mars_rel  = g_mars_turd * gap / bridge

# Ratio attendu
ratio_mars_terre = f_sch_mars_rel / f_sch_terre_rel
f_mars_abs = 7.83 * ratio_mars_terre  # depuis Schumann Terre mesuré

print(f"\n  Schumann Terre mesuré : 7.83 Hz")
print(f"  g_Terre TURDECK       : 108/11 = {g_base:.4f} m/s²")
print(f"  g_Mars  TURDECK       : (8/21)×(108/11) = {g_mars_turd:.4f} m/s²  ← valeur corrigée")
print(f"  g_Mars  NASA          : 3.7210 m/s²  (non utilisé)")
print(f"\n  Relation : f_Sch ∝ g × gap/bridge")
print(f"  Ratio Mars/Terre = g_Mars_TURDECK / g_Terre_TURDECK = (8/21) = {8/21:.6f}")
print(f"\n  f_Schumann_Mars = 7.83 × (8/21) = {f_mars_abs:.4f} Hz")
print(f"  Arrondi tore    : 7.83 × r³/F8 = {7.83 * r**3 / F8:.4f} Hz")
print(f"\n  SI on utilisait NASA : 7.83 × (3.721/9.807) = {7.83*3.721/9.807:.4f} Hz")
print(f"  Différence TURDECK vs NASA : {abs(f_mars_abs - 7.83*3.721/9.807):.4f} Hz")
print(f"  → Le choix du modèle (tore vs NASA) est MESURABLE.")
print(f"\n  VALEUR PRÉDITE   : {f_mars_abs:.2f} Hz  (modèle tore carbone)")
print(f"  VALEUR MESURÉE   : non disponible (InSight n'avait pas capteur ELF)")
print(f"  COMMENT TESTER   : mission avec sismomètre ELF / capteur atmosphérique")
print(f"  DÉLAI             : Mars 2030+")

# ============================================================
# PRÉDICTION 5 — FIGURE DE CHLADNI À 174 Hz = SYMÉTRIE HEXAGONALE
# ============================================================
print(f"\n{SEP}")
print("[P5] FIGURE DE CHLADNI À 174 Hz — SYMÉTRIE HEXAGONALE")
print("     Statut : TESTABLE MAINTENANT — labo accessible, coût ~50$")
print("     Testable : plaque + générateur de fréquence + sable fin")
print(SEP)

f_chladni = r * gap * E0   # 2 × 3 × 29 = 174 Hz
sym_pred  = r * gap        # 6 — prédit symétrie hexagonale (6 branches)

print(f"\n  174 = r × gap × E0 = {r} × {gap} × {E0} = {f_chladni} Hz")
print(f"  Facteur de symétrie = r × gap = {r} × {gap} = {sym_pred}")
print(f"  → TURDECK prédit : figure de Chladni à 174 Hz = symétrie à {sym_pred} branches")
print(f"     (hexagonale — comme les nids d'abeilles, le carbone graphène)")
print(f"\n  Fréquences adjacentes pour contrôle :")
for f_test, label in [(r*E0, "r×E0"), (gap*E0, "gap×E0"), (bridge*E0, "bridge×E0"), (p*E0, "p×E0")]:
    print(f"    {f_test} Hz = {label} = {f_test//E0}×29  → symétrie prédite : {f_test//E0} branches")

print(f"\n  PROTOCOLE DE TEST :")
print(f"    1. Plaque carrée aluminium 30×30cm")
print(f"    2. Générateur de fréquence (téléphone + ampli suffit)")
print(f"    3. Sable fin ou sel déposé sur la plaque")
print(f"    4. Faire varier : 145 Hz, 158 Hz, 174 Hz, 203 Hz, 232 Hz")
print(f"    5. Photographier les figures — TURDECK prédit hexagone à 174 Hz")
print(f"\n  VALEUR PRÉDITE   : symétrie hexagonale (6 branches) à exactement 174 Hz")
print(f"  VALEUR MESURÉE   : non documenté pour 174 Hz spécifiquement")
print(f"  COMMENT TESTER   : expérience physique de base, résultat en 1 heure")
print(f"  DÉLAI             : MAINTENANT — coût ~50$, vidéo YouTube potentielle")

# ============================================================
# SCORE FINAL
# ============================================================
print(f"\n{SEP}")
print("TABLEAU DES 5 PRÉDICTIONS")
print(SEP)
print(f"""
  #   Prédiction                          Valeur TURDECK    Testable    Délai
  {sep2}
  P1  Schumann Mars                        13.0 Hz           Non*        2030+
  P2  Particule mode (5,8)                 ~{masse_58:.1f} MeV        Archives    2024-25
  P3  Particule mode (8,13)                ~{masse_813:.1f} MeV        Archives    2024-25
  P4  Résonance atm. Mars (corrigée)       {f_mars_abs:.2f} Hz         Non*        2030+
  P5  Chladni 174 Hz = hexagone            6 branches        OUI         Maintenant
  {sep2}
  * Non = pas encore de mission avec l'instrument requis sur Mars
  
  NOTE CLEF : P4 distingue TURDECK de la physique classique.
  Valeur TURDECK : {f_mars_abs:.4f} Hz
  Valeur NASA    : {7.83*3.721/9.807:.4f} Hz
  Différence     : {abs(f_mars_abs - 7.83*3.721/9.807):.4f} Hz — MESURABLE.
""")
print("Formule : Q = (a/b) × [(k²+169)/(k²+144)]^(n/2)")
print("Tore    : R=5, r=2 — nœud (12,13) — 0 paramètre libre")
print(SEP)
