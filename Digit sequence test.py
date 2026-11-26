import os
import random
import time
import csv
import pyttsx3
from datetime import datetime

# ===== Config =====
OUT_DIR = "02 Result_Memory_2026"
os.makedirs(OUT_DIR, exist_ok=True)

RESULTS_CSV = os.path.join(OUT_DIR, "result_Number_memory_2026.csv")
SLOWDOWN = 70
START_DIGITS = 4
MAX_DIGITS = 10
PAUSE_BETWEEN_ROUNDS_S = 1.0  # small pause so TTS resets

# ===== Helpers =====
def generate_non_repeating_number(length: int) -> str:
    """
    Generate a numeric string of given length where no two adjacent digits are the same.
    Allows leading zeros (e.g., '0427') to match original behavior.
    """
    if length <= 0:
        return ""
    digits = [str(random.randint(0, 9))]
    for _ in range(1, length):
        next_digit = str(random.randint(0, 9))
        while next_digit == digits[-1]:
            next_digit = str(random.randint(0, 9))
        digits.append(next_digit)
    return "".join(digits)

def speak_and_save(spoken_text: str, wav_path: str, slowdown: int = SLOWDOWN):
    # Create a fresh engine each round (helps avoid “second round doesn’t speak” issues)
    engine = pyttsx3.init()
    try:
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - slowdown)
        engine.save_to_file(spoken_text, wav_path)
        engine.say(spoken_text)
        engine.runAndWait()
    finally:
        # Ensure the engine fully releases resources
        try:
            engine.stop()
        except Exception:
            pass

# ===== Main Loop =====
num_digits = START_DIGITS

while num_digits <= MAX_DIGITS:
    current_digits = num_digits

    # ===== Make number & spoken form (no adjacent equal digits) =====
    number = generate_non_repeating_number(current_digits)
    spoken_number = " ".join(number)

    print(f"\n🎲 Round: {current_digits} digits", flush=True)
    # print(f"Generated number: {number}", flush=True)
    # print(f"Speaking now as: {spoken_number}", flush=True)

    # ===== Speak & save =====
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    wav_filename = f"spoken_number_{ts}.wav"
    wav_path = os.path.join(OUT_DIR, wav_filename)
    speak_and_save(spoken_number, wav_path)

    # ===== Get input =====
    # print(f"\n👉 Type the {current_digits} digits you heard (no spaces).", flush=True)
    start = time.perf_counter()
    user_raw = input("> ")
    elapsed = time.perf_counter() - start

    user_digits = "".join(ch for ch in user_raw if ch.isdigit())
    correct = (user_digits == number)

    # ===== Feedback =====
    if correct:
        print("✅ PASS — correct!", flush=True)
    else:
        print("❌ FAIL", flush=True)
        print("Game Over!", flush=True)

    # print(f"⏱ Reaction time: {elapsed:.3f} s", flush=True)
    # print(f"💾 Audio saved to: {wav_path}", flush=True)

    # ===== Log =====
    write_header = not os.path.exists(RESULTS_CSV)
    with open(RESULTS_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow([
                "timestamp","digits_count","target_number","spoken_form",
                "user_input_raw","user_input_digits_only","correct",
                "reaction_time_s","audio_file"
            ])
        writer.writerow([
            ts,current_digits,number,spoken_number,
            user_raw,user_digits,int(correct),
            f"{elapsed:.3f}",wav_filename
        ])

    if not correct:
        break

    if current_digits >= MAX_DIGITS:
        print("🎉 Perfect! You completed all rounds. Well done!", flush=True)
        break

    # Small pause so the next round’s speech reliably plays
    time.sleep(PAUSE_BETWEEN_ROUNDS_S)
    num_digits = current_digits + 1















