import subprocess
while True:
    command = input("Enter a command (or 'exit' to quit): ")
    
    if command.lower() == "exit":
        break
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except PermissionError:
        print("Permission denied.")