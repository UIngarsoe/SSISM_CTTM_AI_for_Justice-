# ssism_cttm.py
"""SSISM CTTM: Cybersecurity Pyinnyashi Training & Testing Model
Author: U Ingar Soe
License: CC BY 4.0
"""

import math
from typing import Tuple

class CTTM_Pyinnyashi_Cybersecurity_Engine:
    def __init__(self, W_A=2.0, W_U=1.5, W_L=1.0, W_R=1.8, W_DT=1.7):
        self.W_A = float(W_A)
        self.W_U = float(W_U)
        self.W_L = float(W_L)
        self.W_R = float(W_R)
        self.W_DT = float(W_DT)

    def _validate_score(self, value: float, name: str) -> float:
        v = float(value)
        if v < 0.0 or v > 5.0:
            raise ValueError(f"{name} out of range [0.0, 5.0]: {v}")
        return v

    def calculate_phi(self, A, U, L, R, DT) -> float:
        A = self._validate_score(A, "Authority")
        U = self._validate_score(U, "Urgency")
        L = self._validate_score(L, "Linguistics")
        R = self._validate_score(R, "LinkRisk")
        DT = self._validate_score(DT, "DeltaTime")
        Z = (self.W_A*A) + (self.W_U*U) + (self.W_L*L) + (self.W_R*R) + (self.W_DT*DT)
        phi = 1 / (1 + math.exp(-Z))
        return phi

    def get_advisor_verdict(self, phi_score: float) -> Tuple[str, float]:
        if not (0.0 < phi_score < 1.0):
            raise ValueError("phi_score must be in (0,1)")
        CRITICAL_THRESHOLD = 0.20
        if phi_score < CRITICAL_THRESHOLD:
            msg = f"MANDATORY LOCKOUT: Severe Social Engineering Detected. (PHI: {phi_score:.6f})"
        else:
            msg = f"PHI_SAFE: Communication verified. Proceed with awareness. (PHI: {phi_score:.6f})"
        return msg, phi_score

if __name__ == "__main__":
    print("--- SSISM CTTM Cybersecurity Model ---")
    engine = CTTM_Pyinnyashi_Cybersecurity_Engine()

    # Test Case: Authority Scam
    phi_scam = engine.calculate_phi(4.5,4.0,2.0,3.5,5.0)
    verdict_scam, _ = engine.get_advisor_verdict(phi_scam)
    print("\nAuthority Scam Test:", verdict_scam)

    # Test Case: Low Risk Communication
    phi_safe = engine.calculate_phi(1.0,1.0,1.0,0.5,1.0)
    verdict_safe, _ = engine.get_advisor_verdict(phi_safe)
    print("\nLow Risk Communication Test:", verdict_safe)
