class CashRegister(object):

    def __init__(self, current_amount):
        self.current_amount = current_amount

    def top_up(self, X):
        self.current_amount += X

    def count_1000(self):
        return self.current_amount // 1000

    def take_away(self, X):
        if X > self.current_amount:
            print("В кассе недостаточно денег")
        else:
            self.current_amount -= X

    def show_amount(self):
        return self.current_amount

# ========================================
# Проверка
# ========================================

tmp = CashRegister(1000)
print(tmp.show_amount())
tmp.top_up(2000)
print(tmp.show_amount())
tmp.take_away(3500)
tmp.take_away(500)
print(tmp.show_amount())
print(tmp.count_1000())

