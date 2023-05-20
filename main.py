import genanki

import style
import words

# define the deck model
my_model = genanki.Model(
    1607392319,
    'English-Persian Vocabulary',
    fields=[
        {'name': 'Word'},
        {'name': 'Definition'},
        {'name': 'Phonetic'},
        {'name': 'PartOfSpeech'},
        {'name': 'Synonyms'},
        {'name': 'Examples'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': style.front(),
            'afmt': style.back(),
        },
    ])
        

# create a new deck
my_deck = genanki.Deck(
    2059400110,
    'General_Vocabulary')


word_list = words.word_list()  
my_notes = []
for word, definition, phonetic, partofspeech, synonyms, examples in word_list:
    note_fields = [
        word,
        definition,
        phonetic,
        partofspeech,
        "&nbsp;".join(synonyms),
        "<br>".join(examples)
    ]
    note = genanki.Note(model=my_model, fields=note_fields)
    my_notes.append(note)
    
# add notes to the deck
for note in my_notes:
   my_deck.add_note(note)

# write the deck to a file
genanki.Package(my_deck).write_to_file('./AnkiDeck.apkg')