# YOUTUBE MANAGER APP WITH SQLITE3 DATABASE 

import sqlite3

con = sqlite3.connect('Youtube_Manager.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_all_data():
    print("Available Youtube Videos are -- ")
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print(("# "*20))

def add_data(name, time, video_id):
    
    cursor.execute("INSERT INTO videos(id, name, time) VALUES(?, ?, ?)",(name, time, video_id))
    con.commit()
    print("Video is successfully added...")

def update_data(video_id, newname, newtime):
    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    if cursor.fetchone():
    #   list_all_data()
      cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(newname, newtime, video_id))
      con.commit()
      print("video is successfully updated...")
    else:
        print("Invalid  video ID!!")
    
def delete_data(video_id):
    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    # list_all_data()
    if cursor.fetchone():
      cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
      con.commit()
      print("video is successfully deleted...")
    else:
        print("Invalid  video ID!!")

def main():
    while True:
        wel_msg = '''
        *****  WELCOME TO YOUTUBE MANAGE APP BY HARSH MALVIYA  *****
        
        CHOOSE AN OPTION - 
        
        1. LIST DOWN ALL THE YOUTUBE VIDEOS
        2. ADD A YOUTUBE VIDEO DETAIL
        3. UPDATE A YOUTUBE VIDEO DETAIL
        4. DELETE A YOUTUBE VIDEO
        5. EXIT THE APP
        '''
        print(wel_msg)
        # print("\n")
        try:
            choice = int(input("Enter Your prefer choice: "))
            print("\n")
            if choice == 1:
                list_all_data()
            elif choice == 2:
                print("Adding a new video details....")
                video_id = int(input("Enter video id to add: "))
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_data(video_id,name,time)
            elif choice == 3:
                print("Updating a video details....")
                video_id = int(input("Enter video id to update: "))
                name = input("Enter video new name: ")
                time = input("Enter video  new time: ")
                update_data(video_id,name,time)
            elif choice == 4:
                print("Deleting a video...")
                video_id = int(input("Enter video id to delete: "))
                delete_data(video_id)
            elif choice == 5:
                print("Thank for Using...")
                break
            else:
                print("Invalid Choice!!")
        

        except ValueError:
            print("Please enter valid number(1-5)")

    con.close()

if __name__ == "__main__":
    main()

# cursor.fetchone() → gets one row
# cursor.fetchall() → gets all rows