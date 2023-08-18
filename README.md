# 🌲 ForestRDF: Animal Tracking with SOSA Ontology 🐾

**ForestRDF**, a synthetic dataset tailored for tracking animals in forests. Semantically-structured wildlife movement data, paving the way for testing RDF and Linked-Data extaction techniques. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)



## Installation

You can eaither ***use the generated dataset*** from the dataset folder, or ***regenerate*** your own data using our script.

To generate your own data:

Step 1:
```bash
# Clone this repository
git clone [Repository-Link]

# Navigate to the directory
cd ForestRDF
```

Step 2:
```bash
# Create a virtual environment using Python's built-in `venv` module (you may need to replace `python3` with `python` or `py` depending on your system setup):
python3 -m venv env


# Activate the virtual environment. 

  # On Unix or MacOS, use:
  source env/bin/activate

  #On Windows, use:
  env\Scripts\activate

```

Step 3:

```bash
# Install the required packages. You can install it using requirements.txt:
pip install -r requirements.txt
```

Step 4:

```bash
# You can now run the script using Python:
python3 createData.py
```
## Usage

This generates a TTL format dataset file that you can use for testing. TTL (Turtle) is a format for representing RDF (Resource Description Framework) data, which is a standard for encoding knowledge in the form of triples. To query TTL files, you typically use the SPARQL query language.

For example, if you wanted to retrieve all the sensor in the dataset, your query might look like this:
```SPARQL
SELECT ?s {?s a <http://www.w3.org/ns/sosa/Sensor>}
```

If you are new to RDF datasets and SPARQL, you can use it in one of three way:

- ### Loading TTL File:
    With Apache Jena's TDB (a type of RDF database).

- ### Programmatic Querying:
    If you're working programmatically, many languages have libraries or frameworks for querying RDF. For example, in Python, you can use the rdflib library.

- ### SPARQL Endpoints:
    If you are using a more advanced RDF database (like Virtuoso, Stardog, etc.), they might offer SPARQL endpoints. These are web services that allow you to send SPARQL queries over HTTP and retrieve results.

Remember, these are just basics to get started. RDF and SPARQL have deep capabilities, and there's a lot more to explore depending on your needs.

### For more about SOSA
- https://www.w3.org/2015/spatial/wiki/SOSA_Ontology
- https://github.com/w3c/sdw/tree/gh-pages/ssn/rdf


## Contributing

We welcome contributions! Please feel free to propose enhancements, report bugs, or submit pull requests.
