# Sentiment Analysis with Zemberek

This project implements a Turkish sentiment analysis pipeline using the Zemberek NLP library for preprocessing and emoticon handling. It processes positive and negative reviews, normalizes them, marks negations, and replaces emoticons with labels for machine learning tasks.

---

## Features

- **Normalization:** Text normalization with Zemberek to standardize input.
- **Negation Handling:** Identifies and marks negated words using Zemberek's morphology analysis.
- **Emoticon Labeling:** Replaces positive and negative emoticons with `POSEMOTION` and `NEGEMOTION` labels.
- **Punctuation Removal:** Removes unnecessary punctuation for cleaner text.
- **Whitespace Cleanup:** Eliminates extra whitespaces to maintain consistent formatting.
- **Batch Processing:** Reads from input files, processes reviews, and writes output to new files.

---

## Project Structure

```
.
├── pozitif_yorumlar.txt          # Input: Raw positive reviews
├── negatif_yorumlar.txt          # Input: Raw negative reviews
├── on_pozitif_yorumlar.txt       # Output: Processed positive reviews
├── on_negatif_yorumlar.txt       # Output: Processed negative reviews
├── sentiment_processor.py        # Script for preprocessing reviews
└── README.md                     # Project documentation
```

---

## Workflow

1. **Load Reviews:**
   - Reads reviews from `pozitif_yorumlar.txt` and `negatif_yorumlar.txt`.

2. **Preprocess Reviews:**
   - Normalize text using Zemberek.
   - Identify and label negations.
   - Replace emoticons with corresponding sentiment labels.
   - Remove punctuation and extra whitespaces.

3. **Save Processed Reviews:**
   - Writes preprocessed reviews to `on_pozitif_yorumlar.txt` and `on_negatif_yorumlar.txt`.

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install Zemberek dependencies:
   - Follow the [Zemberek setup guide](https://github.com/ahmetaa/zemberek-nlp) to configure the Java library.

3. Ensure you have the following Python libraries installed:
   ```bash
   pip install jpype1
   ```

4. Place your `pozitif_yorumlar.txt` and `negatif_yorumlar.txt` files in the project directory.

5. Run the preprocessing script:
   ```bash
   python sentiment_processor.py
   ```

6. Processed reviews will be saved as `on_pozitif_yorumlar.txt` and `on_negatif_yorumlar.txt`.

---

## Dependencies

- Python 3.7+
- Zemberek NLP Library
- JPype1
- re (built-in)
- os (built-in)

---

## Example Output

**Input Review:**
```
Harika bir ürün :) Kesinlikle tavsiye ederim. :)
```

**Processed Review:**
```
Harika bir ürün POSEMOTION Kesinlikle tavsiye ederim POSEMOTION
```

