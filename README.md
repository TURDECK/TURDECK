# TURDECK

**Ten fundamental constants, five domains, zero free parameters.**
**A unique torus knot (12, 13) on the torus R = 5, r = 2.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18968359.svg)](https://doi.org/10.5281/zenodo.18968359)

**Author:** Sébastien Monast — Independent researcher, Mirabel, QC, Canada
**Version:** 1.0 — March 2026
**License:** CC-BY 4.0

---

## The Formula

```
Q = (a/b) × [(k² + 13²) / (k² + 12²)]^(n/2)
```

A single algebraic formula that reproduces **ten fundamental constants** across **five independent domains** of physics — with **zero free parameters**.

| Domain | Constants | Precision |
|---|---|---|
| Particles | α, mp/me, lepton masses, sin²θ_W, g−2 | 0.13 – 7.71 ppm |
| Cosmology | T(CMB), age of universe, Hubble tension, fusion ε | 0.032 – 0.22% |
| Gravity | g(Earth), g(Mars), 5 celestial bodies | 0.12 – 1.01% |
| Biology | B-form DNA (3 parameters) | EXACT |
| Electroweak | Weak mixing angle | 0.0002% |

**Combined coincidence probability: P(chance) = 5 × 10⁻⁶**

---

## The Torus

The torus R = 5, r = 2 is the **unique** non-degenerate torus simultaneously satisfying:

1. **Fibonacci selection:** F(R+r+1) = R² − r²
2. **Pythagorean triple:** 5² + 12² = 13²
3. **Knot coprimality:** gcd(12, 13) = 1

Verified by exhaustion (R < 100) and Monte Carlo over 10⁶ random tori.

### Torus Parameters

| Symbol | Value | Meaning |
|---|---|---|
| R | 5 | Major radius — Venus–Earth conjunctions |
| r | 2 | Minor radius — Unique by Fibonacci |
| gap | 3 | R − r |
| bridge | 7 | R + r |
| p | 12 | Meridional windings — synodic months |
| q | 13 | Longitudinal windings — Venus orbits |
| P | 109 | q² − p×R — also R(Sun)/R(Earth) = 109.2 |
| S | 30 | p + q + R |

---

## The 10 Retrodictions

| # | Constant | a/b | k | n | TURDECK | Reference | Error |
|---|---|---|---|---|---|---|---|
| R1 | α⁻¹ | 137 | 218 | +1 | 137.03592 | 137.03600 | 0.57 ppm |
| R2 | mp/me | 1836 | 388 | +1 | 1836.1523 | 1836.1527 | 0.21 ppm |
| R3 | mτ/me | 3477 | 436 | +1 | 3477.2285 | 3477.228 | 0.13 ppm |
| R4 | T(CMB) | 30/11 | — | 0 | 2.7273 K | 2.7255 K | 0.065% |
| R5 | Age universe | 138/10 | — | 0 | 13.8 Gyr | 13.8 Gyr | EXACT |
| R6 | Hubble ratio | 13/12 | — | 0 | 1.08333 | 1.08368 | 0.032% |
| R7 | g(Earth) | 108/11 | — | 0 | 9.818 | 9.807 | 0.118% |
| R8 | g(Mars) | (108/11)×8/21 | — | 0 | 3.740 | 3.721 | 0.518% |
| R9 | B-DNA | R×r, r, 34/10 | — | 0 | 10, 2, 3.4 | 10, 2, 3.4 | EXACT |
| R10 | sin²θ_W | 3/13 | 79 | +1 | 0.23122 | 0.23122 | 0.0002% |

---

## Five Testable Predictions

| # | Prediction | Method |
|---|---|---|
| P1 | Mars Schumann frequency = 13 Hz | Future lander with ELF sensor |
| P2 | Particle mode (5,8) → 15.5 MeV | LHC Run 2-3 / Belle II archives |
| P3 | Particle mode (8,13) → 40.2 MeV | LHC Run 2-3 / Belle II archives |
| P4 | Mars atmospheric resonance = 2.98 Hz | Future Mars mission |
| P5 | Chladni figure at 174 Hz = hexagonal symmetry | **Testable now** — aluminum plate + frequency generator + sand |

---

## Validation

- **Monte Carlo:** 10⁶ random tori tested. Only (5, 2, 12, 13) satisfies all 8 constants simultaneously. Best non-TURDECK score: 5/8.
- **Permutation test:** Only 1 of 24 possible k-assignments passes thresholds.
- **Out-of-sample:** Muon g−2 (not in original dataset) confirmed at 7.71 ppm vs Fermilab 2025.

---

## Repository Contents

| File | Description |
|---|---|
| `TURDECK_v1_EN_Final.pdf` | Full paper — English |
| `TURDECK_v1_FR.pdf` | Full paper — French |
| `python/TURDECK_Doc1_10_retrodictions.py` | Verifies all 10 retrodictions |
| `python/TURDECK_Doc2_predictions.py` | Computes 5 testable predictions |
| `python/TURDECK_confinement_muon.py` | Models the lepton confinement mechanism |

**Prerequisite:** `numpy`
**Run:** `python3 <script>.py`

---

## Citation

```bibtex
@misc{monast2026turdeck,
  author       = {Monast, Sébastien},
  title        = {{TURDECK — Ten fundamental constants, five domains, zero free parameters. A unique torus knot (12,13) on the torus R=5, r=2}},
  year         = {2026},
  month        = {3},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18968359},
  url          = {https://doi.org/10.5281/zenodo.18968359}
}
```

---

## Open Collaboration

We invite:
1. **Experimentalists** to test P5 (Chladni 174 Hz) in the laboratory
2. **Particle physicists** with access to Belle II / LHC archives to search for resonances at 15.5 and 40.2 MeV
3. **Anyone** wishing to challenge the retrodictions or propose new constants to test

---

## References

Key references: CODATA 2022 (NIST) · Muon g−2 Collaboration, Fermilab 2025 · Cohn 1964 (Fibonacci squares) · Williamson & van der Mark 1997 (toroidal electron) · Avrin 2012 (torus knot particles) · Biswas & Ghosh 2019, EPL (quantum mechanics on torus knots) · Bazsó et al. 2010 (Venus–Earth resonance) · Planck Collaboration 2018 · Riess et al. 2022 (SH0ES)

Full reference list in the paper.

---

*© 2026 Sébastien Monast. This work is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
