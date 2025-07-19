import difflib
from dotenv import load_dotenv
import os
import google.generativeai as genai
import unicodedata
def exact(value, target):
    value = normalize(value)
    target = normalize(target)
    print(f"[exact] target: {target}, value: {value}")
    return value == target

def contains(value, target):
    """
    Check if the target is contained within the values.
    """
    print(f"[contains] Comparing: {repr(target)} vs {repr(value)}")
    if not value or not target:
        return False
    value = normalize(value)
    target = normalize(target)
    return target in value


def semantic(task_description, value, target, method="llm"):    
    if method == "llm":
        # TODO: gọi OpenAI API hoặc vector DB

        load_dotenv()
        # api_key = os.getenv("GOOGLE_API_KEY")

        genai.configure(api_key="AIzaSyBIW_lcvc8pCBFrE3J0SXZpfNrwOLK4Yd4")
        
        prompt = f"""
            You are a helpful evaluator.
            Task: "{task_description}"
            Expected answer: "{target}"
            Agent answer: "{value}"
            Are they semantically equivalent in the task context? 
            Reply only YES or NO.
        """
        print(f"[semantic] LLM prompt: {prompt}")
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)
        if response.text.strip().upper() in ["YES", "NO"]:
            # Trả về True nếu trả lời là YES, False nếu NO
            print(f"[semantic] LLM response: {response.text.strip()}")
        return response.text.strip().upper() == "YES"
    elif method == "fuzzy":
        ratio = difflib.SequenceMatcher(None, value, target).ratio()
        if ratio >= 0.8:
            return True
    return False


def starts_with(values, target):
    """
    Check if the values start with the target.
    """
    return values.startswith(target)

def ends_with(values, target):
    """
    Check if the values end with the target.
    """
    return values.endswith(target)



def check_contains(agent_value, match_value):
    """
    Checks if agent_value contains match_value.
    - If match_value is a string: return contains(agent_value, match_value)
    - If match_value is a list: check all items
    """
    print(f"[check_contains] agent_value: {agent_value}, match_value: {match_value}")
    if isinstance(match_value, str):
        return contains(agent_value, match_value)
    elif isinstance(match_value, list):
        if not match_value:
            print("match_value list is empty")
            return False
        for item in match_value:
            if not contains(agent_value, item):
                print(f"Contains check failed for item: {item}")
                return False
        return True
    else:
        print(f"Unsupported match_value type: {type(match_value)}")
        return False
    

def normalize(text):
    """
    Chuẩn hóa chuỗi để so sánh:
    - Ép về str
    - Chuẩn hóa unicode (NFKC)
    - Thay non-breaking space (U+00A0) bằng space thường
    - Bỏ zero-width space, BOM
    - strip() để bỏ khoảng trắng đầu/cuối
    """
    if text is None:
        return ""
    return (
        unicodedata.normalize("NFKC", str(text))
        .replace('\xa0', ' ')     # non-breaking space → space
        .replace('\u200b', '')    # zero-width space
        .replace('\ufeff', '')    # BOM
        .strip()
    )