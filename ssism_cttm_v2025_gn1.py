#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SSISM V Smart Advisor — Cybersecurity Pyinnyashi Training & Testing Model (CTTM)
Version: 2025-GN1
Author: U Ingar Soe
License: CC BY 4.0

Description:
--------------
This model forms part of the SSISM CTTM framework — an educational and defensive
AI system designed to enhance *digital mindfulness* for civil society, activists,
and journalists. It computes a "Digital Trust Score (Φ)" based on five weighted
social-engineering risk factors and enforces the "Mandatory Lockout Rule" for
high-risk communications.

Philosophy:
“To protect truth without hatred.
 To detect deceit without anger.
 To train awareness without ego.”
"""

import math

# -----------------------------------------------------------------------------------
# Input Factor Definitions (0–5 scale)
# -----------------------------------------------------------------------------------
# A: Authority Score (5 = highest authority claim)
# U: Urgency Score (5 = extreme time pressure)
# L: Linguistics Score (5 = suspicious or manipulative language)
# R: Link/File Risk Score (5 = untrustworthy or unknown source)
# dT: Time Anomaly Score (5 = highly unusual contact timing)
# -----------------------------------------------------------------------------------

def calculate_digital_trust_score(A, U, L, R, dT):
    """
    Calculates the Digital Trust Score (Φ) using a weighted Logistic Regression model.
    A Φ < 0.2 triggers a CRITICAL LOW TRUST ALERT and initiates Tiered Response logic.

    Parameters
    ----------
    A : float  (Authority Score, 0–5)
    U : float  (Urgency Score, 0–5)
    L : float  (Linguistics Score, 0–5)
    R : float  (Link/File Risk Score, 0–5)
    dT : float (Time Anomaly Score, 0–5)

    Returns
    -------
    (Phi_score, Action_Message) : tuple
        Phi_score : float (Digital Trust Score, 0–1)
        Action_Message : str (Defensive advisory)
    """

    # Pre-calibrated Weights based on real-world threat data
    W_A, W_U, W_L, W_R, W_dT = 2.0, 1.5, 1.0, 1.2, 1.3

    # Step 1. Compute the Total Risk Score (Z)
    Z = (W_A * A) + (W_U * U) + (W_L * L) + (W_R * R) + (W_dT * dT)

    # Step 2. Apply Sigmoid function to convert Z → Φ
    # Φ = 1 / (1 + e^Z) → high risk (large Z) → low trust (small Φ)
    try:
        Phi = 1 / (1 + math.exp(Z))
    except OverflowError:
        # Extreme risk case handling
        Phi = 0.0001

    # Step 3. Apply the MANDATORY LOCKOUT principle
    LOCKOUT_THRESHOLD = 0.2
    if Phi < LOCKOUT_THRESHOLD:
        action_message = (
            f"⚠️ CRITICAL LOW TRUST ALERT (Φ < {LOCKOUT_THRESHOLD}).\n"
            "Activate Tier 2 or Tier 3 Defensive Protocol:\n"
            "→ LOCKOUT (24-hour freeze) or\n"
            "→ EVASION & verification before communication resumes."
        )
    else:
        action_message = "✅ Trust level acceptable (Tier 1: Proceed with caution)."

    return round(Phi, 4), action_message


# -----------------------------------------------------------------------------------
# Example Scenarios
# -----------------------------------------------------------------------------------
if __name__ == "__main__":
    # Scenario 1: High-risk (urgent + authority pressure)
    phi_high, msg_high = calculate_digital_trust_score(A=5, U=5, L=1, R=1, dT=0)
    print("Scenario 1 — HIGH RISK")
    print(f"Digital Trust Score (Φ): {phi_high}")
    print(f"Action: {msg_high}\n")

    # Scenario 2: Low-risk (benign context)
    phi_low, msg_low = calculate_digital_trust_score(A=0, U=0, L=0, R=0, dT=0)
    print("Scenario 2 — LOW RISK")
    print(f"Digital Trust Score (Φ): {phi_low}")
    print(f"Action: {msg_low}\n")
