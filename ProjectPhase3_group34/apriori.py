import sqlite3

conn = sqlite3.connect('/Users/shreyasakpal/Desktop/spotify.sqlite')
print('Connected!!')
cur = conn.cursor()
min_support = 5

# Generate L1
cur.execute(f"DROP TABLE IF EXISTS l1;")

cur.execute(f"""
    CREATE TABLE L1 AS
    SELECT artist_id as artist1, album_name, count(*) as count
    FROM artist_album_collaboration
    WHERE popularity > 50
    GROUP BY artist
    HAVING COUNT(*) >{min_support};
""")
conn.commit()
cur.execute(f'SELECT COUNT(*) FROM L1;')
count = cur.fetchone()[0]
print(f"L1: {count} frequent itemsets")

# Generate subsequent levels of the lattice
n = 2

while True:
    cur.execute(f"DROP TABLE IF EXISTS l{n};")
    curr_level = f"l{n}"
    current_query = f"CREATE TABLE {curr_level} AS SELECT "
    for i in range(1, n + 1):
        current_query += f" aac{i}.artist_id AS artist{i},"
    current_query += f" aac1.album_name, COUNT(*) AS count FROM "
    for i in range(0, n):
        if i == 0:
            current_query += f" artist_album_collaboration AS aac{i + 1} JOIN"
        else:
            current_query += f" artist_album_collaboration AS aac{i + 1} ON aac{i}.album_id = aac{i + 1}.album_id AND artist{i} < artist{i + 1} AND aac{i}.popularity > 50 and aac{i+1}.popularity > 50"
            if i != n - 1:
                current_query += f" JOIN"
    current_query += f" GROUP BY "
    for i in range(1, n + 1):
        if i != n:
            current_query += f"artist{i},"
        else:
            current_query += f"artist{i}"
    current_query += f" HAVING count(*) > {min_support};"

    cur.execute(current_query)
    conn.commit()

    # Print the number of frequent itemsets in each level of the lattice
    cur.execute(f"SELECT COUNT(*) FROM L{i};")
    count = cur.fetchone()[0]
    print(f"L{i}: {count} frequent itemsets")

    # Stop if the current query returns an empty table
    if count == 0:
        break
    n += 1

# Close the database connection
cur.close()
conn.close()
