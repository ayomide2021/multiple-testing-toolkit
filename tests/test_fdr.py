from fdr_toolkit.fdr import benjamini_hochberg

def test_bh_basic():
    p_vals = [0.001, 0.01, 0.2]
    results = benjamini_hochberg(p_vals, alpha=0.05)

    assert sum(results["rejected"]) >= 1
