score = 70

if 90 <= score <= 100:
    score_letter = "A"
   
elif 80 <= score <= 89:
    score_letter = "B"

elif 70 <= score <= 79:
    score_letter = "C"

elif 60 <= score <= 69:
    score_letter = "D"

else: 
    score_letter = "F"

print(f'Score: {score}')
print(f'Grade: {score_letter}')
