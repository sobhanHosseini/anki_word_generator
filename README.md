# Anki Deck Generator

This project generates an Anki deck using words provided in an array.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/anki-deck-generator.git
   ```

2. Navigate to the project directory:
    ```bash
    cd anki-deck-generator
    ```

3. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
## Usage

1. Open the words file located in the project directory.
2. Add the words you want to include in the Anki deck to the array, following this structure for each word:
    ```
    [Word, Definition, Phonetic, PartOfSpeech, Synonyms, Examples]
    ```
    - **Word**: The word itself.
    - **Definition**: The definition or meaning of the word.
    - **Phonetic**: The pronunciation of the word.
    - **PartOfSpeech**: The part of speech of the word.
    - **Synonyms**: Synonyms or similar words to the main word (optional).
    - **Examples**: Examples of how to use the word in a sentence (optional).

    Each word should be on a separate line, and fields should be separated by commas.
3. Save the **`words`** file.
4. Run the main.py script:
    ```
    python main.py
    ```
    This will generate the Anki deck.

5. Once the script completes, a file named **`AnkiDeck.apkg`** will be created in the project directory.

6. Import the AnkiDeck.apkg file into Anki software to use the generated deck.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Fork the repository and create a new branch.

2. Make your changes and test them thoroughly.

3. Submit a pull request describing the changes you've made.

## License

This project is licensed under the **`MIT License`**.

