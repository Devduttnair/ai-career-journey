skills = ["Python", "Linux", "Git", "AWS"]

print(skills)
print(skills[0])
print(skills[2])
skills.append("Docker")
print(skills)
skills.remove("Linux")
print(skills)
print("Skills Remaining: ", len(skills))

for skill in skills:
    if skill == "AWS":
        print("Cloud skill found")
    else: 
        print(skill)
        
