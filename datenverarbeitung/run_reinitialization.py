import time
import os

current_dir = os.path.dirname(__file__)
reinit_file = "initialize_inventory.txt"
target_file = os.path.join("raw_logs", "2023-08-28 14h-56m.log")
# target_file = "test_reinit.txt"

reinit = open(reinit_file, "r")
target = open(target_file, "a")

# Prevent bugs
target.write("\n")

for line in reinit:
    target.write(line)
    print(line)
    target.close()
    target = open(target_file, "a")
    time.sleep(2.0)

print("\n\n\n")
print("Done.")
