import subprocess


while True:
    try:
        command = input("> ")
        if command.lower() == "exit":
            break
        else:
            subprocess.run(command.lower())
    except Exception:
        print("Not command like that.......")

print("5ee Y0u 500n")


   