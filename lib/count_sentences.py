#!/usr/bin/env python3

class MyString:
  def __init__(self, value):
    if isinstance(value, str):
      self.value = value

  def is_sentence(self, value):
    if self.value.endswith("."):
      return True
    else:
      return False
    
  def is_question(self, value):
    if self.value.endswith("?"):
      return True
    else:
      return False
    
  def is_exclamation(self, value):
    if self.value.endswith("!"):
      return True
    else:
      return False
    
  def count_sentences(self, value):
    value_sentences = self.value.split(".")
    value_questions = self.value.split("?")
    value_exclamations = self.value.split("!")

    sentences = [sentence for sentence in value_sentences]
    questions = [question for question in value_questions]
    exclamations = [exclamation for exclamation in value_exclamations]

    return len(sentences) +len(questions) +len(exclamations)


