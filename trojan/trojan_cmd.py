# trojan_cmd.py
import os

def fake_payload():
    os.system('start cmd /c "echo kriptoloji & timeout /t 3 >nul"')

if __name__ == "__main__":
    fake_payload()
