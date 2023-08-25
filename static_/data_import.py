import pandas as pd

def import_data_to_dataframe(file_path, format=None, **kwargs):
    """
    Import data from a file into a pandas dataframe.

    Parameters:
    - file_path (str): Path to the file to be imported.
    - format (str, optional): Format of the file ('csv', 'excel', 'sql', etc.).
                              If None, the function will try to infer the format.
    - **kwargs: Additional arguments to be passed to the pandas read function.

    Returns:
    - pd.DataFrame: DataFrame with the imported data.
    """

    if format is None:
        # Infer the file type from its extension
        extension = file_path.split('.')[-1].lower()
        if extension == 'csv':
            format = 'csv'
        elif extension in ['xls', 'xlsx']:
            format = 'excel'
        elif extension == 'sql':
            raise ValueError("For SQL, please specify a format and provide a connection string.")
        # Add more formats as needed
        else:
            raise ValueError(f"Unsupported file format: {extension}")

    if format == 'csv':
        return pd.read_csv(file_path, **kwargs)
    elif format == 'excel':
        return pd.read_excel(file_path, **kwargs)
    # For SQL, you'll need to pass a connection as an argument in kwargs
    elif format == 'sql':
        connection = kwargs.pop("connection")
        query = kwargs.pop("query")
        return pd.read_sql(query, connection, **kwargs)
    else:
        raise ValueError(f"Unsupported format specified: {format}")