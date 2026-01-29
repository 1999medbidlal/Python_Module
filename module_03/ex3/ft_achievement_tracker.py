data = {
        'alice': [
            'first_blood',
            'pixel_perfect',
            'speed_runner',
            'level_10',
            'first_blood',
            'first_blood'
        ],
        'bob': [
            'level_master',
            'boss_hunter',
            'treasure_seeker',
            'level_10',
            'level_master',
            'level_master'
        ],
        'charlie': [
            'treasure_seeker',
            'boss_hunter',
            'combo_king',
            'first_blood',
            'level_10',
            'boss_hunter',
            'first_blood',
            'boss_hunter',
            'first_blood'
        ]
    }
alice = set(data['alice'])
bob = set(data['bob'])
charlie = set(data['charlie'])
print("=== Achievement Tracker System ===")
print(f"\nPlayer alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")
print("\n=== Achievement Analytics ===")
unique_achievement = alice.union(bob).union(charlie)
print(f"All unique achievements: {unique_achievement}")
total_achievement = len(unique_achievement)
print(f"Total unique achievements:{total_achievement}")
point_common = alice.intersection(bob).intersection(charlie)
print(f"\nCommon to all players: {point_common}")
unique_alice = alice.difference(bob).difference(charlie)
unique_bob = bob.difference(alice).difference(charlie)
unique_charlie = charlie.difference(alice).difference(bob)
rare_achievements = unique_alice.union(unique_bob).union(unique_charlie)
print(f"Rare achievements (1 player): {rare_achievements}")
print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
