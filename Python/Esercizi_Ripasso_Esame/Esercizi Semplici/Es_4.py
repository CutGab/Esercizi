def count_unique_words(text: str) -> dict:

    unique_words: dict = {}

    new_text = text.lower()

    for i in new_text.split():
        
        s = i.strip(",.!?")
        
        if s not in unique_words:
            
            unique_words[s] = 1
        
        else:

            unique_words[s] += 1

    return unique_words

print(count_unique_words("Hello, world! Hello... PYTHON? world."))