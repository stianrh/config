#! /bin/sh
echo bind key $1 with $3 in window $2
echo usage: bindkey F1 top-right \"C-c \' ls -a\'\"
eval tmux bind-key -n $1 send-keys -t .$2 $3 ENTER
echo tmux bind-key -n $1 send-keys -t .$2 $3 ENTER
