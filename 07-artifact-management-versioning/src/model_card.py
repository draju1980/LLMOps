"""Module 07: Model Card Schema"""
from dataclasses import dataclass, asdict
import json

@dataclass
class ModelCard:
    name: str
    version: str
    base_model: str
    training_dataset: str
    eval_metrics: dict

    def to_dict(self):
        return asdict(self)

    def save_card(self, output_path="model_card.json"):
        with open(output_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
        return output_path
