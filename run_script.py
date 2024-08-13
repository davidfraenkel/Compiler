import sys
import subprocess

def run_python_file(file_path):
    result = subprocess.run(["python", file_path])
    return result.returncode

if __name__ == "__main__":
    sys.exit(run_python_file(sys.argv[1]))