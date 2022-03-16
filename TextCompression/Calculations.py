import math

def AverageLength(first_data,coded_map):
  global total_length
  global average_length
  total_length = len(first_data)
  average_length = 0
  key: Node
  for key in coded_map:
    temp_probabilty = key.data / total_length
    average_length = average_length + (temp_probabilty * len(coded_map[key]))
  return average_length

def Entrophy(first_data,coded_map):
#  total_length = len(first_data)
  Entropy = 0
  key: Node
  for key in coded_map:
    temp_probabilty = key.data / total_length
    Entropy = Entropy + (temp_probabilty * math.log2(temp_probabilty))
  return -1 * Entropy

def CompressionRatio(first_data,coded_map):
  return 8 / average_length

#def difference()
def CalculateAndPrintAll(first_data,coded_map):
  avg = AverageLength(first_data,coded_map)
  entrophy=Entrophy(first_data,coded_map)
  ratio=CompressionRatio(first_data,coded_map)
  print(f"L = {avg}")
  print(f"H = {entrophy}")
  print(f"C = {ratio}")
  print(f"Before Compression = {total_length*8} bits")
  print(f"After Compression = {int((total_length)*avg)} bits")
  return [avg, entrophy, ratio, total_length * 8, int((total_length) * avg)]