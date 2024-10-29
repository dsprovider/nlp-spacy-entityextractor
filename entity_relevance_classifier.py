# [1] -- Import Generic Libraries
import os
import csv
from datetime import datetime
from collections import OrderedDict

# [2] -- Import Specific NLP Libraries
import spacy

# ====================================================================================================================================

# Load the English model for spaCy
nlp = spacy.load("en_core_web_sm")

# Define POS tag patterns (rules)
rules = [
    ['DET', 'ADJ', 'NOUN'],
    ['DET', 'ADJ', 'ADJ', 'NOUN'],
    ['DET', 'NOUN', 'VERB'],
    ['DET', 'NOUN', 'VERB', 'ADJ'],
    ['DET', 'NOUN', 'VERB', 'NOUN'],
    ['DET', 'NOUN', 'VERB', 'ADJ', 'NOUN'],
    ['DET', 'NOUN', 'VERB', 'DET', 'NOUN'],
    ['DET', 'NOUN', 'VERB', 'DET', 'ADJ','NOUN'],
    ['DET', 'NOUN', 'AUX', 'NOUN'],
    ['DET', 'NOUN', 'AUX', 'ADJ', 'NOUN'],
    ['DET', 'NOUN', 'AUX', 'ADJ'],

    ['DET', 'VERB', 'PART', 'VERB', 'NOUN'],
    ['DET', 'VERB', 'PART', 'VERB', 'DET', 'NOUN'],
    ['DET', 'VERB', 'PART', 'VERB', 'DET', 'ADJ', 'NOUN'],
    ['DET', 'VERB', 'PART', 'VERB', 'ADJ', 'NOUN'],
    ['DET', 'VERB', 'PART', 'VERB', 'ADP', 'NOUN'],
    ['DET', 'VERB', 'PART', 'VERB', 'ADP', 'DET', 'NOUN'],
    ['DET', 'VERB', 'PART', 'VERB', 'ADP', 'DET', 'ADJ', 'NOUN'],
    
    ['ADJ', 'NOUN', 'VERB'],
    ['ADJ', 'NOUN', 'ADP', 'DET', 'NOUN'],

    ['ADV', 'VERB', 'PRON', 'NOUN'],
    ['ADV', 'VERB', 'DET', 'NOUN'],
    
    ['VERB', 'ADJ', 'NOUN'],
    ['VERB', 'DET', 'NOUN'],
    ['VERB', 'DET', 'ADJ', 'NOUN'],
    ['VERB', 'ADP', 'PRON', 'NOUN'],
    ['VERB', 'ADP', 'DET', 'NOUN'],
    ['VERB', 'ADP', 'PRON', 'ADJ', 'NOUN'],
    ['VERB', 'ADP', 'DET', 'ADJ', 'NOUN'],
    
    ['NOUN', 'ADP', 'PROPN'],              
    ['NOUN', 'VERB', 'NOUN'],
    
    ['PROPN', 'NOUN'],
    ['PROPN', 'PROPN'],
    ['PROPN', 'PROPN', 'NOUN'],
    ['PROPN', 'PROPN', 'AUX', 'VERB', 'PART', 'VERB', 'ADP', 'DET', 'ADJ', 'NOUN'],
    ['PROPN', 'PROPN', 'AUX', 'VERB', 'PART', 'VERB'],
    ['PROPN', 'PROPN', 'AUX', 'VERB', 'PART', 'NOUN'],
    ['PROPN', 'PROPN', 'AUX', 'VERB', 'PART', 'PROPN', 'PROPN'],
    ['PROPN', 'PROPN', 'AUX', 'ADV', 'VERB', 'PART'],
    ['PROPN', 'PROPN', 'AUX', 'VERB', 'PART'],
    ['PROPN', 'PROPN', 'AUX', 'VERB'],
    ['PRON', 'VERB', 'PRON'],
    ['PRON', 'VERB', 'PART', 'VERB', 'NOUN'],
    ['PRON', 'VERB', 'PART', 'VERB', 'DET', 'NOUN'],
    ['PRON', 'VERB', 'PART', 'VERB', 'DET', 'ADJ', 'NOUN'],
    ['PRON', 'VERB', 'PART', 'VERB', 'ADJ', 'NOUN'],
    ['PRON', 'VERB', 'PART', 'VERB', 'ADP', 'NOUN'],
    ['PRON', 'VERB', 'PART', 'VERB', 'ADP', 'DET', 'NOUN'],
    ['PRON', 'VERB', 'PART', 'VERB', 'ADP', 'DET', 'ADJ', 'NOUN'],
    ['PRON', 'VERB', 'DET', 'ADJ', 'NOUN'],
    ['PRON', 'AUX', 'DET', 'ADJ', 'NOUN'],
    ['PRON', 'AUX', 'VERB', 'DET', 'NUM', 'NOUN'],
    ['PRON', 'AUX', 'VERB', 'NOUN'],
    ['PRON', 'AUX', 'VERB', 'DET', 'NOUN'], 
]

# ====================================================================================================================================

# *************************************
# *** FUNCTIONS TO EXTRACT ENTITIES ***
# *************************************

def extract_entities(doc):
    all_entities = []
    all_pos_tag_entities = []

    # Loop over text sentence
    for sent in doc.sents:

        # Apply POS tagging
        pos_tagged_tokens = [(token.text, token.pos_) for token in sent]

        # Extract entities from sentences based off predefined rules
        entities = extract_matching_patterns(pos_tagged_tokens, rules)
        all_pos_tag_entities.extend(entities)

    for match in all_pos_tag_entities:
        extracted_text = " ".join([token[0] for token in match])
        extracted_text = extracted_text.strip()
        all_entities.append(extracted_text)

    all_entities = remove_duplicates(all_entities)

    return all_entities


# Function to check if a subsequence matches any rule
def matches_rule(subsequence, rules):
    pos_sequence = [pos for _, pos in subsequence]  # Extract the POS tags
    return any(pos_sequence == rule for rule in rules)  # Check if POS sequence matches any rule

# Function to extract matching patterns without duplicates
def extract_matching_patterns(pos_tagged_tokens, rules):
    matches = []  # List to store matched patterns
    n = len(pos_tagged_tokens)  # Number of tokens in the list
    i = 0  # Start from the first token

    # Iterate over the tokens and check for each possible subsequence
    while i < n:
        matched = False
        for rule in rules:
            rule_len = len(rule)  # Get the length of the current rule
            if i + rule_len <= n:  # Ensure subsequence doesn't exceed the token list
                subsequence = pos_tagged_tokens[i:i + rule_len]  # Get the subsequence of tokens
                if matches_rule(subsequence, rules):  # Check if it matches any rule
                    matches.append(subsequence)  # If a match, append the subsequence to matches
                    i += rule_len  # Move the sliding window ahead by the length of the rule
                    matched = True
                    break  # Break the inner loop after finding a match, move to the next set of tokens
        if not matched:
            i += 1  # If no match, move to the next token

    return matches

# ********************************
# *** NAMED ENTITIES FUNCTIONS ***
# ********************************

def extract_named_entities(doc):
    data = {}
    entity_types = ['DATE', 'EVENT', 'GPE', 'LOC', 'ORG', 'PERSON', 'TIME']

    # Loop over named entities in the document
    for ent in doc.ents:
        label = ent.label_ # Get the label (e.g., PERSON, ORG, etc.)
        
        if label in entity_types:
            # If the label is not already in the dictionary, add it with the entity text in a list
            if label not in data:
                data[label] = [ent.text]
            # If the label is already in the dictionary, append the new entity text
            else:
                data[label].append(ent.text)

    data = normalize_dictionary(data, entity_types)

    return data  # Return the dictionary of named entities

# ====================================================================================================================================

# **************************
# *** GENERIC FUNCTIONS  ***
# **************************

def normalize_dictionary(input_dict, required_keys):
    # Create a new dictionary with each required key, defaulting to an empty string if missing
    normalized_dict = {key: input_dict.get(key, "") for key in required_keys}
    return normalized_dict


# Preserves the order of the list
def remove_duplicates(input_list):
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

def remove_duplicate_entries_from_dictionary(dictionary):
    for key in dictionary:
        # Update the dictionary in place with the unique values list
        dictionary[key] = list(OrderedDict.fromkeys(dictionary[key]))
    return dictionary


def read_file(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f">> Error: The file '{filename}' was not found."
    except Exception as e:
        return f">> Error: {e}"

# ====================================================================================================================================

def main():
    
    directory = r"<directory_path_containing_text_files>"

    csv_filename = f"Report_" + datetime.now().strftime("%Y-%m-%d %H%M%S") + ".csv"
    csv_filepath = os.path.join(os.path.join(os.getcwd(), "out"), csv_filename)

    csv_header = ['filename', 'entities_summary', 'DATE', 'EVENT', 'GPE', 'LOC', 'ORG', 'PERSON', 'TIME']

    # Open (or create) a CSV file in write mode
    with open(csv_filepath, mode="w", newline="") as file:
    
        # Create a writer object with '|' as the delimiter
        writer = csv.writer(file, delimiter="|")

        # Write the header
        writer.writerow(csv_header)

        for filename in os.listdir(directory):
            print(f">> Processing and extracting entities from ... {filename}")
            filepath = os.path.join(directory, filename)
            text = read_file(filepath)
            doc = nlp(text)
            
            # --- [1] Entities extraction based on predefined POS rules ---
            entities = extract_entities(doc)
            entities_summary = " - ".join(entities)

            # --- [2] SpaCy NER ---
            ner_entities = extract_named_entities(doc)
            ner_entities = remove_duplicate_entries_from_dictionary(ner_entities)

            # Prepare the row for CSV
            row = [filename] + [entities_summary] + list(ner_entities.values())
            
            # Write the row to the CSV file
            writer.writerow(row)

    print("\n\n>> CSV file created successfully at:", csv_filename)
    

if __name__ == "__main__":
    main()
