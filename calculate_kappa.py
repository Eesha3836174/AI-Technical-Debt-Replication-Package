"""
Script to calculate Inter-Rater Reliability (Observed Agreement & Cohen's Kappa)
for Systematic Literature Review screening data.

Authors: Eesha Naveed & Hafsa Shamriz
Study: Infrastructure-Induced Technical Debt in Machine Learning Systems
"""

def compute_cohens_kappa(a, b, c, d):
    """
    Computes Observed Agreement (Po) and Cohen's Kappa (kappa) from a 2x2 matrix.
    
    a: Both Include (Dual Inclusions)
    b: Reviewer A Include, Reviewer B Exclude
    c: Reviewer A Exclude, Reviewer B Include
    d: Both Exclude (Dual Exclusions)
    """
    N = a + b + c + d
    
    # 1. Observed Agreement (Po)
    Po = (a + d) / N
    
    # 2. Expected Chance Agreement (Pe)
    p_reviewer_A_inc = (a + b) / N
    p_reviewer_A_exc = (c + d) / N
    p_reviewer_B_inc = (a + c) / N
    p_reviewer_B_exc = (b + d) / N
    
    Pe = (p_reviewer_A_inc * p_reviewer_B_inc) + (p_reviewer_A_exc * p_reviewer_B_exc)
    
    # 3. Cohen's Kappa
    kappa = (Po - Pe) / (1 - Pe)
    
    # Landis & Koch (1977) Interpretation Band
    if kappa < 0:
        band = "Poor Agreement"
    elif kappa <= 0.20:
        band = "Slight Agreement"
    elif kappa <= 0.40:
        band = "Fair Agreement"
    elif kappa <= 0.60:
        band = "Moderate Agreement"
    elif kappa <= 0.80:
        band = "Substantial Agreement"
    else:
        band = "Almost Perfect Agreement"
        
    return N, Po, Pe, kappa, band


def main():
    # Screening numbers from dataset (106 unique papers)
    a = 21  # Dual Inclusions
    b = 3   # Disagreement (Eesha Include, Hafsa Exclude)
    c = 2   # Disagreement (Eesha Exclude, Hafsa Include)
    d = 80  # Dual Exclusions
    
    N, Po, Pe, kappa, band = compute_cohens_kappa(a, b, c, d)
    
    print("=" * 55)
    print(" INTER-RATER RELIABILITY ANALYSIS (COHEN'S KAPPA)")
    print("=" * 55)
    print(f" Total Sample Size (N)       : {N}")
    print(f" Both Included (a)           : {a}")
    print(f" Disagreements (b)           : {b}")
    print(f" Disagreements (c)           : {c}")
    print(f" Both Excluded (d)           : {d}")
    print("-" * 55)
    print(f" Observed Agreement (Po)    : {Po:.4f} ({Po * 100:.2f}%)")
    print(f" Chance Agreement (Pe)      : {Pe:.4f} ({Pe * 100:.2f}%)")
    print(f" Cohen's Kappa (κ)          : {kappa:.4f}")
    print(f" Landis & Koch Band         : {band}")
    print("=" * 55)


if __name__ == "__main__":
    main()
