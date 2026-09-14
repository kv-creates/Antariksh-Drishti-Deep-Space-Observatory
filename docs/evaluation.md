# 📏 Evaluation

`evaluation/metrics.py` computes recall, efficiency, SNR error. `evaluation/report.py` writes Markdown summary.

```bash
python -m evaluation.report
```

Thresholds: recall ≥95%, efficiency ≥70%, SNR ±5%. CI fails otherwise (see `.github/workflows/ci.yml`).
