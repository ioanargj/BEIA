def implicit():
    import google.auth
    translate_client._connection._credentials
    from google.cloud import translate_v2

    translate_client = translate.Client()



def translate_text(text, target_language='en'):

    # Detect the language
    translate_client = translate.Client()

    # The result can have more than one sentence
    result = translate_client.detect_language(text)
    print("Text: {}".format(text))
    print("Confidence: {}".format(result['confidence']))
    print("Language: {}".format(result['language']))

if __name__ == '__main__':

    with open("helloworld.txt", "r") as f:
         translate_text(f)
    with open("testfile.txt", "w") as fisier:
         print(file=fisier)

