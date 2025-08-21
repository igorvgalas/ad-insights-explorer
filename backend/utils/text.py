from rapidfuzz import fuzz

def calculate_similarity(a: str, b: str) -> float:
    """
    Returns similarity score between 0.0 and 1.0 using rapidfuzz ratio.
    """
    return fuzz.ratio(a, b) / 100
