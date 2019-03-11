import os
import csv
def sum_to_n(n, multiplier):
  total = 0
  for level in range(n+1):
    total += (level * multiplier)
  return total

def compute():
  #For every level
  values = list()
  for level in range(0,11):
    level_values = list()
    for multiplier in (2,):
      for vitality in range(0,6):
        #final formula
        # 30 + sum_to_n(level,1) + (level * vitality * 2)
        curr_vitality = 30 + sum_to_n(level, 1) + (level * vitality * multiplier)
        level_values.append(curr_vitality)
    values.append(level_values)

  with open('health_file.csv','w') as outfile:
    writer = csv.writer(outfile)
    for value in values:
      writer.writerow(value)

if __name__ == '__main__':
  compute()
  print('Done.')
    
