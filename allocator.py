def allocate_resources(users, total_cpu, total_ram):
    # Sort users by priority (higher priority first)
    users_sorted = sorted(users, key=lambda x: x['priority'], reverse=True)

    allocated = []
    waiting = []

    for user in users_sorted:
        if user['cpu'] <= total_cpu and user['ram'] <= total_ram:
            allocated.append(user)
            total_cpu -= user['cpu']
            total_ram -= user['ram']
        else:
            waiting.append(user)

    return allocated, waiting, total_cpu, total_ram