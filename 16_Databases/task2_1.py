import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Create table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Get file name input
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'

# Open and process file
with open(fname) as fh:
    for line in fh:
        if not line.startswith('From: '):
            continue

        # Extract email and domain
        email = line.split()[1]  # Get full email
        org = email.split('@')[1]  # Extract domain

        # Check if domain exists in database
        cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
        row = cur.fetchone()

        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

# Commit changes
conn.commit()

# Retrieve top 10 organizations
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close connection
cur.close()
conn.close()

