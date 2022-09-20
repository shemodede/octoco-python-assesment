import sqlite3, argparse, hashlib, bcrypt

# Create and parse the necessary commandline arguments
args_parser = argparse.ArgumentParser()
args_parser.add_argument('-i', '--filename', help='Input string.', action='store', type=str, dest='filename', nargs='*')
args_parser.add_argument('-r', '--rounds', help='Number of rounds to encrypt by.', action='store', type=int, dest='rounds', default=18, nargs='*', required=False)
args_parser.add_argument('-d', '--db_file', help='Name of data file.', action='store', type=str, dest='db_file', default="bcrypt", nargs='*', required=False)
args = args_parser.parse_args()

# Fetch and store parsed CL arguments in variables for use
input_string = " ".join(args.filename)
rounds = args.rounds[0]
db_filename = " ".join(args.db_file)

# Store full datafile name in variable
db_full_name = db_filename + ".cache"

# Create datatable if it does not already exist
def create_db_table():
    conn = sqlite3.connect(db_full_name)
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS ENCRYPTION_DATA_TABLE
        (
            ID INTEGER PRIMARY KEY NOT NULL,
            HASHED_INPUT_STRING TEXT NOT NULL,
            ROUNDS INT NOT NULL,
            ENCRYPTED_STRING_OUTPUT TEXT NOT NULL
        );
        ''')
    except sqlite3.OperationalError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        conn.close()

# Check if input string has already been stored in cache
def check_if_input_data_is_cached(input_hash_string, rounds):
    existing_entry = False
    encrypted_value = None
    cursor = None
    conn = sqlite3.connect(db_full_name)
    try:
        cursor = conn.execute('''SELECT * FROM
        ENCRYPTION_DATA_TABLE WHERE HASHED_INPUT_STRING = '%s' AND ROUNDS = '%s' ;
        '''%(input_hash_string, rounds))
    except sqlite3.OperationalError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        rows = cursor.fetchone()
        if rows is None:
            existing_entry = False
        elif len(rows) > 0:
            existing_entry = True
            encrypted_value = rows[3]
        conn.close()
    
    return existing_entry, encrypted_value

# Insert hashed value data into database/cache as required
def insert_db_table_data(input_hash_string, rounds, encrypted_output_string):
    conn = sqlite3.connect(db_full_name)
    try:
        conn.execute('''INSERT INTO ENCRYPTION_DATA_TABLE
        (HASHED_INPUT_STRING, ROUNDS, ENCRYPTED_STRING_OUTPUT) VALUES
        ('%s', '%s', '%s');
        '''%(input_hash_string, rounds, encrypted_output_string))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        conn.close()

# Encrypt the plain input string with bcrypy as required
def encrypt_hashed_input_string():
    salt = bcrypt.gensalt(rounds=rounds)
    encrypted_hash_string = bcrypt.hashpw(input_string.encode('utf-8'), salt)
    return encrypted_hash_string

# Hash input string using hashlib (md5)
def hash_input_string():
    hashed_input_string = hashlib.md5(input_string.encode('utf-8')).hexdigest()
    return hashed_input_string

# store hashed input string in variable
hashed_input_data = hash_input_string()

# Call to function for creation of DB table
create_db_table()

# Call to function to check if input string has already been encrypted, 
# if `entry_exists` is True, `encrypted_value` should contain the hashed/encrypted value stored in cache
entry_exists, encrypted_value = check_if_input_data_is_cached(hashed_input_data, rounds)
new_encrypted_string = None
if not entry_exists:
    # Generate new hashed value for input string
    new_encrypted_string = encrypt_hashed_input_string()
    # Store new hashed value in cache
    insert_db_table_data(hashed_input_data, rounds, hashlib.md5(new_encrypted_string).hexdigest())
    # Print new generated hash value
    print(new_encrypted_string)
else:
    # Print existing hash value from cache
    print(encrypted_value)
