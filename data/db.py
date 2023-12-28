import psycopg

def create_tables():
    with psycopg.connect("host=localhost port=5432 dbname=la-crime user=postgres password=test") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS areas (
                areaCode int PRIMARY KEY,
                areaName varchar(50),
                UNIQUE (areaCode, areaName) 
            );
            CREATE TABLE IF NOT EXISTS sex (
                sexCode serial PRIMARY KEY,
                sex char(1),
                UNIQUE (sex) 
            );
            CREATE TABLE IF NOT EXISTS descents (
                descentID serial PRIMARY KEY,
                descentShort char(1),
                descentLong varchar(50),
                UNIQUE (descentShort, descentLong) 
            );
            CREATE TABLE IF NOT EXISTS crimes (
                crimeCode int PRIMARY KEY,
                crimeDescription varchar(100),
                UNIQUE (crimeCode, crimeDescription) 
            );
            CREATE TABLE IF NOT EXISTS weapons (
                weaponCode int PRIMARY KEY,
                weaponDescription varchar(50),
                UNIQUE (weaponCode, weaponDescription) 
            );
            CREATE TABLE IF NOT EXISTS premises (
                premiseCode int PRIMARY KEY,
                premiseDescription varchar(100),
                UNIQUE (premiseCode, premiseDescription) 
            );
            CREATE TABLE IF NOT EXISTS locations (
                id serial PRIMARY KEY,
                address varchar(50),
                latitude real,
                longitude real,
                areaCode int references areas(areaCode) 
            );
            CREATE
            TABLE IF NOT EXISTS victims (
                id serial PRIMARY KEY,
                age int,
                sexCode int references sex(sexCode),
                descentID int references descents(descentID) 
            );
            CREATE TABLE IF NOT EXISTS crimeInfo (
                id serial PRIMARY KEY,
                dateReported date,
                dateOccurred date,
                timeOccurred time,
                locationID int references locations(id),
                victimID int references victims(id),
                crimeCode int references crimes(crimeCode),
                weaponCode int references weapons(weaponCode),
                premiseCode int references premises(premiseCode)
            );
        """)
        conn.commit()
        conn.close()
