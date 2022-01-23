import subprocess
commit_message = input()
commit_message = "'" + commit_message + "'"

cmd = "git add -A"
args = cmd.split()
subprocess.call(args)

cmd = "git commit -m"
args = cmd.split()
args.append(commit_message)
subprocess.call(args)

cmd = "git push"
args = cmd.split()
subprocess.call(args)

