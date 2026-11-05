"""Module 16: Labs Solutions"""
# Lab 1: VRAM Calculator
def calculate_vram(model_params_b, adapter_rank=8):
    model_vram = model_params_b * 2  # 16-bit
    adapter_vram = model_params_b * adapter_rank / 100
    return model_vram + adapter_vram

# Lab 2: Canary Deployment
def canary_route(traffic_pct=10):
    return {"stable": 100-traffic_pct, "canary": traffic_pct}

# Lab 3: Prompt Skew Detection
def detect_skew(train_prompt, serve_prompt):
    return hash(train_prompt) == hash(serve_prompt)
