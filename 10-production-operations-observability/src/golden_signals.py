"""Module 10: Golden Signals Metrics"""
class GoldenSignals:
    def __init__(self):
        self.metrics = {"ttft": [], "tpot": [], "tokens_per_sec": []}

    def record_inference(self, ttft_ms, tpot_ms, tokens):
        self.metrics["ttft"].append(ttft_ms)
        self.metrics["tpot"].append(tpot_ms)
        self.metrics["tokens_per_sec"].append(tokens / (ttft_ms + tpot_ms) * 1000)
