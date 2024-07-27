import re
from zemberek.morphology import TurkishMorphology
from zemberek.normalization import TurkishSentenceNormalizer
import os

morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)


def normalize_text(text, normalizer):
    return normalizer.normalize(text)

def replace_emoticons_with_labels(text):
    labeled_text = ""
    words = text.split()
    for word in words:
        if re.search(r'[:;]-?[\)]', word):
            labeled_text += "POSEMOTION "
        elif re.search(r'[:;]-?[\(|\[]', word):
            labeled_text += "NEGEMOTION "
        else:
            labeled_text += word + " "
    return labeled_text.strip()

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

def remove_extra_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

def extract_stem_and_mark_negatives(text, morphology):
    words = text.split()
    processed_text = ""
    for word in words:
        analysis_results = morphology.analyze(word)
        stem = word
        for result in analysis_results:
            if not result.is_unknown():
                stem = result.get_stem()
                morphemes = result.get_morphemes()
                if "Neg" in morphemes:
                    stem += "NEG"
        processed_text += stem + " "
    return processed_text.strip()

def read_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def preprocess_reviews(reviews, morphology, normalizer):
    processed_reviews = []
    for review in reviews:
        review = normalize_text(review, normalizer)
        review = extract_stem_and_mark_negatives(review, morphology)
        review = replace_emoticons_with_labels(review)
        review = remove_punctuation(review)
        review = remove_extra_whitespace(review)
        processed_reviews.append(review)
    return processed_reviews

def write_file(file_path, reviews):
    with open(file_path, 'w', encoding='utf-8') as output_file:
        for review in reviews:
            output_file.write(review + '\n')


positive_reviews_file_path = "pozitif_yorumlar.txt"
processed_positive_reviews_file_path = "on_pozitif_yorumlar.txt"

negative_reviews_file_path = "negatif_yorumlar.txt"
processed_negative_reviews_file_path = "on_negatif_yorumlar.txt"

try:
    positive_reviews = read_file(positive_reviews_file_path)
    processed_positive_reviews = preprocess_reviews(positive_reviews, morphology, normalizer)
    write_file(processed_positive_reviews_file_path, processed_positive_reviews)
    print("Pozitif yorumlar işlendi ve kaydedildi:", processed_positive_reviews_file_path)

    negative_reviews = read_file(negative_reviews_file_path)
    processed_negative_reviews = preprocess_reviews(negative_reviews, morphology, normalizer)
    write_file(processed_negative_reviews_file_path, processed_negative_reviews)
    print("Negatif yorumlar işlendi ve kaydedildi:", processed_negative_reviews_file_path)

except FileNotFoundError as e:
    print(e)
