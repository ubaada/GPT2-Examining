# Read the Tagged word file which is partition into 80/20
f = open("split_80.txt", "r")
txt = f.read()
txt = txt.replace("\n"," \n_notag ") # handling new lines as a tagged word
txt = txt.replace("  "," ") # clean double spaces
words = txt.split(" ") # Convert text to array of tagged words (word_tag) format 

# Gendered pairs dictionary to swap each other with.
dict = [["his","her"],["gods","goddesses"], ["manager","manageress"], ["barons","baronesses"],["nephew","niece"], ["prince","princess"], ["boars","sows"],["baron","baroness"], ["stepfathers","stepmothers"], ["wizard","witch"],["father","mother"], ["stepsons","stepdaughters"], ["sons-in-law","daughters-in-law"],["dukes","duchesses"], ["boyfriend","girlfriend"], ["fiances","fiancees"],["dad","mom"], ["shepherd","shepherdess"], ["uncles","aunts"],["beau","belle"], ["males","females"], ["hunter","huntress"],["beaus","belles"], ["grandfathers","grandmothers"], ["lads","lasses"],["daddies","mummies"], ["step-son","step-daughter"], ["masters","mistresses"],["policeman","policewoman"], ["nephews","nieces"], ["brother","sister"],["grandfather","grandmother"], ["priest","priestess"], ["hosts","hostesses"],["landlord","landlady"], ["husband","wife"], ["poet","poetess"],["landlords","landladies"], ["fathers","mothers"], ["masseur","masseuse"],["monks","nuns"], ["usher","usherette"], ["hero","heroine"],["stepson","stepdaughter"], ["postman","postwoman"], ["god","goddess"],["milkmen","milkmaids"], ["stags","hinds"], ["grandpa","grandma"],["chairmen","chairwomen"], ["husbands","wives"], ["grandpas","grandmas"],["stewards","stewardesses"], ["murderer","murderess"], ["manservant","maidservant"],["men","women"], ["host","hostess"], ["heirs","heiresses"],["masseurs","masseuses"], ["boy","girl"], ["male","female"],["son-in-law","daughter-in-law"], ["waiter","waitress"], ["tutors","governesses"],["priests","priestesses"], ["bachelor","spinster"], ["millionaire","millionairess"],["steward","stewardess"], ["businessmen","businesswomen"], ["congressman","congresswoman"],["emperor","empress"], ["duke","duchess"], ["sire","dam"],["son","daughter"], ["sirs","madams"], ["widower","widow"],["kings","queens"], ["papas","mamas"], ["grandsons","granddaughters"],["proprietor","proprietress"], ["monk","nun"], ["headmasters","headmistresses"],["grooms","brides"], ["heir","heiress"], ["boys","girls"],["gentleman","lady"], ["uncle","aunt"], ["he","she"],["king","queen"], ["princes","princesses"], ["policemen","policewomen"],["governor","matron"], ["fiance","fiancee"], ["step-father","step-mother"],["waiters","waitresses"], ["mr","mrs"], ["stepfather","stepmother"],["daddy","mummy"], ["lords","ladies"], ["widowers","widows"],["emperors","empresses"], ["father-in-law","mother-in-law"], ["abbot","abbess"],["sir","madam"], ["actor","actress"], ["mr.","mrs."],["wizards","witches"], ["actors","actresses"], ["chairman","chairwoman"],["sorcerer","sorceress"], ["postmaster","postmistress"], ["brothers","sisters"],["lad","lass"], ["headmaster","headmistress"], ["papa","mama"],["milkman","milkmaid"], ["heroes","heroines"], ["man","woman"],["grandson","granddaughter"], ["groom","bride"], ["sons","daughters"],["congressmen","congresswomen"], ["businessman","businesswoman"], ["boyfriends","girlfriends"]]

new_txt = ""
is_newline = True # for capitalising 1st letter after each "." or newline
for i in words:
    if "_" in i:
        combined = i.split("_")
        old_word = combined[0]
        tag = combined[1]
        new_word = old_word
        
        # === Counterfactua Data Augmentation ========
        # special case (her/him). 
        if old_word == "her" and tag=="PPO":
            new_word = "him"
        elif old_word == "him" and tag=="PPO":
            new_word = "her"
        elif tag != "NP": # exclude proper nouns
            for d in dict: # swap pairs
                if old_word == d[0]:
                    new_word = d[1]
                elif old_word == d[1]:
                    new_word = d[0]
        # ======================================
                    
        if is_newline == True:
            new_word= new_word.title()
        if (new_word != ".") and (new_word != ",") and (new_word != "\n"):
            new_word = " " + new_word # Add a space before a word if it's not above conditions.
            is_newline = False
        if new_word == "." or new_word == "\n":
            is_newline = True
        new_txt = new_txt + new_word

# write the file
text_file = open("cdo_80.txt", "w")
text_file.write(new_txt)
text_file.close()
    