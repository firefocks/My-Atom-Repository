import random

a_surv = {"infantry": 0, "artillery": 0, "tanks": 0, "fighters": 0, "bombers": 0}
d_surv = {"infantry and artillery": 0, "tanks": 0, "fighters": 0, "bombers": 0, "AA guns": 0}
#d_surv = dict()
#d_survivors = list()
#survivors = ['Infantry', 'Artillery', 'Tanks', 'Fighters', 'Bombers']

attackers = int(input("Enter number of infantry attackers: "))
artillery = int(input("Enter number of artillery attackers: "))
a_tanks = int(input("Enter number of attacker tanks: "))
a_fighter = int(input("Enter number of attacker fighters: "))
a_bomber = int(input("Enter number of attacker bombers: "))

defenders = int(input("Enter number of infantry and artillery defenders: "))
d_tanks = int(input("Enter number of defender tanks: "))
d_fighter = int(input("Enter number of defender fighters: "))
d_bomber = int(input("Enter number of defender bombers: "))
aaguns = int(input("Enter number of AA guns: "))

iterations = int(input("How many iterations would you like? "))

a_win = 0
d_win = 0
draw = 0

for i in range(iterations):
    # Calculate number of weapon types
    if attackers - artillery < 0 : inf_a = 0
    else : inf_a = attackers-artillery
    #print("Attacker infantry",inf_a)
    if inf_a > 0 : art_a = 2*artillery
    else : art_a = artillery + attackers
    #print("Attacker Artillery and buffed infantry",art_a)

    tanks_a = a_tanks
    fighter_a = a_fighter
    bomb_a = a_bomber
    attacker_num = inf_a + art_a + tanks_a + fighter_a + bomb_a
    #print("Number of attackers:", attacker_num)

    inf_d = defenders
    tanks_d = d_tanks
    fighter_d = d_fighter
    bomb_d = d_bomber
    aa = aaguns
    round = 0
    defender_num = inf_d + tanks_d + fighter_d + bomb_d + aa
    #print("Number of defenders:", defender_num)

    while attacker_num > 0 and defender_num > 0 :
        a_hit = 0
        d_hit = 0
        aa_hit = 0


        air_units = fighter_a + bomb_a
        if air_units == 0 :
            aa_range = 0
        elif air_units <= int(3*aa) :
            aa_range = air_units
        else :
            aa_range = int(3*aa)

        # AA attacks first

        if round == 0 :
            #print("Round:", round)
#            print("Attacking fighters:", fighter_a)
#            print("Attacking bombers:", bomb_a)
#            print("AA gun fires once!")
            for i in range(aa_range) :
                roll_aa = random.randint(1,6)
#                print("AA gun round", i+1, "Roll", roll_aa)
                if roll_aa <= 1 :
#                    print("AA gun hit!")
                    aa_hit = aa_hit + 1
                    if fighter_a - aa_hit > 0 :
                        fighter_a = fighter_a - aa_hit
#                        print("Fighter down! Remaining fighters:", fighter_a)
                    elif bomb_a + fighter_a - aa_hit > 0 :
                        bomb_a = bomb_a + fighter_a - aa_hit
                        fighter_a = 0
#                        print("Bomber down! Remaining bombers:", bomb_a)
                    else :
                        bomb_a = 0
                        fighter_a = 0
#                        print("All aircraft destroyed!")
            round = round + 1
                #print("AA gun hit! Fighters left:", fighter_a)
        #print("Air attacker count", fighter_a, "fighters and", bomb_a, "bombers")
        # Infantry hits
        for i in range(inf_a) :
            roll_a = random.randint(1,6)
            if roll_a <= 1 :
                #print("Attacker scores a hit!", roll_a)
                a_hit = a_hit + 1
            #else : print("Attacker misses!")
        # Artillery + buffed infantry hits
        for i in range(int(art_a)) :
            roll_art = random.randint(1,6)
            if roll_art <= 2 :
                #print("Artillery scores a hit!", roll_art)
                a_hit = a_hit + 1
            #else : print("Artillery misses!")
        for i in range(tanks_a) :
            roll_tank = random.randint(1,6)
            if roll_tank <= 3 :
                a_hit = a_hit + 1
        for i in range(fighter_a) :
            roll_fight = random.randint(1,6)
            #print("Fighter round", i+1, "Roll", roll_fight)
            if roll_fight <= 3 :
                a_hit = a_hit + 1
        for i in range(bomb_a) :
            roll_bomb = random.randint(1,6)
            #print("Bomber", i+1, "Roll", roll_bomb)
            if roll_bomb <= 4 :
                a_hit = a_hit + 1
        #print("Attacker hits:", a_hit)

        # Defender Infantry hits
        for i in range(inf_d) :
            roll_d = random.randint(1,6)
            if roll_d <= 2 :
                #print("Defender scores a hit!", roll_d)
                d_hit = d_hit + 1
                #print("Infantry hit", roll_d)
            #else : print("Defender misses!")
        # Defender Tank hits
        for i in range(d_tanks) :
            roll_dtank = random.randint(1,6)
            if roll_dtank <= 3 :
                d_hit = d_hit + 1
                #print("Tank hit", roll_dtank)
        for i in range(fighter_d) :
            roll_dfight = random.randint(1,6)
            if roll_dfight <= 4 :
                d_hit = d_hit + 1
                #print("Fighter hit", roll_dfight)
        for i in range(bomb_a) :
            roll_dbomb = random.randint(1,6)
            if roll_dbomb <= 1 :
                d_hit = d_hit + 1
                #print("Bomber hit", roll_dbomb)
        #print("Defender hits:", d_hit)
        #print("AA gun hits", aa_hit)

        if inf_a - d_hit > 0 :
            inf_a = inf_a - d_hit
        elif art_a + inf_a - d_hit > 0 :
            art_a = art_a + inf_a - d_hit
            inf_a = 0
        elif tanks_a + art_a + inf_a - d_hit > 0 :
            tanks_a = tanks_a + art_a + inf_a - d_hit
            inf_a = 0
            art_a = 0
        elif fighter_a + tanks_a + art_a + inf_a - d_hit > 0 :
            fighter_a = fighter_a + tanks_a + art_a + inf_a - d_hit
            inf_a = 0
            art_a = 0
            tanks_a = 0
        elif bomb_a + fighter_a + tanks_a + art_a + inf_a - d_hit > 0 :
            bomb_a = bomb_a + fighter_a + tanks_a + art_a + inf_a - d_hit
            inf_a = 0
            art_a = 0
            tanks_a = 0
            fighter_a = 0
        else :
            inf_a = 0
            art_a = 0
            tanks_a = 0
            fighter_a = 0
            bomb_a = 0
        attacker_num = inf_a + art_a + tanks_a + fighter_a + bomb_a
        #print("Remaining attacker infantry:", inf_a)
        #print("Remaining attacker artillery and buffed infantry:", art_a)
        #print("Remaining attacker tanks:", tanks_a)
        #print("Remaining attacker fighters:", fighter_a)
        #print("Remaining attacker bombers:", bomb_a)
        #print("Remaining number of attackers:", attacker_num)

        if inf_d - a_hit > 0 :
            inf_d = inf_d - a_hit
        elif bomb_d + inf_d - a_hit > 0 :
            bomb_d = bomb_d + inf_d - a_hit
            inf_d = 0
        elif aa + bomb_d + inf_d - a_hit > 0 :
            aa = aa + bomb_d + inf_d - a_hit
            inf_d = 0
            bomb_d = 0
        elif tanks_d + aa + bomb_d + inf_d - a_hit > 0 :
            tanks_d = tanks_d + aa + bomb_d + inf_d - a_hit
            inf_d = 0
            bomb_d = 0
            aa = 0
        elif fighter_d + tanks_d + aa + bomb_d + inf_d - a_hit > 0 :
            fighter_d = fighter_d + tanks_d + aa + bomb_d + inf_d - a_hit
            inf_d = 0
            bomb_d = 0
            aa = 0
            tanks_d = 0
        else :
            inf_d = 0
            bomb_d = 0
            aa = 0
            tanks_d = 0
            fighter_d = 0
        defender_num = inf_d + tanks_d + fighter_d + bomb_d + aa
        #print("Remaining defender infantry and artillery defenders:", inf_d)
        #print("Remaining defender bombers:", bomb_d)
        #print("Remaining defender tanks:", tanks_d)
        #print("Remaining defender fighters:", fighter_d)
        #print("Remaining number of defenders:", defender_num)
        #print("Remaining number of AA guns:", aa)

        if attacker_num > 0 and defender_num <= 0 :
            a_win = a_win + 1
            a_surv["infantry"] = a_surv.get("infantry", 0) + inf_a
            a_surv["artillery"] = a_surv.get("artillery", 0) + art_a
            a_surv["tanks"] = a_surv.get("tanks", 0) + tanks_a
            a_surv["fighters"] = a_surv.get("fighters", 0) + fighter_a
            a_surv["bombers"] = a_surv.get("bombers", 0) + bomb_a

            #print("Attacker wins!")
        elif defender_num > 0 and attacker_num <= 0 :
            d_win = d_win + 1
            d_surv["infantry and artillery"] = d_surv.get("infantry and artillery", 0) + inf_d
            d_surv["tanks"] = d_surv.get("tanks", 0) + tanks_d
            d_surv["fighters"] = d_surv.get("fighters", 0) + fighter_d
            d_surv["bombers"] = d_surv.get("bombers", 0) + bomb_d
            d_surv["AA guns"] = d_surv.get("AA guns", 0) + aa

            #print("Defender wins!")
        elif attacker_num <= 0 and defender_num <= 0 :
            draw = draw + 1
            #print("It's a draw!")
        else : continue

print("Results:", a_win, "attacker victories", d_win, "defender victories", draw, "draws")
print("Percentages of winning:", float(a_win/iterations), float(d_win/iterations), float(draw/iterations))

print("Attacker average survivors:")
for k,v in a_surv.items() :
    if a_win > 0 :
        v = float(v/a_win)
    else :
        v = 0
    if v > 0 :
        print(k,v)

print("Defender average survivors:")
for k,v in d_surv.items() :
    if d_win > 0 :
        v = float(v/d_win)
    else :
        v = 0
    if v > 0 :
        print(k,v)
