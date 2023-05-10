#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) == 0:
        return ""
    # remove leading and trailing white space
    text = text.strip()
    # split text into sentences
    sentences = text.split('.')
    # remove empty sentences
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
    # add indentation to each sentence
    indented_sentences = []
    for s in sentences:
        indented_sentences.append('    ' + s)
    # combine sentences into a single string
    result = '\n\n'.join(indented_sentences)
    # add newline after last sentence
    result += '\n'
    return result
