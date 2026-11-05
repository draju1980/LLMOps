"""Module 05: ChatML Formatting & Loss Masking"""
import json

class ChatMLFormatter:
    @staticmethod
    def format_instruction(instruction, response):
        return {
            "messages": [
                {"role": "user", "content": instruction},
                {"role": "assistant", "content": response}
            ]
        }

    @staticmethod
    def format_alpaca(instruction, input_text, output_text):
        return {
            "instruction": instruction,
            "input": input_text,
            "output": output_text
        }

    @staticmethod
    def export_jsonl(records, output_path="training_data.jsonl"):
        with open(output_path, 'w') as f:
            for record in records:
                f.write(json.dumps(record) + '\n')
        return output_path
