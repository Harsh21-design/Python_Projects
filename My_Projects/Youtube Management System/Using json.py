# YOUTUBE MANAGER APP
import json

def loadData():
    try:
        with open('youtube.txt','r') as file1:
            load = json.load(file1) # (list of videos)
            return load
    except FileNotFoundError:
        return []

def SaveData(videos):
    with open('youtube.txt','w') as file1:
        json.dump(videos,file1)  

def AllData(videos):
    print("*"*5)
    print("Available Youtube Videos are-\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} ({video['time']})")
        # SaveData(videos)

    print("*"*5) 

def AddData(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({'name':name,'time':time})
    print("Video Added Successfuly")
    print("*"*10)
    SaveData(videos)

def UpdateData(videos):
    AllData(videos)
    index = int(input("Enter Video Number to update details: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new name of video: ")
        time = input("Enter the new duration of video: ")
        videos[index-1] = {'name':name,'time':time}
        SaveData(videos)
    else:
        print("Invalid Index Number!!")
    print("Video Updated Successfuly")
    print("*"*10)

def DeleteData(videos):
    AllData(videos)
    index = int(input("Enter Video Number to be Deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        SaveData(videos)
    else:
        print("Invalid Number!!")
    print("Video Deleted Successfuly")
    print("*"*10)


def main():
    videos = loadData()
    while True:
        wel_msg = '''
        "*****  WELCOME TO YOUTUBE MANAGE APP BY HARSH MALVIYA  *****"
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
            match choice:
                case 1:
                    AllData(videos)
                case 2:
                    AddData(videos)
                case 3:
                    UpdateData(videos)
                case 4:
                    DeleteData(videos)
                case 5:
                    print("Thank you for using the Youtube Manager App.")
                    break
                case _:
                    print("Invalid Choice!! Please select a valid option.")

        except ValueError:
            print("Please enter valid number(1-5)")

if __name__ == "__main__":
    main()