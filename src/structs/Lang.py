import json
import os

class Lang:
    def __init__(self, lang_key):
        self.lang_key = lang_key
        self.translations = self.load_translations()

    def load_translations(self):
        lang_file_path = os.path.join('ressources', 'lang', f'{self.lang_key}.json')
        with open(lang_file_path, 'r', encoding='utf-8') as lang_file:
            translations = json.load(lang_file)
        return translations

    def translate(self, key):
        return self.translations.get(key, key)

    @staticmethod
    async def readLangs():
        lang_dir = os.path.join('ressources', 'lang')
        return [f.split('.')[0] for f in os.listdir(lang_dir) if f.endswith('.json')]
