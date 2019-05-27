#! /bin/bash
LIST="list"
if [ "$1" == "$LIST" ]; then
    tmux list-keys | grep send-keys
elif [ "$#" -ne 3 ]; then
    echo usage: bindkey KEY PANE "COMMAND"
    echo list: bindkey list
    echo example: bindkey F1 top-right \"C-c \' ls -a\'\"
else
    eval tmux bind-key -n $1 send-keys -t .$2 $3 ENTER
    echo bind key $1 with \"$3\" in pane \"$2\"
fi
