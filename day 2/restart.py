# ── CONCEPT 1: Variables & Data Types ──────────────────
# What you need to know for security scripting

# Strings (used for IP addresses, passwords, log lines)
ip_address = "192.168.1.1"
hostname = "target-server.com"
log_entry = "2024-01-15 FAILED LOGIN from 192.168.1.100"

# Integers (used for ports, counts, timestamps)
port = 8080
max_attempts = 5
timeout = 30

# Booleans (used for flags: is_open, is_vulnerable)
port_open = True
is_admin = False

# Lists (used for storing multiple IPs, ports, results)
common_ports = [21, 22, 23, 25, 53, 80, 443, 3389]
suspicious_ips = ["10.0.0.5", "192.168.1.100", "172.16.0.1"]

# Dictionaries (used for storing structured scan results)
scan_result = {
    "ip": "192.168.1.1",
    "port": 80,
    "status": "open",
    "service": "HTTP"
}

# ── PRACTICE EXERCISE ───────────────────────────────────
# Create variables for a fake target:
# - target_ip (string)
# - ports_to_scan (list of 5 ports)
# - scan_results (empty dictionary)
# Print all three using print()
target_ip='123.456.789.101112'
ports_to_scan='78,55,22,66,665'
scan_result={}
print ("target ip:", target_ip)
print("ports:",ports_to_scan)
print("result", scan_result)



# ── CONCEPT 2: If/Else Logic ────────────────────────────
# Critical for: "if port is open, do X. If not, do Y"
# port_status = "open"
#port_number = 22

#if port_status == "open":
#    print(f"[ALERT] Port {port_number} is open!")
#elif port_status == "filtered":
#   print(f"[WARN] Port {port_number} is filtered")
#else:
#   print(f"[OK] Port {port_number} is closed")

# ── PRACTICE EXERCISE ───────────────────────────────────
# Write an if/else block that:
# - If port == 22: print "SSH detected - check auth logs"
# - If port == 3389: print "RDP detected - high risk"
# - If port == 80: print "HTTP detected - check for HTTPS redirect"
# - Else: print "Unknown service on port X"

# PRACTICE: check service by port
port_number=22
if port_number == 22:
    print("SSH detected - check auth logs")
elif port_number == 3389:
    print("RDP detected - high risk")
elif port_number == 80:
    print("HTTP detected - check for HTTPS redirect")
else:
    print(f"Unknown service on port {port_number}") #f string stores directly unknown data

    # ── CONCEPT 3: Loops ────────────────────────────────────
# Critical for: scanning multiple ports, reading log lines

# For Loop (when you know the range)
ports = [22, 80, 443, 8080, 3389]

for port in ports:
    print(f"Checking port: {port}")

# Range-based loop (scan ports 1 to 1024)
for port in range(1, 1025):
    print(f"Scanning port {port}")   # We will use socket here later

# While Loop (when you don't know when to stop)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    print(f"Login attempt {attempts + 1}")
    attempts += 1

# ── PRACTICE EXERCISE ───────────────────────────────────
# Write a loop that:
# - Goes through this list of IPs: ["192.168.1.1",
#   "192.168.1.2", "192.168.1.3"]
# - Prints: "Scanning target: <ip>" for each one
target_ip = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
for ip in target_ip:
    print(f"Scanning target: {ip}")


# ── CONCEPT 4: Functions ─────────────────────────────────
# Critical for: reusable scan modules, tool building

# Basic function
def scan_port(ip, port):
    print(f"Scanning {ip}:{port}")
    return True   # Will return real result later

# Function with default value
def check_host(ip, timeout=3):
    print(f"Checking {ip} with {timeout}s timeout")

# Function that returns a value
def is_admin_port(port):
    admin_ports = [22, 23, 3389, 5900]
    if port in admin_ports:
        return True
    return False

# Calling functions
result = is_admin_port(22)
print(f"Is admin port: {result}")

# ── PRACTICE EXERCISE ───────────────────────────────────
# Write a function called analyze_port(port_number) that:
# - Returns "HIGH RISK" if port is 23 (Telnet) or 3389 (RDP)
# - Returns "MEDIUM RISK" if port is 21 (FTP) or 80 (HTTP)
# - Returns "LOW RISK" for everything else
# Test it with 5 different ports
def analyze_port(port_number):
    if port_number in [23, 3389]:
        return "HIGH RISK"
    elif port_number in [21, 80]:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"
    
# ── CONCEPT 5: Working with Files ───────────────────────
# Critical for: reading log files, saving scan results

# Reading a file (log analysis)
with open("server.log", "r") as file:
    lines = file.readlines()   # Each line as a list item
    for line in lines:
        print(line.strip())    # strip() removes \n

# Writing results to a file
scan_results = ["192.168.1.1:80 OPEN", "192.168.1.1:443 OPEN"]

with open("results.txt", "w") as file:
    for result in scan_results:
        file.write(result + "\n")

# Appending to a file (don't overwrite, just add)
with open("results.txt", "a") as file:
    file.write("Scan completed at 14:30\n")

    # ── CONCEPT 6: Imports ──────────────────────────────────
# Critical for: using Python's built-in security libraries

import socket          # Network connections
import os              # Operating system operations
import sys             # System arguments (command line)
import datetime        # Timestamps for logs
import json            # Parsing API responses
import re              # Regex for log parsing

# Using datetime (for scan timestamps)
now = datetime.datetime.now()
print(f"Scan started at: {now}")

# Using sys.argv (command line arguments)
# Run script as: python scanner.py 192.168.1.1
if len(sys.argv) > 1:
    target = sys.argv[1]
    print(f"Target: {target}")

    # ── CONCEPT 7: Error Handling ───────────────────────────
# Critical for: scripts that MUST NOT crash

# Without error handling (script crashes on failure)
# result = socket.connect(("192.168.1.1", 80))  ← crashes

# With error handling (professional approach)
import socket

def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return "OPEN"
        else:
            return "CLOSED"
    except socket.timeout:
        return "TIMEOUT"
    except socket.error as e:
        return f"ERROR: {e}"
    finally:
        sock.close()   # Always close the socket

# ── DAILY TASK ──────────────────────────────────────────
# Combine everything:
# Write a script that reads a file called "ports.txt"
# (create it with ports: 80, 443, 22, 3389, one per line)
# For each port, call your analyze_port() function
# Save results to "port_analysis.txt"
# Wrap everything in try/except
def analyze_port(port):
    if port == 22:
        return "SSH detected - check auth logs"
    elif port == 3389:
        return "RDP detected - high risk"
    elif port == 80:
        return "HTTP detected - check for HTTPS redirect"
    elif port == 443:
        return "HTTPS detected - secure traffic"
    else:
        return f"Unknown service on port {port}"

try:
    # Step 1: Read ports from file
    with open("ports.txt", "r") as infile:
        ports = infile.readlines()

    results = []

    # Step 2: Process each port
    for line in ports:
        line = line.strip()  # remove newline
        if line.isdigit():   # ensure it's a number
            port = int(line)
            result = analyze_port(port)
            results.append(result)
        else:
            results.append(f"Invalid entry: {line}")

    # Step 3: Save results to output file
    with open("port_analysis.txt", "w") as outfile:
        for r in results:
            outfile.write(r + "\n")

    print("Analysis complete. Results saved to port_analysis.txt")

except FileNotFoundError:
    print("Error: ports.txt not found. Please create the file with ports listed one per line.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

