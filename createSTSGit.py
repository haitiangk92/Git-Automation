import os
import time

os.system("pwd >> temp.txt")

repoName = open("temp.txt", "r").readlines()[0].split("/")[-1].strip().replace(" ","-")
createRepo = f"curl -H \"Authorization: token $GIT_TOKEN\" https://api.github.com/user/repos -d '{{\"name\": \"{repoName}\"}}'"
os.system("rm temp.txt")
os.system(createRepo)

time.sleep(1)
print("\nRepo Created\n")

os.system("git init")
print("\nGit Initiated\n")

with open(".gitignore", 'w') as ignore:
    ignore.write(".classpath\n.project\n/bin/*")
print("\n .ignore File Created\n")

os.system("git add .")
print("\nFiles added\n")
time.sleep(1)

os.system(f"git remote add origin https://github.com/haitiangk92/{repoName}.git")
print("\nRepo Linked to Directory\n")
time.sleep(1)

os.system('git commit -m "first commit"')
print("\nFiles Commited\n")
time.sleep(1)

os.system("git push -u origin master")
print("\n\n***Complete***\n\n")