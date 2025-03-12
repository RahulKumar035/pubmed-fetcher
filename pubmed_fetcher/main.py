from Bio import Entrez
import pandas as pd

# Step 1: Fetch PubMed IDs based on a query
def search_pubmed(query):
    Entrez.email = "your_email@example.com"  # Replace with your email
    handle = Entrez.esearch(db="pubmed", term=query, retmax=10)
    result = Entrez.read(handle)
    return result["IdList"]

# Step 2: Fetch paper details using PubMed IDs
def fetch_paper_details(pubmed_ids):
    handle = Entrez.efetch(db="pubmed", id=pubmed_ids, retmode="xml")
    return Entrez.read(handle)

# Step 3: Process papers into a DataFrame
def process_papers(papers):
    results = []
    for paper in papers["PubmedArticle"]:
        article = paper["MedlineCitation"]["Article"]
        pubmed_id = paper["MedlineCitation"]["PMID"]
        title = article["ArticleTitle"]
        
        # Handle missing or empty ArticleDate
        pub_date = "N/A"
        if "ArticleDate" in article and article["ArticleDate"]:
            pub_date = article["ArticleDate"][0]
        
        # Extract authors and affiliations
        non_academic_authors = []
        company_affiliations = []
        corresponding_email = "N/A"
        
        if "AuthorList" in article:
            for author in article["AuthorList"]:
                if "AffiliationInfo" in author and author["AffiliationInfo"]:  # Check if AffiliationInfo exists and is not empty
                    affiliation = author["AffiliationInfo"][0]["Affiliation"]
                    if "pharma" in affiliation.lower() or "biotech" in affiliation.lower():
                        non_academic_authors.append(author.get("LastName", "N/A"))
                        company_affiliations.append(affiliation)
                    # Extract email (heuristic)
                    if "@" in affiliation:
                        corresponding_email = affiliation.split()[-1]

        results.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(company_affiliations),
            "Corresponding Author Email": corresponding_email
        })
    
    return pd.DataFrame(results)
if __name__ == "__main__":
    query = "cancer treatment"  # Example query
    pubmed_ids = search_pubmed(query)
    papers = fetch_paper_details(pubmed_ids)
    df = process_papers(papers)
    print(df)