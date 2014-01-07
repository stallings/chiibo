
# import statements
import json


# encapsulates properties for meta
class Meta():
    default_language = 'us'
    language_directory = ''
    current_language = default_language
    translation = {}


def translate(text):
    if Meta.current_language == Meta.default_language: return text
    elif text in Meta.translation: return Meta.translation[text]
    else: return text
    
    
def generate_language_file(language):
    source_file = open(Meta.language_directory + 'source.txt', 'r')
    language_file = open(Meta.language_directory + language + '.json', 'w')
    
    keyword_map = {}
    for line in source_file: 
        if line[0] != '#' and line != '\n': keyword_map[line.strip('\n')] = 0
     
    json.dump(keyword_map, language_file)
    
    language_file.close()
    source_file.close()
    


def set_directory(directory):
    Meta.language_directory = directory



def set_language(language):
    try:
        if language == None: language = Meta.default_language
        language_file = open(Meta.language_directory + language + '.json', 'r')
    except IOError:
        Meta.current_language = Meta.default_language
        return Meta.current_language
    else:
        Meta.current_language = language
        Meta.translation = json.load(language_file)
        language_file.close()
        return Meta.current_language
        
        
