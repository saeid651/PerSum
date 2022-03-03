#!/usr/bin/env perl

binmode(STDIN,":utf8");
binmode(STDOUT,":utf8");

while (<>){

    # sentence splitting

    s/([\.\!\?\N{U+2E2E}\N{U+061F}][\"\'\N{U+200C}]?)\s+/$1\n/gs;

    print;
}
