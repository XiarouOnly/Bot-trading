from scanner.dexscreener import get_token

from analysis.score import calculate
from analysis.recommendation import get_recommendation
from analysis.rugpull import check
from analysis.momentum import analyze as momentum
from analysis.final_score import build


def analyze_token():

    print("\n==============================")
    print(" Xiarou Scanner AI")
    print("==============================\n")

    address = input("Masukkan Token Address : ").strip()

    if address == "":
        print("Token address kosong.")
        return

    pair = get_token(address)

    if pair is None:
        print("Token tidak ditemukan.")
        return

    score = calculate(pair)

    recommendation = get_recommendation(score["score"])

    rug = check(pair)

    momentum_result = momentum(pair)

    final = build(
        score,
        momentum_result,
        rug
    )

    print("\n==============================")

    print("AI SCORE :", final["ai_score"])

    print("SIGNAL :", final["signal"])

    print("CONFIDENCE :", final["confidence"], "%")

    print("RISK :", rug["risk_level"])

    print("\n========== DATA ==========")

    print("Liquidity :", score["liquidity"])

    print("Volume 24H :", score["volume"])

    print("FDV :", score["fdv"])

    print("Change :", score["change"])

    print("\n========== AI REASON ==========")

    for reason in score["reasons"]:
        print("✓", reason)

    print("\n========== RUGPULL ==========")

    print("Risk Score :", rug["risk_score"])

    for reason in rug["reasons"]:
        print("❌", reason)

    print("\n========== MOMENTUM ==========")

    print("Momentum Score :", momentum_result["score"])

    for reason in momentum_result["reasons"]:
        print("📈", reason)

    print("\n==============================\n")


def main():

    while True:

        print("""
==============================

🚀 Xiarou Scanner AI

1. Analyze Token

0. Exit

==============================
""")

        menu = input("Pilih : ").strip()

        if menu == "1":

            analyze_token()

        elif menu == "0":

            print("Bye.")

            break

        else:

            print("Menu tidak tersedia.")


if __name__ == "__main__":

    main()
