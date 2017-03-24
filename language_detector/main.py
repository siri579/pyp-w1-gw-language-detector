# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    word_count =0
    lang = None
    
    for lan in languages:
        words = len([word for word in lan['common_words'] if word in text])
        if words > word_count:
            word_count=words
            lang= lan['name']
            
    return lang
    
    
                
                
                
                
                    
           
