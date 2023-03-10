#!/usr/bin/python3
def multiple_return(sentence):
    return len(sentence), sentence[0] if sentence else None
