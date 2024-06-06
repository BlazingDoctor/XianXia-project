import time

class Character:
    def __init__(self, name):
        self.name = name
        self.data = {"x": 0, "y": 0, "health": 100}

    def to_dict(self):
        return {self.name: self.data}

    @staticmethod
    def from_dict(data):
        name, attributes = list(data.items())[0]
        character = Character(name)
        character.data = attributes
        return character

    def __repr__(self):
        return f"Character(name={self.name}, data={self.data})"

class CharacterManager:
    def __init__(self):
        self.characters = {}

    def add_character(self, character):
        self.characters[character.name] = character.data

    def remove_character(self, name):
        if name in self.characters:
            del self.characters[name]

    def get_character(self, name):
        return self.characters.get(name, None)

    def to_dict(self):
        return self.characters

    def from_dict(self, data):
        self.characters = data

# Example usage
def main():
    manager = CharacterManager()

    # Add some characters
    manager.add_character(Character("Alice"))
    manager.add_character(Character("Bob"))

    # Measure time to modify Bob's attributes
    start_time = time.time()
    bob = manager.get_character("Bob")
    if bob:
        bob["x"] = 100
        bob["y"] = 100
        bob["health"] = 50
    modify_time = time.time() - start_time
    print(f"Time to modify Bob: {modify_time:.10f} seconds")

    # Measure time to add Charlie
    # Also an Example of initializing a character from a dictionary
    start_time = time.time()
    charlie_dict = {"Charlie": {"x": 10, "y": 20, "health": 90}}
    charlie = Character.from_dict(charlie_dict)
    manager.add_character(charlie)
    add_time = time.time() - start_time
    print(f"Time to add Charlie: {add_time:.10f} seconds")

    # Measure time to remove Alice
    start_time = time.time()
    manager.remove_character("Alice")
    remove_time = time.time() - start_time
    print(f"Time to remove Alice: {remove_time:.10f} seconds")

    # Print characters
    for name, data in manager.characters.items():
        print(f"{name}: {data}")

if __name__ == "__main__":
    main()
