import os

LOG_FILES = [
    "/var/log/syslog",
    "/var/log/messages",
]

CRITICAL_KEYWORDS = [
    "error",
    "failed",
    "critical",
    "panic",
    "segfault",
]


def analyze_logs():
    print("Linux Crash Analyzer")
    print("-" * 40)

    for log_file in LOG_FILES:
        if os.path.exists(log_file):
            print(f"\nAnalyzing: {log_file}")

            try:
                with open(log_file, "r", errors="ignore") as file:
                    lines = file.readlines()

                    for line in lines[-100:]:
                        lower_line = line.lower()

                        for keyword in CRITICAL_KEYWORDS:
                            if keyword in lower_line:
                                print(f"[!] {line.strip()}")

            except PermissionError:
                print("Permission denied.")
        else:
            print(f"{log_file} not found.")


if __name__ == "__main__":
    analyze_logs()
