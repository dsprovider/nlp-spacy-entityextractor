# 🧩 Entity Extraction with SpaCy and POS Tagging Rules 🧩

This repository is a Python-based project focused on exploring two methods of entity extraction using the SpaCy NLP library. The main goal of the project is to provide a script that takes a folder path containing text files (e.g., articles or news pieces) as input and generates a CSV file as output. This CSV file will contain extracted entities from each text file, streamlining and speeding up content comprehension.

# 🌟 Features

**1. Custom POS Tagging Rules 🎩:**

  - A series of POS tag patterns to capture entities in a more granular way, without relying solely on existing models.

  - Based on sequences of POS tags (e.g., DET + ADJ + NOUN) to identify meaningful chunks of text.
    

**2. SpaCy's Built-In NER 🔍:**

  - Uses SpaCy's Named Entity Recognition (NER) to identify common entities such as ORG (organizations), GPE (geopolitical entities), or PERSON (individuals).

# 🛠️ How It Works

This project revolves around two key approaches:

**1️⃣ POS-Based Rule Extraction**

Using a custom rule-based approach, this method tags entities based on predefined patterns of POS tags. This is useful for cases where you want more control over what constitutes an entity.

Examples of Rules:

*DET + ADJ + NOUN*
*NOUN + VERB + ADJ*
*PROPN + AUX + VERB*

To see all patterns in action, check the rules list in the code.

**2️⃣ SpaCy's Built-In NER Extraction**

This project also uses SpaCy's NER pipeline to capture entities with established labels:

* *ORG* for organizations
* *GPE* for geopolitical entities
* *PERSON* for individuals
* …and more

# 🏗️ Code Overview

1. **Import Libraries 📚:** Essential packages for NLP tasks.

2. **Download SpaCy Model 📥:** *python -m spacy download en_core_web_sm*.

3. **Load SpaCy Model 🧠:** Loads the *en_core_web_sm model* to power our extractions.

4. **Define POS Rules 🎛️:** Custom patterns to catch entities based on POS tagging.

5. **Extraction Functions:**

   * **extract_entities 🕵️:** Extract entities based on our POS tag rules.
  
   * **extract_named_entities 🕶️:** Use SpaCy’s built-in NER model for broader entity coverage.

# 🚀 Getting Started

1. **Clone this repo:**

   *git clone https://github.com/dsprovider/nlp-spacy-entityextractor.git*

   *cd nlp-spacy-entityextractor*

2. **Install the dependencies:**

   *pip install -r requirements.txt*

3. **Input your text data:** Point to your directory of text files (change *directory* in main() to your directory path)
   
4. **Run the Code:**

   *python entity_relevance_classifier.py*


# 📜 Sample Outputs

Running the Python script will generate a CSV file that contains the following columns:

* **filename:** Name of the processed text file.

* **entities_summary:** Contains entities extracted from the text based on predefined POS rules, joined with a ' - ' separator. This column provides a concise summary of the text, allowing users to understand the main content without reading the entire text.

* **NER entities:** Lists identified Named Entity Recognition (NER) entities, which may include 'DATE','EVENT', 'GPE', 'LOC', 'ORG', 'PERSON' or 'TIME'. This column offers a quick insight into the text's subject, intended to be even faster to read than the details in entities_summary.

# 🔜 Upcoming Features

* Ideally, **this project could integrate a web scraping** phase to automatically collect data from relevant websites. Once the data is gathered, the entity extraction process would run, providing a quick, high-level summary of the content. This output could be designed for inclusion in executive reports, offering clear and concise insights for those with limited time who need strong, to-the-point headlines.

* **Explore NLTK as a potential feature in future testing phases to assess its performance further, despite initial tests indicating lower precision compared to SpaCy**. This additional evaluation could provide deeper insights into NLTK's capabilities and identify specific cases where it may still be effective.










