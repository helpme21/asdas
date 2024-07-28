meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            }

while True:   
    a=input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ").upper()
    if a in meme_dict.keys():
        print("Tanım: "+meme_dict[a])
