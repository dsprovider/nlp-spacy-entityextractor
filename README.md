# 🧩 Entity Extraction with SpaCy and POS Tagging Rules 🧩

This repository is a Python-based project that explores two methods of entity extraction using SpaCy NLP library.

# 🌟 Features

**1. Custom POS Tagging Rules 🎩:**

  - A series of POS tag patterns to capture entities in a more granular way, without relying solely on existing models.

  - Based on sequences of POS tags (e.g., DET + ADJ + NOUN) to identify meaningful chunks of text.
    

**2. SpaCy's Built-In NER 🔍:**

  - Uses SpaCy's Named Entity Recognition (NER) to identify common entities such as ORG (organizations), GPE (geopolitical entities), and PERSON (individuals).

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

2. **Load SpaCy Model 🧠:** Loads the *en_core_web_sm model* to power our extractions.

3. **Define POS Rules 🎛️:** Custom patterns to catch entities based on POS tagging.

4. **Extraction Functions:**

   * **extract_entities 🕵️:** Extract entities based on our POS tag rules.
  
   * **extract_named_entities 🕶️:** Use SpaCy’s built-in NER model for broader entity coverage.

# 🚀 Getting Started

1. Clone this repo:

2. Install the dependencies:

3. Run the Code:











