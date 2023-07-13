echo 'Files'
read a
echo 'Message'
read msg
echo $msg >$a
echo `grep -o 'the\|an\|a' $a | wc -w`