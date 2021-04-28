# PyCracker
PyCracker is a brute force password cracker written in python. It was designed to teach people about pen-testing tools like John The Ripper. By using this software, you agree to use it responsibly. Under the MIT license, the author(s) is/are not liable for missuse of this software.

## Usage

PyCracker takes command line argurments using several flags
|flag|long flag|necessary|example|description|
|--|--|--|--|--|
|h|--help|optional|--help|get help|
|-a|--algorithm|manditory|-a md5|Which hashing algorithm to use|
|-i|--hash|needed if -r isn't used|-i hashes.txt|Input file containing hashes|
|-r|--raw|needed if -i isn't used|-r acbd18db4cc2f85cedef654fccc4a4d8|A hash or list of hashes|
|-w|--wordlist|manditory|-w rockyou.txt|The wordlist being used|
|-o|--output|optional|-o output.json|File to output to|

Bellow is an example of how the software is used:
```bash
python3 -a md5 -i hash.txt -w rockyou.txt -o results.json
```
If you use --raw to input multiple hashes, put the in double quotes and deliminate with spaces.
