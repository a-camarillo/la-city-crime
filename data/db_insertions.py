import psycopg
import data

data = data.cleaned_data()

def insert_data():
    with psycopg.connect("host=localhost port=5432 dbname=la-crime user=postgres password=test", autocommit=True) as conn:
        cur = conn.cursor()
        for item in data:
            print("now inserting data")
            with conn.transaction():
                cur.execute(
                        """
                        INSERT INTO areas (areaCode, areaName)
                        VALUES (%s, %s)
                        ON CONFLICT DO NOTHING
                        """,
                        (item["AREA"], item["AREA NAME"])
                        )
                cur.execute(
                        """
                        INSERT INTO sex (sex)
                        VALUES (%s)
                        ON CONFLICT DO NOTHING
                        """,
                        (item["Vict Sex"],)
                        )
                cur.execute(
                        """
                        INSERT INTO descents (descentShort, descentLong)
                        VALUES (%s, %s)
                        ON CONFLICT DO NOTHING
                        """,
                        (item["Vict Descent"], item["descentLong"])
                        )
                cur.execute(
                        """
                        INSERT INTO crimes (crimeCode, crimeDescription)
                        VALUES (%s, %s)
                        ON CONFLICT DO NOTHING
                        """,
                        (item["Crm Cd"], item["Crm Cd Desc"])
                        )
                cur.execute(
                        """
                        INSERT INTO weapons (weaponCode, weaponDescription)
                        VALUES (%s, %s)
                        ON CONFLICT DO NOTHING
                        """,
                        (item["Weapon Used Cd"], item["Weapon Desc"])
                        )
                cur.execute(
                        """
                        INSERT INTO premises (premiseCode, premiseDescription)
                        VALUES (%s, %s)
                        ON CONFLICT DO NOTHING
                        """,
                        (item["Premis Cd"], item["Premis Desc"])
                        )
                cur.execute(
                        """
                        INSERT INTO locations (address, latitude, longitude, areaCode)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT DO NOTHING
                        """,
                        (item["LOCATION"], item["LAT"], item["LON"], item["AREA"])
                        )
                cur.execute(
                        """
                        INSERT INTO victims (age, sexCode, descentID)
                        VALUES (%s,
                        (SELECT sexCode FROM sex WHERE sex = (%s)),
                        (SELECT descentID FROM descents WHERE descentShort = (%s))
                        )
                        ON CONFLICT DO NOTHING
                        """,
                        (item["Vict Age"], item["Vict Sex"], item["Vict Descent"])
                        )
                cur.execute(
                        """
                        INSERT INTO crimeInfo 
                        (dateReported, dateOccurred, timeOccurred, locationID, victimID, crimeCode, weaponCode, premiseCode)
                        VALUES (
                        %s,
                        %s,
                        %s,
                        (
                        SELECT id FROM locations 
                        WHERE address = %s 
                        AND latitude = %s 
                        AND longitude = %s 
                        AND areaCode = %s
                        LIMIT 1
                        ),
                        (
                        SELECT v.id FROM victims v 
                        INNER JOIN sex s ON v.sexCode = s.sexCode
                        INNER JOIN descents d on v.descentID = d.descentID 
                        WHERE v.age = %s 
                        AND s.sex = %s 
                        AND d.descentShort = %s
                        LIMIT 1
                        ),
                        %s,
                        %s,
                        %s
                        )
                        """,
                        (item["Date Rptd"], item["DATE OCC"], item["TIME OCC"],
                         item["LOCATION"], item["LAT"], item["LON"], item["AREA"],
                         item["Vict Age"], item["Vict Sex"], item["Vict Descent"],
                         item["Crm Cd"], item["Weapon Used Cd"],
                         item["Premis Cd"])
                        )
