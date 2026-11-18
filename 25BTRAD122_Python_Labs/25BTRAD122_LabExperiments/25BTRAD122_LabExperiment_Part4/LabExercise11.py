filename = "application.log"

counts = {
    "ERROR": 0,
    "WARNING": 0,
    "INFO": 0
}

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("The log file is empty.")

    else:
        for line in lines:
            log = line.upper()

            if "ERROR" in log:
                counts["ERROR"] += 1
            elif "WARNING" in log:
                counts["WARNING"] += 1
            elif "INFO" in log:
                counts["INFO"] += 1

        print("\n===== LOG FILE SUMMARY =====")
        print("Total log entries:", len(lines))
        print("ERROR:", counts["ERROR"])
        print("WARNING:", counts["WARNING"])
        print("INFO:", counts["INFO"])

except FileNotFoundError:
    print("Error: Log file not found.")

except PermissionError:
    print("Error: Permission denied while accessing the file.")

except Exception as e:
    print("An unexpected error occurred:", e)
