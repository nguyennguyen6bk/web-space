import json
import sys
import os

from evaluate.evaluator import Evaluator


with open('./data/tasks_temp.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)

def test_regex_match():
    eva = Evaluator(tasks)

    task_id = "t06";
    agent_result =  {
        "email": "user@example.com",
        "password": "Password123"
    }
    result = eva.evaluate_with_selenium(task_id, agent_result)

    assert result is True  # Hoặc assert result == expected

def test_regex_match_email_invalid():
    eva = Evaluator(tasks)

    task_id = "t06";
    agent_result =  {
        "email": "invalid-email",
        "password": "Password123"
    }
    result = eva.evaluate_with_selenium(task_id, agent_result)

    assert result is False  # Hoặc assert result == expected

def test_regex_match_password_invalid():
    eva = Evaluator(tasks)

    task_id = "t06";
    agent_result =  {
        "email": "invalid-email",
        "password": "Password123"
    }
    result = eva.evaluate_with_selenium(task_id, agent_result)

    assert result is False  # Hoặc assert result == expected

def test_regex_match_password_invalid():
    eva = Evaluator(tasks)

    task_id = "t06";
    agent_result =  {
        "email": "user@example.com",
        "password": "short"
    }
    result = eva.evaluate_with_selenium(task_id, agent_result)

    assert result is False  # Hoặc assert result == expected

if __name__ == "__main__":
    test_regex_match()
    test_regex_match_email_invalid()
    test_regex_match_password_invalid()
