#!/usr/bin/env python3
"""Test script for Pattern 2: Build + Test + Fix Loop.
This script has a deliberate bug — missing import."""
import json
import math
from pathlib import Path

# Bug: missing 'import math'
def compute_stats(numbers):
    """Calculate mean and standard deviation of a list of numbers."""
    n = len(numbers)
    if n == 0:
        return {"mean": 0, "stddev": 0}
    
    mean = sum(numbers) / n
    
    # BUG: math is not imported — this will throw NameError
    variance = sum((x - mean) ** 2 for x in numbers) / n
    stddev = math.sqrt(variance)  # <-- NameError: math not defined
    
    return {"mean": round(mean, 2), "stddev": round(stddev, 2)}


def main():
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    stats = compute_stats(data)
    output = {**stats, "source": "Pattern 2 test"}
    
    out_path = Path(__file__).parent / "pattern2-result.json"
    out_path.write_text(json.dumps(output, indent=2))
    print(f"✓ Stats computed: {stats['mean']} ± {stats['stddev']}")
    print(f"✓ Written to {out_path}")


if __name__ == "__main__":
    main()
