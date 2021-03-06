import os
import time
import sys

try:
    commitMessage = ""

    for string in sys.argv[1:len(sys.argv)]:
        commitMessage += f"{string} "

    print(f"Committing with message: {commitMessage}")
except:
    print("\nNo Commit Messsage Detected\n".upper())
    quit()

os.system("git add .")
print("\nFiles Added\n")
time.sleep(1)

os.system(f'git commit -m "{commitMessage}"')
print("\nFiles Committed\n")
time.sleep(1)

os.system("git push -u origin master")
print("\n\n***Complete***\n\n")
