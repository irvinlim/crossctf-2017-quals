while read p; do
    a=`echo "$p"moreThan10CharPassword | shasum -a 256`
    acmp='70e0f6cba9351375d1ec3440c6e2a5e41389d92c632baa1a28ca3d930c4a5a05  -'
    if [ "$a" == "$acmp" ]
    then
        echo $a
    fi
done <john.txt