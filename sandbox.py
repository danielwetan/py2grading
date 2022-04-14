from answer_reader import read_answer_file, read_file_output

answer_file = "answer/sum.txt"
answer = read_answer_file(answer_file)

actual_sum_file = "actual/sum.py"

actual = read_file_output(actual_sum_file, str.encode(answer["input"]))
expected = int(answer["output"])

if int(actual) != int(expected):
  print(f"got {actual} but want {expected}")
else:
  print("correct answer!")