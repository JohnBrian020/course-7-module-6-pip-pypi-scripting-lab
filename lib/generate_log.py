from datetime import datetime
import os


def generate_log(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("Data must be a list")

    # Generate today's filename
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # Write data to file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Confirmation message
    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(log_data)