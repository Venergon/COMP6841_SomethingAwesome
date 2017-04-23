import random

class ArgType:
    def __init__(self, probs_dict):
       self.cumulative_prob = 0

       if probs_dict is None:
           self.const = True
       else:
           self.const = False

           self.chars = []
           self.probs = []

           for char in probs_dict:
               prob = probs_dict[char]
               self.chars.append(char)
               self.probs.append(prob + self.cumulative_prob)
               self.cumulative_prob += prob


    def get_char(self, prob):
        counter = 0
        for i, char_prob in enumerate(self.probs):
            if char_prob >= prob:
                counter = i
                break

        return self.chars[counter]

    def new_char(self, curr_char):
        if self.const:
            return curr_char

        prob = random.random()*self.cumulative_prob

        return self.get_char(prob)
