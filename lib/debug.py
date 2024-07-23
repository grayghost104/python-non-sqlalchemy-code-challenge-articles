#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    # print("HELLO! :) let's debug :vibing_potato:")
    au1=Author(name="tom")
    au2=Author(name="sally")

    mag=Magazine(name="stop and shop", category="shopping")

    Article(
        author=au1,
        magazine=mag, 
        title="deadly shopping"
    )


    # Magazine(name = "")
    # Article("")
    # Author(name= "")
    # don't remove this line, it's for debugging!
    ipdb.set_trace()
