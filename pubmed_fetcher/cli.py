import argparse
from pubmed_fetcher.main import search_pubmed, fetch_paper_details, process_papers

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    args = parser.parse_args()

    # Fetch papers
    pubmed_ids = search_pubmed(args.query)
    papers = fetch_paper_details(pubmed_ids)
    df = process_papers(papers)

    # Save or print results
    if args.file:
        df.to_csv(args.file, index=False)
        print(f"Results saved to {args.file}")
    else:
        print(df.to_csv(index=False))

if __name__ == "__main__":
    main()