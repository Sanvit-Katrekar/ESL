# ESL - Generative AI competition
---
## Converting English/Arabic to Emirati Sign Language

### The Plan

Use LLMs (LLAMA2 and JAIS) to convert English/Arabic sentences into ESL animations.

#### Tech stack
* Python for scripting and interfacing with LLMs
* ChromaDB as a vector database for LLM embeddings
* MySQL as simple database
* Blender/(other softwares) for creating animations

### Step 1: Data collection
Scrape ESL videos from the website and add it to MySQL as well as ChromaDB

### Step 2: Convert to Arabic
Convert English meanings to Arabic using JAIS

### Step 3: LLM tactics

Ask LLAMA2 to return an output in the form of the available ESL words given.

This will result in clear ESL grammar (Hopefully).

### Step 4:

Figure out how to get animations for the word structure given by the LLM using the video links.

## Execution
---
1. **Cloning the repo**

Go to desktop and create new folder.

Open terminal and type in:

```zsh
git clone https://github.com/Sanvit-Katrekar/ESL.git
```

Go to VS CODE and open the "ESL" folder.

2. **Installing Requirements**

```zsh
pip install -r requirements.txt
```

3. **Adding env variables**

Create a new file names .env and add the values for the below variables:

MYSQL_HOST=xxx
MYSQL_DATABASE=xxx
MYSQL_USER=xxx
MYSQL_PASSWORD=xxx
MYSQL_PORT=xxx