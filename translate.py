from translate import Translator 

translator = Translator(to_lang="es")
translation = translator.translate("How are you?")
print(translation)