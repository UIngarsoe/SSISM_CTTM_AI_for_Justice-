import math

# SSISM V Smart Advisor Core Logic: Cybersecurity Pyinnyashi Training & Testing Model (CTTM)

# -----------------------------------------------------------------------------------
# Factor Definitions (Input Scores 0-5):
# A: Authority Score (5=Highest Authority Claim)
# U: Urgency Score (5=Extreme Time Pressure)
# L: Linguistics Score (5=Poor/Suspicious Language)
# R: Link/File Risk Score (5=Untrustworthy/Unknown Link)
# dT: Time Anomaly Score (5=Highly Unusual Contact Time)
# -----------------------------------------------------------------------------------

def calculate_digital_trust_score(A, U, L, R, dT):
    """
    Calculates the Digital Trust Score (Phi) using a weighted Logistic Regression model.
    A score < 0.2 triggers a CRITICAL LOW TRUST ALERT, requiring a Tiered Response.
    
    Inputs (scores 0-5): Authority (A), Urgency (U), Linguistics (L), Link/File (R), Time Anomaly (dT)
    
    Returns: Tuple (Phi_score, Action_Message)
    """
    
    # ----------------------------------
    # Pre-Calibrated Weights (W) based on real-world scam and influence experiences
    W_A = 2.0  # Weight for Authority
    W_U = 1.5  # Weight for Urgency
    W_L = 1.0  # Weight for Linguistics
    W_R = 1.2  # Weight for Link/File Risk
    W_dT = 1.3 # Weight for Time Anomaly
    # ----------------------------------
    
    # 1. Calculate the Total Risk Score (Z) - Linear aggregation of weighted factors
    Z = (W_A * A) + (W_U * U) + (W_L * L) + (W_R * R) + (W_dT * dT)
    
    # 2. Calculate the Digital Trust Score (Phi) using the Sigmoid (Logistic) Function
    # Phi = 1 / (1 + e^Z)  <-- maps High Z (Risk) to Low Phi (Trust)
    try:
        Phi = 1 / (1 + math.exp(Z))
    except OverflowError:
        # Handle cases where Z is too large (extreme risk)
        Phi = 0.0001
        
    # Define the CRITICAL LOW TRUST Threshold (Phi < 0.2)
    LOCKOUT_THRESHOLD = 0.2 
    
    # 3. Apply Tiered Response Logic
    if Phi < LOCKOUT_THRESHOLD:
        action_message = f"CRITICAL LOW TRUST ALERT (Phi < {LOCKOUT_THRESHOLD}). CONSULT GUIDELINES for Tier 2/Tier 3 MANDATORY ACTION PROTOCOL (LOCKOUT or EVASION)."
    else:
        action_message = "Digital Trust Score is Acceptable (Tier 1: Proceed with Caution)."
        
    return round(Phi, 4), action_message

# --- Example Usage ---
# Scenario 1: High Risk (A=5, U=5) -> Triggers CRITICAL ALERT
score_high_risk, message_high_risk = calculate_digital_trust_score(A=5, U=5, L=1, R=1, dT=0)
print(f"Scenario 1 - Digital Trust Score (Phi): {score_high_risk}")
print(f"Action: {message_high_risk}\n")

# Scenario 2: Low Risk (All low scores) -> Acceptable
score_low_risk, message_low_risk = calculate_digital_trust_score(A=0, U=0, L=0, R=0, dT=0)
print(f"Scenario 2 - Digital Trust Score (Phi): {score_low_risk}")
print(f"Action: {message_low_risk}\n")
