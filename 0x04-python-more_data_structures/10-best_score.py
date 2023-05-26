#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = max(a_dictionary.values())

    for student, score in a_dictionary.items():
        if score == max_score:
            return student
