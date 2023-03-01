import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="the name to greet")
parser.add_argument("age", help="the age of the person being greeted", type=int)
args = parser.parse_args()

if(args.name){
  return 'Alice'
}
else if(args.age){
  return 20
}
   
