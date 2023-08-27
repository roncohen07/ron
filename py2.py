def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"Error: {error_message}\n")

try:
    # הקוד שבו עשוי להתרחש שגיאה
    result = 10 / 0  # דוגמה לשגיאה - חלוקה באפס
except Exception as e:
    error_message = str(e)
    log_error(error_message)
