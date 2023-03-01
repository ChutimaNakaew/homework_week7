import argparse

parser = argparse.ArgumentParser()
parser.add_argument("txt")
args = parser.parse_args()

if args.txt == 'name':
  print('Alice')
elif args.txt == 'age':
  print(20)
   
