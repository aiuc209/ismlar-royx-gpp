class IsmTasnifi:
    def __init__(self, ism):
        self.ism = ism

    def tasnif(self):
        if len(self.ism) <= 3:
            return "Oddiy"
        elif 4 <= len(self.ism) <= 6:
            return "O‘rtacha"
        else:
            return "Murakkab"

def ismlar_tasnifi(ismlar):
    tasniflangan_ismlar = []
    for ism in ismlar:
        tasnif = IsmTasnifi(ism)
        tasniflangan_ismlar.append((ism, tasnif.tasnif()))
    return tasniflangan_ismlar

ismlar = ["Ali", "Abdulloh", "Abdulaziz", "Muhammad", "Muhammadsodiq"]
print(ismlar_tasnifi(ismlar))
