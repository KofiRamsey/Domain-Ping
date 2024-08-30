#!/usr/bin/env python3

import subprocess
import sys

def ping_domain(domain, count=5):
    try:
        # Run the ping command
        result = subprocess.run(
            ['ping', '-c', str(count), domain],
            capture_output=True,
            text=True
        )

        # Check if the ping was successful
        if result.returncode == 0:
            return "Online"
        else:
            return "Offline"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ping.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    
    # Ping the domain
    status = ping_domain(domain)

    # Print the status
    print(f"{domain.capitalize()} is {status}")
