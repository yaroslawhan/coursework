import eel

# Определите путь к HTML файлу
eel.init('web')

chrome_path = r'C:\Users\yaros\Downloads\chrome-win'
eel.start('index.html', size=(1200, 800), chrome_path=chrome_path)
