import os
import json
import discord
from discord.ext import tasks, commands
from datetime import datetime
from config import DATA
from unidecode import unidecode

class Server:
    def __init__(self, guild):
        self.guild = guild
        self.server_name = guild.name
        self.server_path = os.path.join(DATA, self.server_name)
        self.users_path = os.path.join(self.server_path, "users")
        self.info_file_path = os.path.join(self.server_path, "info.txt")
        self.config_file_path = os.path.join(self.server_path, "config.py")

        self.initialize_data_structure()

    def initialize_data_structure(self):
        sanitized_folder_path = unidecode(self.users_path)
        os.makedirs(sanitized_folder_path, exist_ok=True)

        if not os.path.exists(self.info_file_path):
            self.update_server_info()

        if not os.path.exists(self.config_file_path):
            self.create_default_config()

    def create_default_config(self):
        with open(self.config_file_path, "w") as config_file:
            config_content = """announcement_channel = "general"
moderation_enabled = True
"""
            config_file.write(config_content)

    def update_server_info(self):
        self.server_info = {
            "server_id": str(self.guild.id),
            "display_name": self.server_name,
            "member_count": len(self.guild.members),
        }

        with open(self.info_file_path, "w") as info_file:
            json.dump(self.server_info, info_file)
    
    def update_users_info(self):
        for member in self.guild.members:
            user = User(self, member)
            user.load_user_info()

    def periodic_task(self):
        self.update_server_info()
        self.update_users_info()

class User:
    def __init__(self, server, user):
        self.server = server
        self.user = user
        self.user_folder_path = os.path.join(server.users_path, str(user.display_name))
        self.info_file_path = os.path.join(self.user_folder_path, "info.json")
        self.moderate_file_path = os.path.join(self.user_folder_path, "moderate.json")

        self.initialize_data_structure()
        self.load_user_info()
        self.load_moderation_info()

    def initialize_data_structure(self):
        sanitized_folder_path = unidecode(self.user_folder_path)
        os.makedirs(sanitized_folder_path, exist_ok=True)

        if not os.path.exists(self.info_file_path):
            self.create_default_info()

        if not os.path.exists(self.moderate_file_path):
            self.create_default_moderation()

    def create_default_info(self):
        default_info = {
            "creation_date": str(self.user.created_at),
            "display_name": self.user.display_name,
            "user_id": str(self.user.id),
        }

        sanitized_info_path = unidecode(self.info_file_path)
        with open(sanitized_info_path, "w") as info_file:
            json.dump(default_info, info_file)

    def create_default_moderation(self):
        default_moderation = {
            "warns": 0,
            "mutes": 0,
            "bans": 0,
            "kicks": 0,
        }
        
        sanitized_moderate_path = unidecode(self.moderate_file_path)
        with open(sanitized_moderate_path, "w") as moderate_file:
            json.dump(default_moderation, moderate_file)

    def load_user_info(self):
        sanitized_info_path = unidecode(self.info_file_path)

        with open(sanitized_info_path, "r") as info_file:
            sanitized_info_path= json.load(info_file)

    def load_moderation_info(self):
        sanitized_moderate_path = unidecode(self.moderate_file_path)
        with open(sanitized_moderate_path, "r") as moderate_file:
            self.moderation_info = json.load(moderate_file)

    def update_moderation_info(self, action, duration=None):
        timestamp = str(datetime.utcnow())

        if action not in self.moderation_info:
            self.moderation_info[action] = {}

        if duration:
            self.moderation_info[action][timestamp] = duration
        else:
            self.moderation_info[action][timestamp] = None

        with open(self.moderate_file_path, "w") as moderate_file:
            json.dump(self.moderation_info, moderate_file)

    def add_int(self, server_name, user_display_name, category, value):
        server = None
        for guild in self.bot.guilds:
            if guild.name == server_name:
                server = Server(guild)
                break

        if server:
            for member in server.guild.members:
                if member.display_name == user_display_name:
                    user = User(server, member)
                    if category not in user.moderation_info:
                        user.moderation_info[category] = 0
                    user.moderation_info[category] += value
                    user.update_moderation_info(category)
                    break
            else:
                print("User not found in the server.")
        else:
            print("Server not found.")