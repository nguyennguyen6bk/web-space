import sys
import os

from evaluate.matchers import *

def test_semantic_matcher():
    task_description = "Translate the following English sentence to Vietnamese. 'Hello, how are you?' "
    agent_value = "Xin chào, bạn khỏe không?"
    match_value = "chào cậu, cậu khỏe chứ?"
    result = semantic(task_description, agent_value, match_value)
    assert result is True  # Hoặc assert result == expected

def test_exact_matcher():
    agent_value = "Xin chào, bạn khỏe không?"
    match_value = "chào cậu, cậu khỏe chứ?"
    result = exact(agent_value, match_value)
    assert result is False  # Hoặc assert result == expected

def test_exact_matcher_2():
    agent_value = "chào cậu, cậu khỏe chứ?"
    match_value = "chào cậu, cậu khỏe chứ?"
    result = exact(agent_value, match_value)
    assert result is True  # Hoặc assert result == expected

def test_contains_matcher():
    agent_value = "Xin chào, bạn khỏe không?"
    match_value = "bạn khỏe không?"
    result = contains(agent_value, match_value)
    assert result is True  # Hoặc assert result == expected

def test_contains_matcher_2():
    agent_value = "Xin chào, bạn khỏe không?"
    match_value = "chào bạn"
    result = contains(agent_value, match_value)
    assert result is False  # Hoặc assert result == expected