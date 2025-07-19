import json
import ast

def normalize_agent_result(agent_result):
    # Nếu đã là Python dict/list/tuple → giữ nguyên
    if isinstance(agent_result, (dict, list, tuple)):
        return agent_result
    
    # Nếu là string → thử chuyển
    if isinstance(agent_result, str):
        # 1) Thử JSON
        try:
            parsed = json.loads(agent_result)
            return parsed
        except json.JSONDecodeError:
            pass

        # 2) Thử Python literal
        try:
            parsed = ast.literal_eval(agent_result)
            # Chỉ chấp nhận dict/list/tuple, không chấp nhận str/bool/number riêng lẻ
            if isinstance(parsed, (dict, list, tuple)):
                return parsed
        except (ValueError, SyntaxError):
            pass

    # Không parse được → trả lại nguyên string
    return agent_result

cases = [
    '{"a": 1}',          # JSON string
    "{'a': 1}",          # Python literal string
    "[1, 2, 3]",         # JSON array string
    "'Hello'",           # Python literal string (will become 'Hello')
    "Hello",             # Plain string
    {"a": 1},            # dict trực tiếp
    [1, 2, 3],           # list trực tiếp
    ["1", '2', 3],           # list trực tiếp
]

for case in cases:
    print("RAW:", case, "| NORMALIZED:", normalize_agent_result(case))