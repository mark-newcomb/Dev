#!/bin/zsh

echo 'Hello, world!'

bash --version

pwd

mkdir -p practice_bash/test_bash
cd practice_bash
touch test_file_1.txt test_file_2.txt test_file_3.txt
ls -la

cat < test_file_1.txt > test_file_2.txt
cat test_file_2.txt

cp test_file_1.txt test_file_4.txt
mv test_file_3.txt test_file_5.txt

rm -f test_file_5.txt

# alias ll='ls -la'

# Continue at W3 Schools: Text Processing section
