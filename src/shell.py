import os
import sys
import subprocess

def run_shell():
    print("Welcome to the Custom Py-Shell. Type 'exit' to quit.")
    while True:
        try:
            line = input("py-shell> ").strip()
            if not line: continue
            if line.lower() == 'exit': break
            
            # Simple process fork or subprocess run
            parts = line.split()
            cmd = parts[0]
            subprocess.run(parts, shell=True)
        except KeyboardInterrupt:
            print("\nUse 'exit' to close shell.")
        except Exception as e:
            print("Error executing command:", e)

if __name__ == "__main__":
    run_shell()
