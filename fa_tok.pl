#!/usr/bin/env perl

binmode(STDIN,":utf8");
binmode(STDOUT,":utf8");

while (<>){

    # tokenization

    s/(\P{P})(\p{P}[\p{P}\s\N{U+200C}]|\p{P}\Z)/$1 $2/gs;
    s/(\P{P})(\p{P}[\p{P}\s\N{U+200C}]|\p{P}\Z)/$1 $2/gs;
    s/(\A\p{P}|[\p{P}\s\N{U+200C}]\p{P})(\P{P})/$1 $2/gs;
    s/(\p{P})(?!\1)/$1 $2/gs;
    s/[ \N{U+200C}]{2,}/ /gs;
   
    print;
}
