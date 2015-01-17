from systemd import journal 

# Follow journalctl 
# using journalctl -f --since "now"
journal.send("Hello World", FIELD2="Greetings", FIELD3="From Python")
