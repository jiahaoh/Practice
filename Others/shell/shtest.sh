#!/usr/bin/env bash

for i in 0 1
do
	sleep 30 &
done
#echo "Your job is done" | mail -s subject jh2050@georgetown.edu &
pid=(`pgrep sleep`)

length=${#pid[@]} # Get the length.
last_p=`expr $length - 1`
last_o=${pid[$last_p]} # Get the last position.
echo "Your last process ID: $last_o"
#nohup ~/app/ncbi-blast-2.7.1+/bin/blastp -query ~/test/split_res_0.fa -db /home/mcgarvey/lily/blastdb/vp -out res_0.xml -outfmt 5 -evalue 1e-4 -num_threads 4
while kill -0 $last_o
do
	continue
done
echo "Your job is done" | mail -s subject jh2050@georgetown.edu &


#nohup ~/app/ncbi-blast-2.7.1+/bin/blastp -query ~/test/split_res_6000.fa -db /home/mcgarvey/lily/blastdb/vp -out res_6000.xml -outfmt 5 -evalue 1e-4 -num_threads 4
