data = {
    'players': {
        'alice': {
            'items': {
                'pixel_sword': 1,
                'code_bow': 1,
                'health_byte': 1,
                'quantum_ring': 3
            },
            'total_value': 1875,
            'item_count': 6
        },
        'bob': {
            'items': {
                'code_bow': 3,
                'pixel_sword': 2
            },
            'total_value': 900,
            'item_count': 5
        },
        'charlie': {
            'items': {
                'pixel_sword': 1,
                'code_bow': 1
            },
            'total_value': 350,
            'item_count': 2
        },
        'diana': {
            'items': {
                'code_bow': 3,
                'pixel_sword': 3,
                'health_byte': 3,
                'data_crystal': 3
            },
            'total_value': 4125,
            'item_count': 12
        }
    },
    'catalog': {
        'pixel_sword': {
            'type': 'weapon',
            'value': 150,
            'rarity': 'common'
        },
        'quantum_ring': {
            'type': 'accessory',
            'value': 500,
            'rarity': 'rare'
        },
        'health_byte': {
            'type': 'consumable',
            'value': 25,
            'rarity': 'common'
        },
        'data_crystal': {
            'type': 'material',
            'value': 1000,
            'rarity': 'legendary'
        },
        'code_bow': {
            'type': 'weapon',
            'value': 200,
            'rarity': 'uncommon'
        }
    }
}

print("=== Player Inventory System ===")
print("\n=== Alice's Inventory ===")
alice_items = data.get("players").get("alice").get("items")
categories = {}
for item, qty in alice_items.items():
    item_type = data.get("catalog").get(item).get("type")
    item_rarity = data.get("catalog").get(item).get("rarity")
    item_value = data.get("catalog").get(item).get("value")
    total_item = qty * item_value
    categories[item_type] = categories.get(item_type, 0) + qty
    print(f"{item} ({item_type},{item_rarity}) : {qty}x @ "
          f"{item_value} gold each = {total_item} gold")
total_value = data.get("players").get("alice").get("total_value")
item_count = data.get("players").get("alice").get("item_count")
print(f"\nInventory value: {total_value} gold")
print(f"Item count: {item_count} items")
output = ""
for key, value in categories.items():
    output += f"{key}({value}), "
print(f"Categories: {output[:-2]}")
print("\n=== Transaction: Alice gives Bob 2 quantum_ring ===")
alice_items["quantum_ring"] -= 2
bob_items = data.get("players").get("bob").get("items")
bob_items.update({"quantum_ring": 2})
print("Transaction successful!")
print("\n=== Updated Inventories ===")
print(f'Alice quantum_ring : {alice_items.get("quantum_ring")}')
print(f'Bob quantum_ring : {bob_items.get("quantum_ring")}')
item_rarity = []
total_valuable = 0
item_count = 0
for item, qty in alice_items.items():
    valuable = data.get("catalog").get(item).get("value")
    total_valuable += valuable * qty
    item_count += qty
    rarity = data.get("catalog").get(item).get("rarity")
    if rarity == "rare":
        item_rarity.append(item)
print("\n=== Inventory Analytics ===")
print(f"Most valuable player: Alice ({total_valuable} gold)")
print(f"Most items: Alice ({item_count} items)")
output = ""
for rare in item_rarity:
    output += f"{rare}, "
print(f"Rarest items: {output[:-2]}")
