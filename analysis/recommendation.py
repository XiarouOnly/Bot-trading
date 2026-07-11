"""
Recommendation Engine
Mengubah AI Score menjadi rekomendasi.
"""

def get_recommendation(score: int):

    if score >= 95:
        return {
            "signal": "🔥 STRONG BUY",
            "risk": "LOW",
            "confidence": 95
        }

    elif score >= 85:
        return {
            "signal": "🟢 BUY",
            "risk": "LOW",
            "confidence": 90
        }

    elif score >= 75:
        return {
            "signal": "🟡 WATCH",
            "risk": "MEDIUM",
            "confidence": 75
        }

    elif score >= 60:
        return {
            "signal": "🟠 WAIT",
            "risk": "MEDIUM",
            "confidence": 60
        }

    return {
        "signal": "🔴 SKIP",
        "risk": "HIGH",
        "confidence": 40
    }
