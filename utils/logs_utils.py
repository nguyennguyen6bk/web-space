
import logging

logger = logging.getLogger("evaluation_logger")
logger.setLevel(logging.INFO)

# --- Rất quan trọng: Xóa tất cả các handler hiện có để tránh trùng lặp hoặc ghi đè ---
# Điều này đảm bảo rằng logger của bạn chỉ có các handler mà bạn muốn.
if logger.hasHandlers():
    logger.handlers.clear()

# Tạo FileHandler
file_handler = logging.FileHandler("logs/evaluation.log", mode="a")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)