import traceback
if __name__ == '__main__':
  
  data = [line.rstrip('\n') for line in open('test_file.txt')]
  total = 0
  for line in data:
    try:
      stat = line.split(':')[0]
      val  = line.split(':')[1]
      good = int(val)
      if stat in ['Vitality', 'Luck']:
        difference = good
      else:
        difference = good + 3
      total += difference
    except Exception as e:
      traceback.print_exc()
      print("bad line {0}".format(line))
  print(total)
