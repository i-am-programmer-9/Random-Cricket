import random
team1 = input("Enter The First Team: ")
team2 = input("Enter The Second Team: ")

team_name = False
#Checking if Team 1 or Team 2 Input equals to Csk
if team1.upper() == 'CSK' or team2.upper() == 'CSK':
    if(team1.upper() == 'CSK'):
        squad_of_team_1 = ['MS Dhoni(c)(wk)', 'Faf Du Plesis', 'Shane Watson', 'Ambati Raydu', 'Ravindra Jadeja', 'Dwane Bravo', 'Sam Currun'
        , 'Deepak Chahar', 'Shardul Thakur','Karn Sharma', 'Piyush Chawla', 'KM Asif', 'Imran Tahir', 'Kedar Jadhav', 'Lungi Ngidi', 
        'Mitchell Sentener', 'Monu Singh', 'Murli Vijay', 'Ruturaj Gaikwad', 'Josh Hezalwood', 'R Shai Kishore']
    if(team2.upper() == 'CSK'):
        squad_of_team_2 = ['MS Dhoni(c)(wk)', 'Faf Du Plesis', 'Shane Watson', 'Ambati Raydu', 'Ravindra Jadeja', 'Dwane Bravo', 'Sam Currun'
        , 'Deepak Chahar', 'Shardul Thakur','Karn Sharma', 'Piyush Chawla', 'KM Asif', 'Imran Tahir', 'Kedar Jadhav', 'Lungi Ngidi', 
        'Mitchell Sentener', 'Monu Singh', 'Murli Vijay', 'Ruturaj Gaikwad', 'Josh Hezalwood', 'R Shai Kishore']

#Checking if Team 1 or Team 2 Input equals to Mi
if team1.upper() == 'MI' or team2.upper() == 'MI':
    if(team1.upper() == 'MI'):
        squad_of_team_1 = ['Rohit Sharma(c)', 'Quinton De Cock', 'Suryakumar Yadav', 'Ishan Kishan', 'Krunal Pandya', 'Hardik Pandya'
        , 'Kieron Pollard', 'Aditya Tare', 'Anmolpreet Singh','Ankul Roy', 'Dhawal Kulkarni', 'Jayant Yadav', 'Mitchell Mclleghan', 
        'Rahul Chahar','Surfane RutherFord', 'Trent Boult', 'Chrish Lynn', 'Digvijay Deshmukh', 'Mosing Khan', 'Nathan Kultar Nile',
        'Prince Balwant Rai Singh', 'Saurbh Tiwari', 'James Pattinson', 'Jaspreet Bumrah']
    if(team2.upper() == 'MI'):
        squad_of_team_2 = ['Rohit Sharma(c)', 'Quinton De Cock', 'Suryakumar Yadav', 'Ishan Kishan', 'Krunal Pandya', 'Hardik Pandya'
        , 'Kieron Pollard', 'Aditya Tare', 'Anmolpreet Singh','Ankul Roy', 'Dhawal Kulkarni', 'Jayant Yadav', 'Mitchell Mclleghan', 
        'Rahul Chahar','Surfane RutherFord', 'Trent Boult', 'Chrish Lynn', 'Digvijay Deshmukh', 'Mosing Khan', 'Nathan Kultar Nile',
        'Prince Balwant Rai Singh', 'Saurbh Tiwari', 'James Pattinson', 'Jaspreet Bumrah']
    team_name = True

#Checking if Team 1 or Team 2 Input equals to RCB
if team1.upper() == 'RCB' or team2.upper() == 'RCB':
    if(team1.upper() == 'RCB'):
        squad_of_team_1 = ['Virat Kohli(c)', 'AB de Villiers', 'Devdutt Padikkal', 'Gurkeerat Singh', 'Moeen Ali', 'Mohammed Siraj', 
        'Navdeep Saini', 'Parthiv Patel', 'Pawan Negi', 'Shivam Dube', 'Umesh Yadav', 'Washington Sundar', 'Yuzvendra Chahal', 'Aaron Finch',
        'Chris Morris', 'Dale Steyn', 'Isuru Udana', 'Joshua Philippe', 'Pavan Deshpande', 'Shahbaz Ahamad', 'Adam Zampa']
    if(team2.upper() == 'RCB'):
        squad_of_team_2 = ['Virat Kohli(c)', 'AB de Villiers', 'Devdutt Padikkal', 'Gurkeerat Singh', 'Moeen Ali', 'Mohammed Siraj', 
        'Navdeep Saini', 'Parthiv Patel', 'Pawan Negi', 'Shivam Dube', 'Umesh Yadav', 'Washington Sundar', 'Yuzvendra Chahal', 'Aaron Finch',
        'Chris Morris', 'Dale Steyn', 'Isuru Udana', 'Joshua Philippe', 'Pavan Deshpande', 'Shahbaz Ahamad', 'Adam Zampa']
        team_name = True

#Checking if Team 1 or Team 2 Input equals to KXIP
if team1.upper() == 'KXIP' or team2.upper() == 'KXIP':
    if(team1.upper() == 'KXIP'):
        squad_of_team_1 = ['KL Rahul(c)', 'Arshdeep Singh', 'Chris Gayle', 'Darshan Nalkande', 'Krishnappa Gowtham', 'Hardus Viljoen',
        'Harpreet Brar', 'Jagadeesha Suchith', 'Karun Nair', 'Mandeep Singh', 'Mayank Agarwal', 'Mohammed Shami', 'Mujeeb Ur Rahman', 
        'Murugan Ashwin', 'Nicholas Pooran', 'Sarfaraz Khan', 'Chris Jordan', 'Deepak Hooda', 'Glenn Maxwell', 'Ishan Porel', 'James Neesham', 
        'Prabhsimran Singh', 'Ravi Bishnoi', 'Sheldon Cottrell', 'Tajinder Dhillon']
    if(team2.upper() == 'KXIP'):
        squad_of_team_2 = ['KL Rahul(c)', 'Arshdeep Singh', 'Chris Gayle', 'Darshan Nalkande', 'Krishnappa Gowtham', 'Hardus Viljoen',
        'Harpreet Brar', 'Jagadeesha Suchith', 'Karun Nair', 'Mandeep Singh', 'Mayank Agarwal', 'Mohammed Shami', 'Mujeeb Ur Rahman', 
        'Murugan Ashwin', 'Nicholas Pooran', 'Sarfaraz Khan', 'Chris Jordan', 'Deepak Hooda', 'Glenn Maxwell', 'Ishan Porel', 'James Neesham', 
        'Prabhsimran Singh', 'Ravi Bishnoi', 'Sheldon Cottrell', 'Tajinder Dhillon']
        team_name = True

#Checking if Team 1 or Team 2 Input equals to KKR
if team1.upper() == 'KKR' or team2.upper() == 'KKR':
    if(team1.upper() == 'KKR'):
        squad_of_team_1 = ['Dinesh Karthik (c)', 'Andre Russell', 'Kamlesh Nagarkoti', 'Kuldeep Yadav', 'Lockie Ferguson', 'Nitish Rana', 'Prasidh Krishna', 'Rinku Singh', 'Sandeep Warrier', 'Shivam Mavi', 'Shubman Gill', 'Siddhesh Lad', 'Sunil Narine', 'Chris Green', 'Eoin Morgan', 'M Siddharth', 'Nikhil Naik', 'Pat Cummins', 'Rahul Tripathi', 'Tom Banton', 'Varun Chakravarthy']
    if(team2.upper() == 'KKR'):
        squad_of_team_2 = ['KL Rahul(c)', 'Arshdeep Singh', 'Chris Gayle', 'Darshan Nalkande', 'Krishnappa Gowtham', 'Hardus Viljoen',
        'Harpreet Brar', 'Jagadeesha Suchith', 'Karun Nair', 'Mandeep Singh', 'Mayank Agarwal', 'Mohammed Shami', 'Mujeeb Ur Rahman', 
        'Murugan Ashwin', 'Nicholas Pooran', 'Sarfaraz Khan', 'Chris Jordan', 'Deepak Hooda', 'Glenn Maxwell', 'Ishan Porel', 'James Neesham', 
        'Prabhsimran Singh', 'Ravi Bishnoi', 'Sheldon Cottrell', 'Tajinder Dhillon']
    team_name = True

#Checking if Team 1 or Team 2 Input equals to SRH
if team1.upper() == 'SRH' or team2.upper() == 'SRH':
    if(team1.upper() == 'SRH'):
        squad_of_team_1 = ['David Warner(c)', 'Abhishek Sharma', 'Basil Thampi', 'Bhuvneshwar Kumar', 'Billy Stanlake', 'Jonny Bairstow', 'Kane Williamson', 'Manish Pandey', 'Mohammad Nabi', 'Rashid Khan', 'Sandeep Sharma', 'Shahbaz Nadeem', 'Shreevats Goswami', 'Siddarth Kaul', 'Khaleel Ahmed', 'T Natarajan', 'Vijay Shankar', 'Wriddhiman Saha', 'Abdul Samad', 'Fabian Allen', 'Mitchell Marsh', 'Priyam Garg', 'Sandeep Bavanaka', 'Sanjay Yadav', 'Virat Singh']
    if(team2.upper() == 'SRH'):
        squad_of_team_2 = ['David Warner(c)', 'Abhishek Sharma', 'Basil Thampi', 'Bhuvneshwar Kumar', 'Billy Stanlake', 'Jonny Bairstow', 'Kane Williamson', 'Manish Pandey', 'Mohammad Nabi', 'Rashid Khan', 'Sandeep Sharma', 'Shahbaz Nadeem', 'Shreevats Goswami', 'Siddarth Kaul', 'Khaleel Ahmed', 'T Natarajan', 'Vijay Shankar', 'Wriddhiman Saha', 'Abdul Samad', 'Fabian Allen', 'Mitchell Marsh', 'Priyam Garg', 'Sandeep Bavanaka', 'Sanjay Yadav', 'Virat Singh']
    team_name = True

#Checking if Team 1 or Team 2 Input equals to RR
if team1.upper() == 'RR' or team2.upper() == 'RR':
    if(team1.upper() == 'RR'):
        squad_of_team_1 = ['Steve Smith(c)', 'Ankit Rajpoot', 'Ben Stokes', 'Jofra Archer', 'Jos Buttler', 'Mahipal Lomror', 'Manan Vohra', 
        'Mayank Markande', 'Rahul Tewatia', 'Riyan Parag', 'Sanju Samson', 'Shashank Singh', 'Shreyas Gopal', 'Varun Aaron', 'Akash Singh', 
        'Anirudha Joshi', 'Anuj Rawat', 'Andrew Tye', 'David Miller', 'Jaydev Unadkat', 'Kartik Tyagi', 'Oshane Thomas', 'Robin Uthappa',
        'Tom Curran', 'Yashasvi Jaiswal']
    if(team2.upper() == 'RR'):
        squad_of_team_2 = ['Steve Smith(c)', 'Ankit Rajpoot', 'Ben Stokes', 'Jofra Archer', 'Jos Buttler', 'Mahipal Lomror', 'Manan Vohra', 
        'Mayank Markande', 'Rahul Tewatia', 'Riyan Parag', 'Sanju Samson', 'Shashank Singh', 'Shreyas Gopal', 'Varun Aaron', 'Akash Singh', 
        'Anirudha Joshi', 'Anuj Rawat', 'Andrew Tye', 'David Miller', 'Jaydev Unadkat', 'Kartik Tyagi', 'Oshane Thomas', 'Robin Uthappa',
        'Tom Curran', 'Yashasvi Jaiswal']
    team_name = True

#Checking if Team 1 or Team 2 Input equals to DC
if team1.upper() == 'DC' or team2.upper() == 'DC':
    if(team1.upper() == 'DC'):
        squad_of_team_1 = ['Shreyas Iyer(c)', 'Ajinkya Rahane', 'Amit Mishra', 'Avesh Khan', 'Axar Patel', 'Harshal Patel', 'Ishant Sharma', 
        'Kagiso Rabada', 'Keemo Paul', 'Prithvi Shaw', 'R Ashwin', 'Rishabh Pant', 'Sandeep Lamichhane', 'Shikhar Dhawan', 'Alex Carey', 
        'Lalit Yadav', 'Marcus Stoinis', 'Mohit Sharma', 'Shimron Hetmyer', 'Tushar Deshpande', 'Daniels Sams', 'Anrich Nortje']
    if(team2.upper() == 'DC'):
        squad_of_team_2 = ['Shreyas Iyer(c)', 'Ajinkya Rahane', 'Amit Mishra', 'Avesh Khan', 'Axar Patel', 'Harshal Patel', 'Ishant Sharma', 
        'Kagiso Rabada', 'Keemo Paul', 'Prithvi Shaw', 'R Ashwin', 'Rishabh Pant', 'Sandeep Lamichhane', 'Shikhar Dhawan', 'Alex Carey', 
        'Lalit Yadav', 'Marcus Stoinis', 'Mohit Sharma', 'Shimron Hetmyer', 'Tushar Deshpande', 'Daniels Sams', 'Anrich Nortje']
    team_name = True
if team_name == False:
    print("Wrong Team")
    quit()

random_squad_for_1 = set({})
random_squad_for_2 = set({})
for i in range(1, 11):
    random_squad_for_1.add(random.randint(1, len(squad_of_team_1)))
    random_squad_for_2.add(random.randint(1, len(squad_of_team_2)))

while len(random_squad_for_1) < 11:
    random_squad_for_1.add(random.randint(1, len(squad_of_team_1)))

while len(random_squad_for_2) < 11:
    random_squad_for_2.add(random.randint(1, len(squad_of_team_2)))

print(f"{team1} is throwing the toss")

choice = ['Heads', 'Tails']
team_2_sayed = random.randint(0, 1)
team_2_sayed = choice[team_2_sayed]

print(f"{team2} Says {team_2_sayed}")
coin_value = random.randint(0, 1)
coin_value = choice[coin_value]

if team_2_sayed == coin_value:
    bat_or_bowl = ['Bat', 'Bowl']
    team_want_to_choose = random.randint(0, 1)
    print(f"{team2} Won the toss and elected to {bat_or_bowl[team_want_to_choose]}")
else:
    bat_or_bowl = ['Bat', 'Bowl']
    team_want_to_choose = random.randint(0, 1)
    print(f"{team2} Won the toss and elected to {bat_or_bowl[team_want_to_choose]}")

print("\nSquads:- \n")

#Printing Squad 1
print(f"{team1} Squad:- ")
random_squad_team_1 = []
#printing Captain
for j in random_squad_for_1:
    random_squad_team_1.append(j)
print("1. " + squad_of_team_1[0])
for i in range(0, 10):
    num = random_squad_team_1[i]
    print(f"{i + 2}. {squad_of_team_1[num]}")

#Printing Squad 2
print("\n")
print(f"{team2} Squad:- ")
random_squad_team_2 = []
#printing Captain
for j in random_squad_for_2:
    random_squad_team_2.append(j)
print("1. " + squad_of_team_2[0])
for i in range(0, 10):
    num = random_squad_team_2[i]
    print(f"{i + 2}. {squad_of_team_2[num]}")