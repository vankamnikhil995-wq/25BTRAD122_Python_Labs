import random

print("===== DICE SIMULATOR =====")

try:
    number_of_dice = int(input("Enter number of dice: "))
    number_of_rolls = int(input("Enter number of rolls: "))

    if number_of_dice <= 0 or number_of_rolls <= 0:
        print("Please enter positive numbers.")

    else:
        face_frequency = {
            1: 0, 2: 0, 3: 0,
            4: 0, 5: 0, 6: 0
        }

        total_frequency = {}

        print("\n===== DICE ROLL RESULTS =====")

        for i in range(number_of_rolls):
            total = 0
            results = []

            for j in range(number_of_dice):
                result = random.randint(1, 6)
                results.append(result)
                total += result

                face_frequency[result] += 1

            if total in total_frequency:
                total_frequency[total] += 1
            else:
                total_frequency[total] = 1

            print("Roll", i + 1, ":", results, "Total =", total)

        print("\n===== FACE FREQUENCY =====")

        for face, count in face_frequency.items():
            print(face, ":", count, "times")

        print("\n===== TOTAL SCORE FREQUENCY =====")

        for score, count in sorted(total_frequency.items()):
            print(score, ":", count, "times")

except ValueError:
    print("Please enter valid whole numbers.")
