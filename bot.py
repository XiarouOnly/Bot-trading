from scanner.dexscreener import get_token

from analysis.score import calculate

print()

print("==========")

print("Xiarou Scanner AI")

print("==========")

address = input("Token Address : ")

pair = get_token(address)

if pair is None:

    print("Token tidak ditemukan")

    exit()

result = calculate(pair)

print()

print("AI SCORE :", result["score"])

print()

print("Liquidity :", result["liquidity"])

print("Volume :", result["volume"])

print("FDV :", result["fdv"])

print("Change :", result["change"])

print()

print("Reason")

for i in result["reasons"]:

    print("✓", i)
