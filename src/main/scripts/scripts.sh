#!/bin/zsh

echo 'Hello, world!'

bash --version

pwd

mkdir -p practice_bash/test_bash
cd practice_bash || ( echo "Error trying to cd...exiting."; exit )
touch test_file_1.txt test_file_2.txt test_file_3.txt
ls -la

cat < test_file_1.txt > test_file_2.txt
cat test_file_2.txt

cp test_file_1.txt test_file_4.txt
mv test_file_3.txt test_file_5.txt

rm -f test_file_5.txt

# alias ll='ls -la'

# Continue at W3 Schools: Text Processing section
my_name="Mark"
echo "Hello, ${my_name}"

my_name_function(){
  name=$1
  echo "${name} was given to this function"
}

my_name_function 'Tim'
my_name_function 'Mike'

my_number=$(( 2 + 4 ))
echo $my_number
my_command_result=$(cat test_file_1.txt)
echo "${my_command_result}"

if [[ $my_name == 'Mark' ]]; then
  echo 'Hi Mark'
fi
if (( 6 == 6 )); then
  echo 'Number is 6'
fi

family_members=('Mark' 'Marissa' 'Hazel' 'Hudson')
for member in "${family_members[@]}"; do
  echo "$member"
done

if [[ $my_name == 'Mark' ]] && (( 2 == 3 )); then
  echo 'My name is Mark and the number is 2'
elif [[ $my_name == 'Mar' ]]; then
  echo 'Name is Mar'
else
  echo 'Who are you?'
fi

for i in {1..5}; do
  echo $i
done

