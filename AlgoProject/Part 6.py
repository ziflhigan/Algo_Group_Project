# Define risk ratings for land conditions and wild animals
land_conditions = {
    "swamp": 4,
    "mountains_caves": 3,
    "thick_woods_lake": 3,
    "sandy_flat_land": 2,
    "inhabited_area": 1
}

wild_animals = {
    "full_of_wild": 5,
    "some_wild": 3,
    "small_poisonous": 4,
    "no_wild_animals": 1
}

# Define weights
weights = {
    "land_condition": 1,
    "wild_animal": 2
}

# List of islands with their respective conditions
islands = [
    {"name": "North", "land_condition": "swamp", "wild_animal": "full_of_wild"},
    {"name": "South", "land_condition": "mountains_caves", "wild_animal": "some_wild"},
    {"name": "East", "land_condition": "thick_woods_lake", "wild_animal": "full_of_wild"},
    {"name": "West", "land_condition": "sandy_flat_land", "wild_animal": "small_poisonous"},
    {"name": "Middle", "land_condition": "inhabited_area", "wild_animal": "no_wild_animals"}
]


def calculate_total_risk(island):
    land_risk = land_conditions[island["land_condition"]]
    animal_risk = wild_animals[island["wild_animal"]]
    total_risk = (land_risk * weights["land_condition"]) + (animal_risk * weights["wild_animal"])
    return total_risk


def find_safest_island(islands):
    min_risk = float('inf')
    safest_island = None
    for island in islands:
        total_risk = calculate_total_risk(island)
        if total_risk < min_risk:
            min_risk = total_risk
            safest_island = island
    return safest_island


safest_island = find_safest_island(islands)
print(f"The safest island is: {safest_island['name']} with a total risk of {calculate_total_risk(safest_island)}")
