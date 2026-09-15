# AI Response Evaluation Tool

def calculate_score(accuracy, relevance, clarity, completeness, instruction_following):
    total = accuracy + relevance + clarity + completeness + instruction_following
    percentage = (total / 25) * 100
    return total, percentage


print("AI Response Evaluation Tool")
print("-" * 30)

accuracy = int(input("Accuracy score (1-5): "))
relevance = int(input("Relevance score (1-5): "))
clarity = int(input("Clarity score (1-5): "))
completeness = int(input("Completeness score (1-5): "))
instruction_following = int(input("Instruction-following score (1-5): "))

total, percentage = calculate_score(
    accuracy,
    relevance,
    clarity,
    completeness,
    instruction_following
)

print("\nEvaluation Result")
print("Total Score:", total, "/ 25")
print("Quality Score:", percentage, "%")

if percentage >= 90:
    print("Excellent response")
elif percentage >= 75:
    print("Good response")
elif percentage >= 60:
    print("Acceptable response")
else:
    print("Needs improvement")
