import math

def AverageLength(first_data,coded_map):
  global total_length
  total_length = len(first_data) * len(first_data[0])
  average_length : float = 0
  key: Node
  for key in coded_map:
    temp_probabilty = key.data / float(total_length)
    average_length = average_length + (temp_probabilty * len(coded_map[key]))
  return average_length

def Entrophy(first_data,coded_map):
  total_length = len(first_data) * len(first_data[0])
  Entropy = 0
  key: Node
  for key in coded_map:
    temp_probabilty = key.data / total_length
    Entropy = Entropy + (temp_probabilty * math.log2(temp_probabilty))
  return -1 * Entropy

def CompressionRatio(first_data,coded_map):
  bit_length_for_each_char = 8 #default is 8
  before_compression = len(first_data) * len(first_data[0]) * bit_length_for_each_char
  after_compression = 0
  key:Node
  for key in coded_map:
    after_compression = after_compression + (len(coded_map[key]) * key.data)
  return before_compression / float(after_compression)

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