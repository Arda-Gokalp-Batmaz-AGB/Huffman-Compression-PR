import math

def AverageLength(first_data,red_map,green_map,blue_map):
  global total_length
  total_length = len(first_data) * len(first_data[0]) # for each rgb component
  global average_length
  average_length = 0
  key: Node
  maps = [red_map,green_map,blue_map]
  for coded_map in maps:
    for key in coded_map:
      temp_probabilty = key.data / float(total_length)
      average_length = average_length + (temp_probabilty * len(coded_map[key]))

  average_length = average_length / 3
  return average_length

def Entrophy(first_data,red_map,green_map,blue_map):
 # total_length = len(first_data) * len(first_data[0])
  Entropy = 0
  key: Node
  maps = [red_map,green_map,blue_map]
  for coded_map in maps:
    for key in coded_map:
      temp_probabilty = key.data / float(total_length)
      Entropy = Entropy + (temp_probabilty * math.log2(temp_probabilty))
  return -1 * (Entropy / 3)

def CompressionRatio():
  return 8 / average_length


def CalculateAndPrintAll(read_data, red_code_map,green_code_map,blue_code_map):
  avg = AverageLength(read_data, red_code_map,green_code_map,blue_code_map)
  entrophy=Entrophy(read_data, red_code_map,green_code_map,blue_code_map)
  ratio=CompressionRatio()
  print(f"L = {avg}")
  print(f"H = {entrophy}")
  print(f"C = {ratio}")
  print(f"Before Compression = {total_length*3*8} bits")
  print(f"After Compression = {int((total_length*3)*average_length)} bits")

  return [avg,entrophy,ratio,total_length*3*8,int((total_length*3)*average_length)]
 # for coded_map in maps:
  #  for key in coded_map:
   #   temp_probabilty = key.data / float(total_length)
    #  average_length = average_length + (temp_probabilty * len(coded_map[key]))
  #return average_length / 3