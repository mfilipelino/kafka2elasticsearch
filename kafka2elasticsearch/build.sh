#!/usr/bin/env bash

target=kafka2elasticsearch

rm -rf $target
mkdir $target
cp *.py $target
cp *.sh $target
cp *.env $target
cp *.txt $target

days="$(date "+%F %T")"
zip -r kafka2elasticsearch.zip $target


