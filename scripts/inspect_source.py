## Import json and open the file
import json

with open("data/raw/en.1.2024-25.json", "r", encoding="utf-8") as file:
    # convert the JSON data to a Python object
    data = json.load(file)

# Data type and keys
print(type(data), data.keys())

# Obtain the list of matches and the length of the list
matches = data["matches"]

print (len(matches))

# Obtain the first element of the list and obtain its keys
first_match = matches[0]
print(first_match)
print(first_match.keys())

# Obtain first match full time score
print("First match full time score: ", first_match["score"]["ft"])

full_time_score = first_match["score"]["ft"]

print(full_time_score[0])
print(full_time_score[1])


# Look for missing scores or invalid scores on the data
missing_score = 0
invalid_score_type = 0
missing_ht = 0
invalid_ht_type = 0
invalid_ht_length = 0
invalid_ht_values = 0
negative_ht_scores = 0
missing_ft = 0
invalid_ft_type = 0
invalid_ft_length = 0
invalid_ft_values = 0
negative_ft_scores = 0
Qht_valid = 0
Qft_valid = 0
inconsistent_scores = 0


# Validate score structure and half-time/full-time goal values
for match in matches:
    ht_valid = False
    ft_valid = False
    # Looking for scores that are missing
    if "score" not in match:
        missing_score += 1
    # Looking for scores that are not dictionaries with isintance and dict
    elif not isinstance(match["score"], dict):
        invalid_score_type += 1
    else:
        # Looking for missing ht
        if "ht" not in match["score"]:
            missing_ht += 1
        # Checking that ht is a list
        elif not isinstance(match["score"]["ht"], list):
            invalid_ht_type += 1
        # Checking that ht contains exactly two values
        elif len(match["score"]["ht"]) != 2:
            invalid_ht_length += 1
        # Checking that goals in ht are int
        elif type(match["score"]["ht"][0]) is not int or type(match["score"]["ht"][1]) is not int:
            invalid_ht_values += 1
        # Checking that the goals are not negatives in ht
        elif match["score"]["ht"][0] < 0 or match["score"]["ht"][1] < 0:
            negative_ht_scores += 1
        else:
            ht_valid = True
            Qht_valid += 1

        # Looking for missing ft
        if "ft" not in match["score"]:
            missing_ft += 1
        # Checking that ft is a list
        elif not isinstance(match["score"]["ft"], list):
            invalid_ft_type += 1
        # Checking that ft contains exactly two values
        elif len(match["score"]["ft"]) != 2:
            invalid_ft_length += 1
        # Checking that goals in ft are int
        elif type(match["score"]["ft"][0]) is not int or type(match["score"]["ft"][1]) is not int:
            invalid_ft_values += 1
        # Checking that the goals are not negatives in ft
        elif match["score"]["ft"][0] < 0 or match["score"]["ft"][1] < 0:
            negative_ft_scores += 1
        else:
            ft_valid = True
            Qft_valid += 1

        # Check score consistency only when both half-time and full-time scores are valid on both teams
        if ht_valid and ft_valid:
            # Neither team's half-time goals may exceed its full-time goals
            if match["score"]["ht"][0] >  match["score"]["ft"][0] or match["score"]["ht"][1] >  match["score"]["ft"][1] :
                inconsistent_scores += 1


print("Matches missing score: ", missing_score)
print("Invalid scores: ", invalid_score_type)
print("Matches missing half time score: ", missing_ht)
print("Half time score with invalid type: ", invalid_ht_type)
print("Half time score with invalid length: ", invalid_ht_length)
print("Matches with invalid ht value types: ", invalid_ht_values)
print("Matches with negative ht goals: ", negative_ht_scores)
print("Matches missing full time score: ", missing_ft)
print("Full time score with invalid type: ", invalid_ft_type)
print("Full time score with invalid length: ", invalid_ft_length)
print("Matches with invalid ft value types: ", invalid_ft_values)
print("Matches with negative ft goals: ", negative_ft_scores)
print("Matches with valid half-time scores:", Qht_valid)
print("Matches with valid full-time scores:", Qft_valid)
print("Matches with inconsistent scores:", inconsistent_scores)