import requests
import csv

# Define a list of markers
markers = [
    "CX3CR1", "ITGAX", "CLEC7A", "ADGRE1",
    "SIGLEC1", "CD68", "MRC1", "ITGAM"
]

# Organism IDs for human and mouse
organism_ids = {
    "human": "9606",
    "mouse": "10090"
}

# Function to get UniProt ID and additional fields
def get_uniprot_id(gene_name, organism_id, reviewed=True):
    base_url = "https://rest.uniprot.org/uniprotkb/search"
    query = f"gene:{gene_name} AND organism_id:{organism_id}"
    if reviewed:
        query = f"({query}) AND (reviewed:true)"
    else:
        query = f"({query}) AND (reviewed:false)"
    params = {
        "query": query,
        "format": "json",
        "fields": "accession,id,reviewed,protein_name,gene_names,organism_id"
    }
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(base_url, params=params, headers=headers)
    print(f"Request URL: {response.url}")  # Print the URL to verify the request
    if response.status_code == 200:
        return response.json()
    else:
        print(response.json())  # Print the full response for debugging
        return {"error": f"Failed to retrieve data for {gene_name}. Status code: {response.status_code}"}

# Prepare CSV file
csv_file = "uniprot_mapping.csv"
csv_columns = ["Marker", "Organism", "UniProt ID", "Entry Name", "Reviewed", "Protein Names", "Genes"]

# Open CSV file for writing
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()

    # Iterate over the markers and fetch UniProt IDs and additional fields
    for marker in markers:
        for organism_name, organism_id in organism_ids.items():
            print(f"Marker: {marker}, Organism: {organism_name.capitalize()}")
            
            # Fetch reviewed entries
            result = get_uniprot_id(marker, organism_id, reviewed=True)
            if 'results' in result:
                for entry in result['results']:
                    accession = entry.get('primaryAccession', 'N/A')
                    entry_id = entry.get('uniProtkbId', 'N/A')
                    reviewed = 'Yes' if entry.get('entryType', '') == 'UniProtKB reviewed (Swiss-Prot)' else 'No'
                    protein_names = entry.get('proteinDescription', {}).get('recommendedName', {}).get('fullName', {}).get('value', 'N/A')
                    genes = ', '.join(g['geneName']['value'] for g in entry.get('genes', []))
                    writer.writerow({
                        "Marker": marker,
                        "Organism": organism_name.capitalize(),
                        "UniProt ID": accession,
                        "Entry Name": entry_id,
                        "Reviewed": reviewed,
                        "Protein Names": protein_names,
                        "Genes": genes
                    })
            else:
                print(f"Error: {result.get('error', 'Unknown error occurred')}")
            print("-------------")
            
            
            
print(f"Data has been written to {csv_file}")

