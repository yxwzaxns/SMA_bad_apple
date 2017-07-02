#!/bin/bash

src_dir=$1
dst_dir=$2
filename=$3

echo "src_dir is : $1"
echo "dst_dir is : $2"
echo "filename is : $3"

if [[ ! -d $2 ]]; then
  mkdir $2
fi
for f in $src_dir/*;do
name=$filename'_'$(echo $f |awk -F '_' '{print $3}')
echo "start mv $f to $dst_dir/$name"

mv $f $dst_dir/$name

done
