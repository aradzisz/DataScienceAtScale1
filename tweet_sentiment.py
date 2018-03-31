import sys
import json

def construct_dict():
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    #print (scores.items()) # Print every (term, score) pair in the dictionary    

def decode_json(file_to_decode):
   ftd = open(file_to_decode, "r", encoding = 'utf8')
   text = ftd.read()
   line = ftd.readline()
#       decoded = json.load(line)
       
   print(line)
    
def decode2(file_to_decode):
    tweets = []
    with open(file_to_decode) as f:
        for line in f.readlines():
            lines = line.encode('utf8','replace')
            print(type(lines)

    

def lines(fp):
    print (str(len(fp.readlines())))

def main():
       
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #construct_dict()
    decode2("problem_1_submission.json")
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
