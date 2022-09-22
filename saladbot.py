import random

dressings = ["olive oil","petrol","mustard","lemon juice","salad cream","mayonaise","balsamic vinegar","french dressing", "Caesar dressing","sweet chilli","honey","soy sauce","yogurt","vodka"]
extras = ["halloumi", "prawns", "chicken","ham","hard boiled egg","smoked salmon","parmesan","olives","mixed seeds","milk chocolate buttons"]
carbohydrates = ["ciabatta","rice", "pasta","quinoa","cous cous","bulgar wheat","lentils","potato","croutons","a whole loaf of Warburtons sliced bread","Praharsh's cheese","crisps"]
green_things_that_dylan_likes_to_eat = ["grass","spinach","rocket","watercress","lettuce","grated carrot","cucumber","avocado","lambs lettuce","mushroom","basil","parsley","romaine lettuce","little gem lettuce", "iceberg lettuce", "belgian endive","beetroot","radishes","green food colouring","green beans"]
instructions = ["The salad is blended and served in a tall glass", "The salad is slow cooked for 7hours",  "Serve on a rice cake base", "Hair dry for 5 minutes and leave to cool before serving"]

for num in range(random.randint(1,2)):
    print(random.choice(dressings))
for num in range(random.randint(0,2)):
    print(random.choice(extras))
for num in range(random.randint(0,3)):
    print(random.choice(carbohydrates))
for num in range(random.randint(1,3)):
    print(random.choice(green_things_that_dylan_likes_to_eat))
if random.randint(0,10) ==0:
    print(random.choice(instructions))
