def allocate_resources(users, total_cpu, total_ram):
    allocated = []
    waiting = []

    for user in users:
        if user['cpu'] <= total_cpu and user['ram'] <= total_ram:
            allocated.append(user)
            total_cpu -= user['cpu']
            total_ram -= user['ram']
        else:
            waiting.append(user)

    return allocated, waiting, total_cpu, total_ram