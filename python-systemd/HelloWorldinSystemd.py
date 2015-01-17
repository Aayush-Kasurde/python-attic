from systemd import journal

journal.send("Hello World")
# See output of command using 
# CMD> journalctl _COMM=python