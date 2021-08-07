import requests



usr_path = str(input("nom du dossier\n"))
username_firstname = str(input("nom du client\n"))
username_lastname = str(input("prénom du client\n"))

nbr_profil = int(input("entrez le nom de profil à chercher 0 - 10000\n"))
while nbr_profil < 0 or nbr_profil > 10000:
    nbr_profil = int(input("entrez le nombre de profil à chercher 0 - 10000\n"))

i = 0

profile_lst = list()
private_lst = list()

def find_profile(nbr_profil, i, profile_lst, private_lst, username):
    while (i <= nbr_profil):
        if i != 0:
            r = requests.get("https://facebook.com/"+username+str(i))
        else:
            r = requests.get("https://facebook.com/"+username)
        if r.status_code != 404:
            profile_lst += [username+str(i)]
        if r.status_code == 302:
            private_lst += [username+str(i)]
            print(username+str(i))
        i += 1

user1 = username_firstname + username_lastname
user2 = username_lastname + username_firstname


find_profile(nbr_profil, i, profile_lst, private_lst, user1)
print("user1 ok")
j = 0

f = usr_path + '/'+user1+'.txt'
r = open(f, 'w')

for i in profile_lst:
    r.write(f'{i}\n')
r.close()

find_profile(nbr_profil, j, profile_lst, private_lst, user2)
print("user2 ok")

f = usr_path + '/'+user2+'.txt'
r = open(f, 'w')
for i in profile_lst:
    r.write(f'{i}\n')
r.close()

print (profile_lst, private_lst)

