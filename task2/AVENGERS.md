# 1.Get Status Of SSH Service On Head Node
![Alt Text](./img/ssh-status.png)
### Run this command to get ssh status: 'systemctl status sshd'

# 2.List Of All Running Services On Head Node
![Alt Text](./img/services-list.png)
### Run this command to get services list on head node: 'systemctl list-units --type=service --state=running'

# 3.Identify SSH Process on Compute Node
![Alt Text](./img/htop-commands.png)
### Run this command for htop: 'htop'
### TIP! (Once in htop, press F4 to filter and type ssh to isolate the process)

# 4.CPU Details (Head and Com2) via Tmux
![Alt Text](./img/tmux-analysis.png)
### Run this command to enable tmux: 'tmux' to start new session
### Then hold 'Ctrl + B' together and let go for a split second, then press 'Shift + 5' 
### Type 'sinfo' to view what's haeppening on the cluster.
### Look at the STATE column for com2.
### If it says idle or mix, it has free resources.
### If it says alloc, it is 100% full.
### If it says down or drain, the node is broken/offline.
### Type 'srun -w com(the free node number) --pty /bin/bash' as it is the official way to ask Slurm for a resource allocation and get an interactive job on that node
### type exit on both terminals to return to the main one

# 5. SSH Logs from the Last Hour on Head Node
![Alt Text](./img/ssh-logs.png)
### Type command 'journalctl -u sshd --since "1 hour ago"' to view ssh logs