import re

def extract_sql(input_str):
    # Find all occurrences of ```sql and their corresponding endings
    matches = re.findall('`{3}sql(.*?)`{3}', input_str, flags=re.DOTALL)
    if len(matches) > 1:
        raise Exception('More than one set of SQL statements found in the input string')
    elif len(matches) == 0:
        raise Exception('No SQL statements found in the input string')
    sql_statement = matches[0]

    # Remove any text that appears before the SQL statement
    sql_statement = re.sub(r'^.*?`{3}sql', '`{3}sql', sql_statement, flags=re.DOTALL)

    # Remove any text that appears after the SQL statement
    sql_statement = re.sub(r'`{3}.*$', '`{3}', sql_statement, flags=re.DOTALL)

    return sql_statement