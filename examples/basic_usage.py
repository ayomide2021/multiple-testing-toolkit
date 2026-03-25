from fdr_toolkit.fdr import benjamini_hochberg
from fdr_toolkit.bonferroni import bonferroni

p_vals = [0.12, 0.03, 0.001, 0.20, 0.04,
          0.002, 0.15, 0.05, 0.30, 0.01]

bh_results = benjamini_hochberg(p_vals)
bonf_results = bonferroni(p_vals)

print("BH Results:")
print(bh_results)

print("\nBonferroni Results:")
print(bonf_results)
