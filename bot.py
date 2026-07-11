from scanner.dexscreener import get_token
from analysis.score import calculate
from analysis.recommendation import get_recommendation
from analysis.rugpull import check
from analysis.momentum import analyze as momentum
print("=" * 50)
print("🚀 Xiarou Scanner AI")
print("=" * 50)

address = input("Masukkan Token Address: ")

pair = get_token(address)

if pair is None:
    print("❌ Token tidak ditemukan.")
    exit()

result = calculate(pair)

recommendation = get_recommendation(result["score"])

print("\n==============================")

print(f"AI SCORE       : {result['score']}/100")
print(f"SIGNAL         : {recommendation['signal']}")
print(f"RISK           : {recommendation['risk']}")
print(f"CONFIDENCE     : {recommendation['confidence']}%")

print("\n===== DATA =====")

print(f"Liquidity      : ${result['liquidity']:,}")
print(f"Volume 24H     : ${result['volume']:,}")
print(f"FDV            : ${result['fdv']:,}")
print(f"Price Change   : {result['change']}%")

print("\n===== REASONS =====")

for reason in result["reasons"]:
    print(f"✅ {reason}")
    rug = check(pair)
    print()

print("===== RUGPULL =====")

print("Risk :", rug["risk_level"])

print("Score :", rug["risk_score"])

for i in rug["reasons"]:

    print("❌", i)
    
recommendation = get_recommendation(result["score"])
momentum_result = momentum(pair)
print("\n===== MOMENTUM =====")
print("Momentum Score :", momentum_result["score"])

for r in momentum_result["reasons"]:
    print("📈", r)
    ===== MOMENTUM =====

Momentum Score : 82

📈 Volume sangat tinggi
📈 Momentum 5m positif
📈 Trend 24h bullish
📈 Buyer mendominasi
