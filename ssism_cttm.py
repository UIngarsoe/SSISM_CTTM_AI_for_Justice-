import math

# SSISM V Smart Advisor Core Logic: Cybersecurity Pyinnyashi Training & Testing Model (CTTM)

# -----------------------------------------------------------------------------------
# A: Authority Score (0-5, 5=Highest Authority Claim)
# U: Urgency Score (0-5, 5=Extreme Time Pressure)
# L: Linguistics Score (0-5, 5=Poor/Suspicious Language)
# R: Link/File Risk Score (0-5, 5=Untrustworthy/Unknown Link)
# dT: Time Anomaly Score (0-5, 5=Highly Unusual Contact Time)
# -----------------------------------------------------------------------------------

def calculate_digital_trust_score(A, U, L, R, dT):
    """
    Calculates the Digital Trust Score (Phi) using a weighted Logistic Regression model.
    A score < 0.2 triggers the MANDATORY LOCKOUT.
    
    Inputs (scores 0-5): Authority (A), Urgency (U), Linguistics (L), Link/File (R), Time Anomaly (dT)
    
    Returns: Tuple (Phi_score, Action_Message)
    """
    
    # ----------------------------------
    # Pre-Calibrated Weights (W) based on real-world scam experiences
    # Urgency and Authority are typically the heaviest indicators
    W_A = 2.0  # Weight for Authority
    W_U = 1.5  # Weight for Urgency
    W_L = 1.0  # Weight for Linguistics
    W_R = 1.2  # Weight for Link/File Risk
    W_dT = 1.3 # Weight for Time Anomaly
    # ----------------------------------
    
    # 1. Calculate the Total Risk Score (Z) - Linear aggregation of weighted factors
    Z = (W_A * A) + (W_U * U) + (W_L * L) + (W_R * R) + (W_dT * dT)
    
    # We use the negative of Z for the Sigmoid function to map high risk (high Z) to low trust (low Phi)
    
    # 2. Calculate the Digital Trust Score (Phi) using the Sigmoid (Logistic) Function
    # Phi = 1 / (1 + e^Z)  <-- maps High Z (Risk) to Low Phi (Trust)
    try:
        Phi = 1 / (1 + math.exp(Z))
    except OverflowError:
        # Handle extreme Z values gracefully
        Phi = 0.0001
        
    # Define the MANDATORY LOCKOUT Threshold (Phi < 0.2)
    LOCKOUT_THRESHOLD = 0.2 
    
    # 3. Enforce the SSISM MANDATORY LOCKOUT Rule
    if Phi < LOCKOUT_THRESHOLD:
        action_message = "MANDATORY LOCKOUT: Digital Trust Score is below 0.2. A 24-HOUR VERIFICATION PROTOCOL IS REQUIRED."
    else:
        action_message = "Digital Trust Score is Acceptable (Proceed with Caution)."
        
    return round(Phi, 4), action_message

# --- Example Usage ---
# Scenario 1: High Urgency (U=5), High Authority (A=5) -> Should trigger LOCKOUT
score_high_risk, message_high_risk = calculate_digital_trust_score(A=5, U=5, L=1, R=1, dT=0)
print(f"Scenario 1 - Digital Trust Score (Phi): {score_high_risk}")
print(f"Action: {message_high_risk}\n")

# Scenario 2: Low Risk (All low scores) -> Should be Acceptable
score_low_risk, message_low_risk = calculate_digital_trust_score(A=0, U=0, L=0, R=0, dT=0)
print(f"Scenario 2 - Digital Trust Score (Phi): {score_low_risk}")
print(f"Action: {message_low_risk}\n")
