import json
import random
import re
from collections import defaultdict


def load_corpus_from_json(file_path: str) -> str:
    """Load sentences from JSON file and combine them into a single cleaned string."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            sentences = data.get("corpus", [])
            # Clean and combine sentences
            cleaned_sentences = []
            for s in sentences:
                # Remove special characters except spaces
                cleaned = re.sub(r"[^\w\s]", "", s.lower())
                cleaned_sentences.append(cleaned)
            return " ".join(cleaned_sentences)
    except (FileNotFoundError, json.JSONDecodeError):
        return ""


def build_markov_model(text: str) -> dict:
    """Build a Markov Chain Model (Current word -> List of next words)."""
    words = text.split()
    model = defaultdict(list)

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        model[current_word].append(next_word)

    return model


def predict_next_words(model: dict, current_word: str) -> dict:
    """Calculate the probability distribution of next words given a current word."""
    current_word = current_word.lower()
    if current_word not in model:
        return {}

    next_words = model[current_word]
    total_count = len(next_words)

    # TODO 3A: Count how many times each word follows current_word.
    word_counts = defaultdict(int)
    for word in next_words:
        word_counts[word] += 1

    # TODO 3B: Convert counts into probabilities (count / total_count).
    # The probabilities of all possible next words should add up to 1.
    probabilities = {word: count / total_count for word, count in word_counts.items()}
    return dict(
        sorted(probabilities.items(), key=lambda item: item[1], reverse=True)
    )


def generate_sentence(model: dict, start_word: str, length: int = 8) -> str:
    """Randomly generate a sentence starting with start_word."""
    current = start_word.lower()
    if current not in model:
        return start_word

    sentence = [current.capitalize()]

    for _ in range(length - 1):
        # TODO 3C: Stop when current has no possible next words.
        # Otherwise, choose a random next word using model[current],
        # update current and append the selected word to sentence.
        if current not in model or not model[current]:
            break
        next_word = random.choice(model[current])
        sentence.append(next_word)
        current = next_word

    return " ".join(sentence) + "."