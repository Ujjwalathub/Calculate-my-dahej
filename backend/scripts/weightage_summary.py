"""
Dowry Weightage Summary
Clear documentation of what increases and decreases dowry amounts
"""

def print_weightage_summary():
    """
    Print a clear summary of dowry weightage rules.
    """
    
    print("=" * 100)
    print(" " * 35 + "DOWRY WEIGHTAGE RULES")
    print("=" * 100)
    print()
    
    # Summary table
    summary = {
        "BOY": {
            "Increases Dowry": [
                "✓ High Income (₹50 per unit)",
                "✓ High Father Income (₹40 per unit)",
                "✓ Government Job (+₹15,00,000)",
                "✓ Very Stable Job (+₹8,00,000)",
                "✓ Stable Job (+₹4,00,000)",
                "✓ Fair Skin (+₹6,00,000)",
                "✓ General Caste (+₹7,00,000)",
                "✓ Height at 5.9 ft (sweet spot)",
            ],
            "Decreases Dowry": [
                "✗ First Marriage (-₹3,00,000)",
                "✗ Physical Disability (-₹12,00,000)",
                "✗ Dark Skin (-₹3,00,000)",
                "✗ SC Caste (-₹4,00,000)",
                "✗ Unstable Job (-₹4,00,000)",
                "✗ Height far from 5.9 ft (-₹25,00,000 per ft deviation)",
            ]
        },
        "GIRL": {
            "Increases Dowry": [
                "✓ First Marriage (+₹5,00,000)",
                "✓ Physical Disability (+₹6,00,000)",
                "✓ Father Income - Mild (+₹10 per unit)",
                "✓ Dark Skin (+₹2,00,000)",
                "✓ SC Caste (+₹3,00,000)",
                "✓ Height at 5.7 ft (sweet spot)",
            ],
            "Decreases Dowry": [
                "✗ High Income (-₹25 per unit)",
                "✗ Government Job (-₹8,00,000)",
                "✗ Fair Skin (-₹4,00,000)",
                "✗ General Caste (-₹5,00,000)",
                "✗ Height far from 5.7 ft (-₹18,00,000 per ft deviation)",
            ]
        },
        "OTHER FACTORS": {
            "Decreases Dowry": [
                "✗ Inter-religion Marriage (-₹10,00,000)",
                "✗ Inter-caste Marriage (-₹5,00,000)",
            ],
            "Neutral": [
                "○ Same Caste & Religion (Base value)",
            ]
        }
    }
    
    # Print formatted summary
    for category, impacts in summary.items():
        print(f"\n{'─' * 100}")
        print(f"  {category}")
        print(f"{'─' * 100}")
        
        for impact_type, items in impacts.items():
            print(f"\n  {impact_type}:")
            for item in items:
                print(f"    {item}")
    
    print("\n" + "=" * 100)
    print()
    
    # Height formula explanation
    print("HEIGHT IMPACT FORMULAS:")
    print("-" * 100)
    print("  Boy Height Effect:  -abs(boy_height - 5.9) × ₹25,00,000")
    print("                      → Perfect at 5.9 ft, penalty grows linearly with deviation")
    print()
    print("  Girl Height Effect: -abs(girl_height - 5.7) × ₹18,00,000")
    print("                      → Perfect at 5.7 ft, penalty grows linearly with deviation")
    print()
    print("  Examples:")
    print("    Boy at 6.0 ft: -abs(6.0 - 5.9) × 25,00,000 = -₹2,50,000")
    print("    Boy at 5.7 ft: -abs(5.7 - 5.9) × 25,00,000 = -₹5,00,000")
    print("    Girl at 5.8 ft: -abs(5.8 - 5.7) × 18,00,000 = -₹1,80,000")
    print("    Girl at 5.5 ft: -abs(5.5 - 5.7) × 18,00,000 = -₹3,60,000")
    print("=" * 100)
    print()
    
    # Base dowry
    print("BASE DOWRY: ₹30,00,000 (before any adjustments)")
    print("FINAL DOWRY: Base + All Positive Impacts - All Negative Impacts (minimum ₹0)")
    print("VARIATION: ±5% random variation applied to final amount")
    print("=" * 100)


def print_quick_reference():
    """
    Print a quick reference table.
    """
    print("\n" + "=" * 100)
    print(" " * 40 + "QUICK REFERENCE")
    print("=" * 100)
    
    table_data = [
        ("Feature", "Boy Side", "Girl Side"),
        ("-" * 30, "-" * 30, "-" * 30),
        ("Income", "↑ Increases", "↓ Decreases"),
        ("Father Income", "↑ Increases", "↑ Mild Increase"),
        ("Government Job", "↑ Strong Increase", "↓ Decreases"),
        ("First Marriage", "↓ Decreases", "↑ Increases"),
        ("Physical Disability", "↓ Strong Decrease", "↑ Increases"),
        ("Fair Skin", "↑ Increases", "↓ Decreases"),
        ("General Caste", "↑ Increases", "↓ Decreases"),
        ("Job Stability", "↑ Increases (boy only)", "—"),
        ("Height Sweet Spot", "5.9 ft", "5.7 ft"),
        ("Inter-religion", "↓ Decreases (both)", "↓ Decreases (both)"),
    ]
    
    for row in table_data:
        print(f"  {row[0]:30s} | {row[1]:30s} | {row[2]:30s}")
    
    print("=" * 100)
    print()
    print("Legend:")
    print("  ↑ = Increases dowry amount")
    print("  ↓ = Decreases dowry amount")
    print("  — = Not applicable")
    print("=" * 100)


if __name__ == "__main__":
    print_weightage_summary()
    print_quick_reference()
