"""Write evaluation summary (stdout + Markdown)."""
from .metrics import recall, sched_efficiency, snr_error

def main():
    r, e, s = recall(), sched_efficiency(), snr_error()
    md = f"# Evaluation\n\n- recall: {r:.2f} (≥0.95)\n- efficiency: {e:.2f} (≥0.70)\n- snr_err: {s:.4f} (≤0.05)\n"
    print(md)
    open("evaluation/REPORT.md", "w", encoding="utf-8").write(md)

if __name__ == "__main__":
    main()
