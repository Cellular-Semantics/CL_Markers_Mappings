# CL_Markers_Mappings

A repository for mapping gene markers in CL to various external databases such as UniProt.

## Status
STATUS: DRAFT

## Prerequisites

1. **Ensure Python is installed**:
    - If you don't have Python 3 installed, you can download it from [python.org](https://www.python.org/downloads/).
   
2. **Install the required packages:**

    ```sh
    pip install requests
    ```

## Setup and Usage 

1. **Clone the repository**:
   
    ```sh
    git clone https://github.com/Cellular-Semantics/CL_Markers_Mappings
    cd CL_Markers_Mappings
    ```
    

2. **Run the UniProt Mapping Script**:
    ```sh
    python3 uniprot_mapping.py
    ```

    - This script will map gene markers to UniProt IDs for human and mouse, and outputs the information into a CSV file.
    - The CSV file generated is named `uniprot_mapping.csv` in the `CL_Markers_Mappings` directory. The file contains the UniProt IDs and additional information for the specified gene markers.

## Customization

**Modify the Script**: Update the `uniprot_mapping.py` script to include or exclude fields according to your requirements.

```python
# Example: Customize fields
params = {
    "query": query,
    "format": "json",
    "fields": "accession,id,reviewed,protein_name,gene_names,organism_id"  # Customize these fields as needed
}

For a complete list of available fields, refer to the [UniProtKB Return Fields Documentation](https://www.uniprot.org/help/return_fields).

## Example Output

The output CSV file (`uniprot_mapping.csv`) will contain the following columns:

| Marker | Organism | UniProt ID | Entry Name | Reviewed | Protein Names | Genes |
|--------|----------|------------|------------|----------|---------------|-------|
| CX3CR1 | Human    | P49238     | CX3C1_HUMAN| Yes      | CX3C chemokine receptor 1 | CX3CR1 |

