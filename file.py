users=[]
passwords=[]
def importingfile():
    with open("users.txt") as file:
        for line in file:
            users.append(line.split()[0])
            passwords.append(line.split()[1])
    return users,passwords
