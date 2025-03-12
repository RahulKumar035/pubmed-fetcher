"# Pubmed Fetcher" 
PubMed Fetcher
A Python tool to fetch research papers from PubMed based on a user-specified query. The program identifies papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.
Features

Fetches papers from PubMed using the PubMed API.
Filters papers with non-academic affiliations (e.g., pharmaceutical or biotech companies).
Saves results in a CSV file with the following columns:

PubmedID
Title
Publication Date
Non-academic Author(s)
Company Affiliation(s)
Corresponding Author Email



Installation

Clone the repository:

bash-
git clone https://github.com/RahulKumar035/pubmed-fetcher.git
cd pubmed-fetcher

Install dependencies using Poetry:

bash-
poetry install
Usage
Run the program with the following command:
bash-
poetry run get-papers-list "your query" -f output.csv
Options

query: The search query for PubMed (e.g., cancer treatment).
-f, --file: Specify the output CSV filename (e.g., output.csv).
-d, --debug: Enable debug mode for additional output.

Example
bashCopypoetry run get-papers-list "cancer treatment" -f output.csv
Project Structure
Copypubmed-fetcher/
├── pubmed_fetcher/
│   ├── __init__.py
│   ├── main.py
│   └── cli.py
├── pyproject.toml
├── poetry.lock
└── README.md
Dependencies

Python: >=3.9
Biopython: For interacting with the PubMed API.
Pandas: For processing and organizing data into a CSV file.
Argparse: For creating the command-line interface.

Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix.
Submit a pull request with a detailed description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

PubMed: For providing the API to access research papers.
Biopython: For simplifying interaction with the PubMed API.
Poetry: For dependency management and packaging.

Contact
For questions or feedback, please contact:

Rahul Kumar
Email: nirajrahul1@gmail.com
GitHub: RahulKumar035
