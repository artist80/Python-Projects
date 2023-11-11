#!/usr/bin/env python3

def determine_child_blood_group(father_blood, mother_blood):
    # Define blood group alleles
    blood_alleles = {
        'A': ('A', 'O'),
        'B': ('B', 'O'),
        'AB': ('A', 'B', 'AB', 'O'),
        'O': ('O',)
    }

    # Validate input
    if father_blood not in blood_alleles or mother_blood not in blood_alleles:
        return "Invalid blood group entered."

    # Determine child's potential blood groups
    child_blood_groups = set(blood_alleles[father_blood]) | set(blood_alleles[mother_blood])

    return list(child_blood_groups)

if __name__ == "__main__":
    # Get input from the user
    father_blood_group = input("Enter father's blood group (A, B, AB, or O): ").upper()
    mother_blood_group = input("Enter mother's blood group (A, B, AB, or O): ").upper()

    # Determine child's potential blood group
    child_blood_groups = determine_child_blood_group(father_blood_group, mother_blood_group)

    # Display the result
    print("Potential child's blood group(s):", ", ".join(child_blood_groups))
