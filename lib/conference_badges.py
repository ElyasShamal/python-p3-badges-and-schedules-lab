def badge_maker(name):
    return f'Hello, my name is {name}.'

badge_maker('Aral')

def batch_badge_creator(names):
    badge = []
    for name in names:
        message = f'Hello, my name is {name}.'
        badge.append(message)
    return badge

batch_badge_creator(["Arel", "Carol"])

def assign_rooms(names):
    room_assignment = []
    for index, name in enumerate(names, start=1):
        room_assignments =  f"Hello, {name}! You'll be assigned to room {index}!"
        room_assignment.append(room_assignments)
    return room_assignment

assign_rooms(['Aral', 'Carol'])

def printer(names):
    badge_messages = batch_badge_creator(names)
    for message in badge_messages:
        print(message)

    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)
    
