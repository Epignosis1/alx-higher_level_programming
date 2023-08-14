#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        first = sentence[0]
        first = None
        return len(sentence),first
    else:
        return len(sentence), sentence[0]
