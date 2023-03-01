import argparse

parser = argparse.ArgumentParser()
parser.add_argument("txt")
args = parser.parse_args()

if args.txt == 'name':
  return 'Alice'
elif args.txt == 'age':
  return 20
   
