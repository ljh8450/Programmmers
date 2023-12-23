participant = list(input().split())
completion = list(input().split())

participant.sort()
completion.sort()
for i in range(len(completion)):
    if participant[i] != completion[i]:
        print(participant[i])
print(participant[len(participant)-1])