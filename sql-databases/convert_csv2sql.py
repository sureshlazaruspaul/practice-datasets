import pandas as pd
from typing import List
import sqlite3
import os

def csv_to_sqlite(filename, table_name=None, db_name=None):
    """
    Convert a CSV file to SQLite database
    
    Args:
        filename (str): Name of the CSV file (with or without .csv extension)
        table_name (str, optional): Name for the table. Defaults to filename without extension
        db_name (str, optional): Name for the database file. Defaults to filename.db
    
    Returns:
        str: Path to the created database file
    """
    
    # Handle filename with or without .csv extension
    if filename.endswith('.csv'):
        csv_file = filename
        base_name = filename[:-4]  # Remove .csv extension
    else:
        csv_file = f'{filename}.csv'
        base_name = filename
    
    # Set default table name if not provided
    if table_name is None:
        table_name = base_name
    
    # Set default database name if not provided
    if db_name is None:
        db_name = f'{base_name}.db'
    
    # Check if CSV file exists
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"CSV file '{csv_file}' not found")
    
    try:
        # Read CSV
        print(f"Reading CSV file: {csv_file}")
        df = pd.read_csv(csv_file)
        print(f"Successfully read {len(df)} rows and {len(df.columns)} columns")
        
        # Create SQLite database
        print(f"Creating SQLite database: {db_name}")
        conn = sqlite3.connect(db_name)
        
        # Convert DataFrame to SQL table
        df.to_sql(table_name, conn, index=False, if_exists='replace')
        
        # Get table info
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]
        
        print(f"Successfully created table '{table_name}' with {row_count} rows")
        
        # Close connection
        conn.close()
        
        print(f"Database created successfully: {db_name}")
        return db_name
        
    except Exception as e:
        print(f"Error: {e}")
        if 'conn' in locals():
            conn.close()
        raise

# Example usage:
if __name__ == "__main__":
    # # Example 1: Basic usage with just filename
    # csv_to_sqlite("credit_risk")
    
    # # Example 2: Custom table name
    # csv_to_sqlite("credit_risk", table_name="credit_data")
    
    # # Example 3: Custom table and database names
    # csv_to_sqlite("credit_risk", table_name="risk_analysis", db_name="financial_data.db")
    
    # # Example 4: With .csv extension in filename
    # csv_to_sqlite("credit_risk.csv")

    filename_list: List[str] = [
        "credit_risk", 
        "criminal_minds", 
        "crisk", 
        "exam_scores",
        "heart_disease_uci",
        "iris",
        "msfhdr",
        "starwars",
        "titanic_manifest",
        "total_population_2010"
    ]

    for filename in filename_list:
        csv_to_sqlite(filename, table_name=filename, db_name=f"{filename}.db")