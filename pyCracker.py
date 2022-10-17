
# Author: David Chidester 2021

import hashlib
import json
import threading
from argparse import ArgumentParser

def main():
    description = """
    The bruteForce password cracker takes in a word list and runs a dictionary attack. \
    These flags are require: -a hashing algorithm, -w word list. \
    You must use either -i for inputting hashes from a file, or -r for raw input. \
    For raw input with multiple hashes, surround in double quotes and deliminate with a space \
    -o is an optional flag for output file which will output results in json format. \
    This program is intended for educational purposes and to explain how professional \
    pen-testing tools like John The Ripper work. It isn't meant to have preformance \
    or features on par with professional tools.
    """
    parser = ArgumentParser(description=description)
    parser.add_argument("-a", "--algorithm", help="Hashing algorithm", required=True)
    parser.add_argument("-i", "--hash", help="Hash List", required=False)
    parser.add_argument("-r", "--raw", help="Raw Input", required=False)
    parser.add_argument("-w", "--wordlist", help="Word List", required=True)
    parser.add_argument("-o", "--output", help="Output File", required=False)

    args = parser.parse_args()
    # args can't be null
    assert (args.algorithm != None), "algorithm hashing must be specified"
    # xor logic with input from file and raw input
    assert ((args.hash != None or args.raw != None)), "hash must be specified"
    assert ((args.hash == None) or (args.raw == None)), "can't input hash raw and from file"
    assert (args.wordlist != None), "word list must be specified"

    # Select an algorithm
    supportedAlgs = ["md5", "sha256", "sha1"]
    assert (args.algorithm in supportedAlgs), "{} isn't a supported algorithm".format(args.algorithm)
    if args.algorithm == "md5":
        hashSum = lambda string : hashlib.md5(string.encode("UTF-8")).hexdigest()
    if args.algorithm == "sha256":
        hashSum = lambda string : hashlib.sha256(string.encode("UTF-8")).hexdigest()
    if args.algorithm == "sha1":
        hashSum = lambda string : hashlib.sha1(string.encode("UTF-8")).hexdigest()

    # Select file containing hashes
    if args.hash != None:
        hashList = open(args.hash, 'r', encoding="utf-8").read().splitlines()
    if args.raw != None:
        hashList = str(args.raw).split(" ")

    # Select wordlist
    wordList = open(args.wordlist, 'r', encoding="utf-8").read().splitlines()

    #crack passwords
    bruteForce(hashList, wordList, hashSum, args)

def bruteForce(hashList, wordList, hashSum, args):
    # Checking for matching hashes
    res = {}
    # Output to terminal?
    printMatch = args.output == None
    for hash in hashList:
        for word in wordList:
            if hashSum(word) == hash:
                if args.output == None: # No output file. Print output instead
                    print(f"Match found! {word} ---> {hash}"
                res[word] = hash
                break
    # no matches found
    if len(res) < 1:
        print("Sorry, no passwords were cracked")
        return
    if args.output != None: # Output file was specified
        file = open(args.output, 'w', encoding="UTF-8")
        file.write(json.dumps(res, indent=0))
        file.write('\n')
        file.close()
    print("done")

def checkMatch(hash, plaintxt, hashSum, printMatch):
    if hashSum(plaintxt) == hash:
        if printMatch:
            print(f"Match found! {plaintxt} ---> {hash}")

main()
