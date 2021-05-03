import mysql.connector

def convertBinary(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertFile(FULL_NAME, NAME, EXTENSION):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='safe',
                                             user='test',
                                             password='1')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO python_employee
                          (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



    while True:
        print("\n" + "*" * 18)
        print("Choose an Option:")
        print("o = Open a File")
        print("s = Store a File")
        print("q = Quit")
        print("*" * 18)
        input_ = input(":")

        if input_ == "q":
            print("See you soon!")
            break

        if input_ == "o":
            # open the file
            file_type = input("Enter in your file's extension: \n")
            file_name = input("Enter the file's name: \n")
            FILE_ = file_name + "." + file_type

            cursor = conn.execute("SELECT * from SAFE WHERE FULL_NAME=" + '"' + FILE_ + '"')

            file_string = ""
            for row in cursor:
                file_string = row[3]
            with open(FILE_, 'wb') as f_output:
                print(file_string)
                f_output.write(base64.b64decode(file_string))

        if input_ == "s":
            # store file
            PATH = input("Enter in the path of the file to be stored: \nExample: /Users/User/Desktop/file.txt\n")

            FILE_TYPES = {
                "txt": "TEXT",
                "java": "TEXT",
                "dart": "TEXT",
                "py": "TEXT"
            }

            # if input != FILE_TYPES:
            #     print("Unsupported filetype or invalid directory, please try again\n")

            file_name = PATH.split("/")
            file_name = file_name[len(file_name) - 1]
            file_string = ""

            NAME = file_name.split(".")[0]
            EXTENSION = file_name.split(".")[1]

            try:
                EXTENSION = FILE_TYPES[EXTENSION]
            except:
                Exception()

            # if EXTENSION == "IMAGE":
            #     IMAGE = cv2.imread(PATH)
            #     file_string = base64.b64encode(cv2.imencode('.jpg', IMAGE)[1]).decode()

            if EXTENSION == "TEXT":
                file_string = open(PATH, "r").read()
                # file_string = base64.b64encode(file_string)

            EXTENSION = file_name.split(".")[1]

            command = 'INSERT OR IGNORE INTO SAFE (FULL_NAME, NAME, EXTENSION, FILES) VALUES (%s, %s, %s, %s);' % (
                '"' + file_name + '"', '"' + NAME + '"', '"' + EXTENSION + '"', '"' + file_string + '"')

            conn.execute(command)
            conn.commit()

        if input != ('o', 's', 'q'):
            print("Incorrect choice, please try again")
