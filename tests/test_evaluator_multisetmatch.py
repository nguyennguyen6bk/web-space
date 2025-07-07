import json
import sys
import os

from evaluate.evaluator import Evaluator


with open('./data/tasks_temp.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)

def test_multiset_match():
    eva = Evaluator(tasks)

    task_id = "t04";
    agent_result =  [                
        "Beaumont Summit Kit",
        "Stellar Solar Jacket"
    ]
    result = eva.evaluate_with_selenium(task_id, agent_result)

    assert result is True  # Hoặc assert result == expected


if __name__ == "__main__":
    test_multiset_match()

