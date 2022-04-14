import subprocess

def read_answer_file(filename):
  stdin_list = {
    "input": 0,
    "output": 0,
  }
  with open(filename) as file:
    lines = file.readlines()
    stdin_list["input"] = lines[0].strip()
    stdin_list["output"] = lines[1].strip()

  return stdin_list


def read_file_output(path, stdin_bytes):
  process = subprocess.Popen(["python3", path], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  process.stdin.write(stdin_bytes)

  answer_out = str(process.communicate()[0], "UTF-8")
  process.stdin.close()

  return int(answer_out.strip())
