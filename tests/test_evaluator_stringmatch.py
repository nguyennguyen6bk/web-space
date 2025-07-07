import asyncio
import json
import sys
import os

from evaluate.evaluator import Evaluator


with open('./data/tasks_temp.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)


def test_string_match_exact():
    eva = Evaluator(tasks)

    task_id = "1";
    agent_result = "Aim Analog Watch"

    result = eva.evaluate(task_id, agent_result)

    assert result is True  # Hoặc assert result == expected

async def test_string_match_exact_playwright():
    eva = Evaluator(tasks)

    task_id = "1";
    agent_result = "Aim Analog Watch"

    result = await eva.evaluate_with_playwright(task_id, agent_result)

    assert result is True  # Hoặc assert result == expected

def test_string_match_contains():
    eva = Evaluator(tasks)

    task_id = "2";
    agent_result = "Stellar Solar Jacket and Beaumont Summit Kit"

    result = eva.evaluate_with_selenium(task_id, agent_result)

    assert result is True  # Hoặc assert result == expected

def test_string_match_semantic():
    eva = Evaluator(tasks)

    task_id = "101";
    agent_result = "Veronica Costello, 6146 Honey Bluff Parkway, Calder, Michigan, 49628-7978, United States, T: (555) 229-3326"

    result = eva.evaluate(task_id, agent_result)

    assert result is True  # Hoặc assert result == expected




if __name__ == "__main__":
    # asyncio.run(test_string_match_exact())
    test_string_match_exact()
    asyncio.run(test_string_match_exact_playwright())
    test_string_match_contains()
    # await test_string_match_semantic()

