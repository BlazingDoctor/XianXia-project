import os
import json

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

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    def load_from_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.from_dict(json.load(file))

# Example usage
def main(file_path):
    pass

def test():
    base_dir = "C:\\shared stuff\\non onedrive stuff folder\\programming\\personal projects\\XianXia script stuff\\staging region\\data"
    file_path = os.path.join(base_dir, 'characters.json')
    
    # Sample characters for testing
    test_characters = [
        Character("Alice"),
        Character("Bob")
    ]

    manager = CharacterManager()

    remove_test_local = False
    toggle_write_input = False
    toggle_read_output = True
    toggle_modify_character = True
    toggle_delete_files = False

    if toggle_write_input:
        for character in test_characters:
            manager.add_character(character)
        manager.save_to_file(file_path)
    
    if toggle_modify_character:
        manager.load_from_file(file_path)
        bob = manager.get_character("Bob")
        if bob:
            bob["x"] = 100
            bob["y"] = 100
            bob["health"] = 50
            manager.add_character(Character("Charlie"))
            if remove_test_local:
                manager.remove_character("Alice")
            manager.save_to_file(file_path)

    if toggle_read_output:
        manager.load_from_file(file_path)
        for name, data in manager.characters.items():
            print(f"{name}: {data}")

    if toggle_delete_files:
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    test()
