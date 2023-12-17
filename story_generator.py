#!/usr/bin/env python3

import random

class AdvancedStoryGenerator:
    def __init__(self):
        self.characters = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
        self.locations = ["a mysterious forest", "an enchanted castle", "a bustling city", "a quiet village", "a distant planet"]
        self.actions = ["discovered a hidden treasure", "embarked on a magical journey", "encountered a mythical creature", "solved a perplexing mystery", "faced a formidable enemy"]
        self.adjectives = ["brave", "curious", "clever", "mysterious", "adventurous"]

    def generate_story(self, character=None, location=None, action=None, adjective=None):
        if not character:
            character = random.choice(self.characters)
        if not location:
            location = random.choice(self.locations)
        if not action:
            action = random.choice(self.actions)
        if not adjective:
            adjective = random.choice(self.adjectives)

        story = f"{character}, a {adjective} adventurer, found themselves in {location}. They {action}."

        return story

    def generate_custom_story(self):
        print("Customize Your Story:")
        character = input("Enter the main character's name (or press Enter for random): ")
        location = input("Enter the story location (or press Enter for random): ")
        action = input("Enter the main action (or press Enter for random): ")
        adjective = input("Enter an adjective describing the character (or press Enter for random): ")

        custom_story = self.generate_story(character, location, action, adjective)
        return custom_story

    def save_story_to_file(self, story, filename="generated_stories.txt"):
        with open(filename, 'a') as file:
            file.write(story + "\n\n")
        print(f"Story saved to {filename}")

# Example usage
story_generator = AdvancedStoryGenerator()

for _ in range(3):  # Generate three stories
    generated_story = story_generator.generate_custom_story()
    print("\nStory:")
    print(generated_story)

    save_prompt = input("Do you want to save this story? (yes/no): ").lower()
    if save_prompt == 'yes':
        story_generator.save_story_to_file(generated_story)
