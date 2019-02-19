# dictionary-exercises

-These dictionary exercises include two files:

  ## 1) Initial word tally exercise
      - User enters a sentence, and the function will analyze the text and return the most repeated words in the sentence.
      - For example: The dog jumped over the other dog
        - This will return a dictionary with the key dog having a value of 2, and all the other keys having values of 1.
 
  ## 2) Improved word tally
      - The goal of the first exercise was to get the top three most repeated words in a user entered sentence. However, if there was a tie
      the function would return all the words in the tie, creating dictionaries with lengths > 3.
      - The improved word tally now caps the most repeated word dictionary at 3, even if there is a tie.
