data = """
|==============================|
|.. PyLao Libary by arrogroup .|
|.. Version 0.9 ...............|
|.. Made by arrogroup .........|
|==============================|
"""

# Class 'Lao NLP'
class nlp:
    def split(data):
        # simple ການຮຽນ to ['ກ', 'າ', 'ນ', 'ຮ', 'ຽ', 'ນ']
        lao_text_arry = [char for char in data]
        
        # ພະຍັນຊະນະ
        ph = ['ກ', 'ຂ', 'ຄ', 'ງ', 'ຈ', 'ສ', 'ຊ', 'ຍ', 'ດ', 'ຕ', 'ຖ', 'ທ', 'ນ', 'ບ', 'ປ', 'ຜ', 'ຝ', 'ພ', 'ຟ', 'ມ', 'ຢ', 'ຣ', 'ລ', 'ວ', 'ຫ', 'ອ', 'ຮ']
        pk = ['ກ', 'ຂ', 'ຄ', 'ງ', 'ຫ']
        pt = ['ງ', 'ຍ', 'ມ', 'ນ', 'ລ', 'ວ', 'ຼ']
        pl = ['ໝ', 'ໜ']

        # ສະລະ
        sn = ['ເ', 'ແ', 'ໄ', 'ໃ']
        sl = ['ະ', 'າ', 'ິ', 'ີ', 'ຶ', 'ື', 'ຸ', 'ູ', 'ໍ', 'ຳ'] # a a2  e e2 ue ue2 u u2 or arm

        # ວັນນະຍຸດ
        vn = ['່', '້', '໊', '໋'] # ແອັກ ໂທ ຕີ ຈັດຕະວາ

        # alphabet
        ap = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']

        # number
        nb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # process zone
        text_len = len(lao_text_arry)

        x = 0
        text = []

        while x < text_len:
            tps = ""

            if (lao_text_arry[x] and lao_text_arry[x+1] in sn[0]):
                tps += lao_text_arry[x]+lao_text_arry[x+1]
                x += 2

            text.append(tps)

        return text