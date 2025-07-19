import ast
import json
from selenium.webdriver.remote.webdriver import WebDriver
from playwright.async_api import Page
from evaluate.handlers import *


class Evaluator:
    def __init__(self, tasks):
        self.tasks = tasks
    

    def evaluate_with_selenium(self, task_id, agent_result=None, browser: WebDriver=None):
        task = next((task for task in self.tasks if task['task_id'] == task_id), None)
        if not task:
            print(f"Task ID {task_id} not found.")
            return False
        # Simulate evaluation logic
        print(f"---------Evaluating task: {task['task_id']}------")
        eval_block = task['eval']
        result = False
        for eval_type in eval_block['eval_type']:
            if eval_type == 'dom_match':
                if isinstance(browser, WebDriver):
                    print(f"Evaluating {eval_type} with Selenium...")
                    if not dom_match_selenium(target_conf=eval_block[eval_type], browser=browser):
                        return False
                else:
                    print("Browser is not a valid Selenium WebDriver instance.")
                    return False
            elif eval_type == 'url_match':
                if isinstance(browser, WebDriver):
                    print(f"Evaluating {eval_type} with Selenium...")
                    if not url_match_selenium(target_conf=eval_block[eval_type], browser=browser):
                        return False
                else:
                    print("Browser is not a valid Selenium WebDriver instance.")
                    return False
            elif eval_type == 'string_match':     
                print(f"Evaluating {eval_type}...")
                if not string_match(target_conf=eval_block[eval_type], agent_result=agent_result, task=task['task_description']):
                    return False
                result = True
            elif eval_type == 'regex_match':
                print(f"Evaluating {eval_type}...")
                if not regex_match(target_conf=eval_block[eval_type], agent_result=agent_result):
                    return False
                result = True
            elif eval_type == 'multiset_match':
                print(f"Evaluating {eval_type}...")
                if not multiset_match(target_conf=eval_block[eval_type], agent_result=agent_result):
                    return False
                result = True
            elif eval_type == 'list_match':
                print(f"Evaluating {eval_type}...")
                if not list_match(target_conf=eval_block[eval_type], agent_result=agent_result):
                    return False
                result = True
            else:
                print(f"Unknown eval type: {eval_type}")
                return False  # Nếu eval_type không hợp lệ, trả về False
                
        return result
    

    async def evaluate_with_playwright(self, task_id, agent_result=None, browser: Page=None):
        task = next((task for task in self.tasks if task['task_id'] == task_id), None)
        if not task:
            print(f"Task ID {task_id} not found.")
            return False
        # Simulate evaluation logic
        print(f"---------Evaluating task: {task['task_id']}------")
        eval_block = task['eval']
        result = False
        for eval_type in eval_block['eval_type']:
            if eval_type == 'dom_match':
                print(f"Evaluating {eval_type} with Playwright...")
                if not await dom_match_playwright(target_conf=eval_block[eval_type], browser=browser):
                    return False
                result = True
                # Handle DOM matching with Playwright
            elif eval_type == 'url_match':
                print(f"Evaluating {eval_type} with Playwright...")
                if not await url_match_playwright(target_conf=eval_block[eval_type], browser=browser):
                    return False
                result = True
                # Handle URL matching with Playwright       
            elif eval_type == 'string_match':
                print(f"Evaluating {eval_type}...")
                if not string_match(target_conf=eval_block[eval_type], agent_result=agent_result, task=task['task_description']):
                    return False
                result = True   
            elif eval_type == 'regex_match':
                print(f"Evaluating {eval_type}...")
                if not regex_match(target_conf=eval_block[eval_type], agent_result=agent_result):
                    return False
                result = True

            elif eval_type == 'multiset_match':
                print(f"Evaluating {eval_type}...")
                if not multiset_match(target_conf=eval_block[eval_type], agent_result=agent_result):
                    return False
                result = True
            elif eval_type == 'list_match':
                print(f"Evaluating {eval_type}...")
                if not list_match(target_conf=eval_block[eval_type], agent_result=agent_result):
                    return False
                result = True
            else:
                print(f"Unknown eval type: {eval_type}")
                return False  # Nếu eval_type không hợp lệ, trả về False
                
        return result

    def eval_type_check(self):
        for task in self.tasks:
            eval_block = task['eval']
            for eval_type in eval_block['eval_type']:
                print(f"Checking eval type: {eval_type} in task {task['task_id']}")
                if eval_type not in ['string_match', 'regex_match', 'url_match', 'dom_match']:
                    print(f"Invalid eval type: {eval_type} in task {task['task_id']}")
                    return False
        print("All eval types are valid.")



        # def evaluate(self, task_id, agent_result=None, browser=None):
    #     task = next((task for task in self.tasks if task['task_id'] == task_id), None)
    #     if not task:
    #         print(f"Task ID {task_id} not found.")
    #         return False
    #     # Simulate evaluation logic
    #     print(f"Evaluating task: {task['task_id']}")        
    #     eval_block = task['eval']
    #     result = False
    #     for eval_type in eval_block['eval_type']:
    #         print(f"Evaluating {eval_type}...")
    #         handler = handlers.get(eval_type)
    #         if handler:
    #             if not handler(target_conf=eval_block[eval_type], agent_result=agent_result, task=task['task_description'], browser=browser):
    #                 print(f"Evaluation failed for {eval_type}")
    #                 return False  # Nếu 1 điều kiện fail → fail toàn bộ
    #             result = True
    #         else:
    #             print(f"Unknown eval type: {eval_type}")
    #             return False  # Nếu eval_type không hợp lệ, trả về False

    #     return result
