import psycopg2
from fastapi import FastAPI, File, UploadFile


app = FastAPI()


def get_db_connection():
    try:
        conn = psycopg2.connect("dbname=postgres user=postgres host=localhost password=1234 port=5432")  # Connecting to PostgreSQL 
        return conn
    except Exception as e:
        print("Error: ", e)


@app.get("/retrieve/{file}")
def retrieve_file(file: str):
    conn = None
    cur = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()  # Creating a cursor to interact with the database
        cur.execute("SELECT file_name, content, media_type FROM files WHERE file_name = %s", (file,))  # Retrieving the file from the database
        file_record = cur.fetchone()
        if file_record:
            return {
                "file_name": file_record[0],
                "file_content": file_record[1].tobytes().decode('utf-8'),  # Converting Memory object to binary and then to string
                "media_type": file_record[2]
            }
        else:
            return {"message": "The requested file name was not found"}
    except:
        return {"message": "An error occurred during file retrieval"}
    finally:
        if cur is not None:
            cur.close()  # Closing cursor
        if conn is not None:
            conn.close()  # Closing connection
    
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)): 
    conn = None
    cur = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        file_content = await file.read()  # Reading the file content
        cur.execute("INSERT INTO files (file_name, content, media_type) VALUES (%s, %s, %s)", (file.filename, file_content, file.content_type))
        conn.commit()  # Adding the file to the database
        return {"message": f"Successfully uploaded {file.filename}"}
    except Exception as e:
        return {"message": "An error occurred during file upload"}
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

@app.delete("/delete_file/{file}")
def delete_file(file: str):
    conn = None
    cur = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT file_name FROM files WHERE file_name = %s", (file,))
        if not cur.fetchone():
            return {"message": "The requested file name was not found"}
        cur.execute("DELETE FROM files WHERE file_name = %s", (file,))
        conn.commit()
        return {"message": "Operation complete"}
    except:
        return {"message": "An error occurded during file deletion"}
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()