"""Module 06: Kubeflow Pipelines v2"""
from dataclasses import dataclass

@dataclass
class KFPComponent:
    name: str
    inputs: list
    outputs: list

    def to_dict(self):
        return {
            "name": self.name,
            "inputs": self.inputs,
            "outputs": self.outputs
        }

class KFPPipeline:
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def get_dag(self):
        return {"pipeline": self.name, "components": [c.to_dict() for c in self.components]}
