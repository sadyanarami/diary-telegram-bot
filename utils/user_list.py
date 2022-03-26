from ntpath import join


joinedFile = open('user_list.txt', 'r')

joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()