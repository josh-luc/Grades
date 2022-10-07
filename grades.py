import sys

def main(text):
    grades = {'Biology':80, 
              'Physics':88, 
              'Chemistry':98, 
              'Math':89, 
              'English':79, 
              'Music':67, 
              'History':68, 
              'Art':53, 
              'Economics':95, 
              'Psychology':88}
    
    x = (sum(grades.values()) - grades[sys.argv[1]]) / (len(grades)-1)
    print(round(x, 2))
    
main(sys.argv[1])