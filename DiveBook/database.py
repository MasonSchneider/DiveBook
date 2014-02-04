import urlparse
import psycopg2
import os

class Database:

    def __init__(self):
        urlparse.uses_netloc.append("postgres")
        url = urlparse.urlparse(os.environ["DATABASE_URL"])

        self.conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        self.cursor = self.conn.cursor()

    # DIVERS ------------------------------------------------------------------------

    def getDivers(self):
        self.cursor.execute("SELECT Divers.id, fName, lName, name FROM Divers, Profiles, Schools WHERE Divers.id = Profiles.diverID AND Profiles.schoolID = Schools.id;")
        return self.cursor.fetchall()

    def getDiverProfile(self, diverid):
        # TODO: pull meets
        self.cursor.execute("SELECT email, fName, lName, age, favoriteDive FROM Divers JOIN Profiles ON id = diverID WHERE id = %s;",[diverid])
        return self.cursor.fetchall()

    def searchDivers(self, fname, lname, school):
    	# TODO: fix search
    	self.cursor.execute("SELECT diverID, fName, lName, name FROM Profiles, Schools WHERE Profiles.schoolID=Schools.id AND (Profiles.fName LIKE %s OR Profiles.lName LIKE %s OR Schools.name LIKE %s);",[fname,lname,school])
    	return self.cursor.fetchall()

    # -------------------------------------------------------------------------------

    # DIVESHEETS --------------------------------------------------------------------

    def getDiveSheets(self, diverid):
        self.cursor.execute("SELECT * FROM DiveSheets WHERE diverID=%s;",[diverid])
        return self.cursor.fetchall()


    # -------------------------------------------------------------------------------

    # DIVES ------------------------------------------------------------------------

    def getDD(self, name, height, position):
    	self.cursor.execute("SELECT dd, number FROM Dives WHERE name=%s AND height=%s AND position=%s;",[name, height, position])
    	dd = self.cursor.fetchall()
    	if len(dd) > 0:
    		return dd[0]
    	return ['NOT FOUND', '000']

    def getDives(self):
        self.cursor.execute("SELECT * FROM Dives;")
        return self.cursor.fetchall()

    # -------------------------------------------------------------------------------

    # MEETS --------------------------------------------------------------------------

    def getUpcomingMeets(self):
        self.cursor.execute("SELECT id, title, state, date FROM Meets WHERE date > CURRENT_DATE;")
        return self.cursor.fetchall()

    def getPastMeets(self):
        self.cursor.execute("SELECT id, title, state, date FROM Meets WHERE date < CURRENT_DATE;")
        return self.cursor.fetchall()

    # --------------------------------------------------------------------------------

    # Account requests ---------------------------------------------------------------

    def login(self, email, password):
    	self.cursor.execute("SELECT id FROM Divers \
    						WHERE email=%s AND hashpass=%s;",[email,password])
    	return self.cursor.fetchall()

    def register(self, email, password):
    	self.cursor.execute("SELECT id FROM Divers WHERE email=%s;",[email])
    	registered =  self.cursor.fetchall()
    	if len(registered) > 0:
    		return False
    	else:
    		self.cursor.execute("INSERT INTO Divers (email, hashpass) VALUES (%s, %s);",[email, password])
    		return True

   	# --------------------------------------------------------------------------------