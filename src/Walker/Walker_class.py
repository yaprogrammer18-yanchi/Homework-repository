import random
import math


class Walker:
    def __init__(self, events_and_prob):
        if not events_and_prob:
            raise ValueError("Переданный список пустой")
        self.events_and_prob = events_and_prob
        self.probability_check()
        self.quantity_of_lines = len(self.events_and_prob)
        self.overage_prob = 1 / self.quantity_of_lines

        self.donors = []
        self.recipients = []
        self.table = [None] * self.quantity_of_lines

        for i in range(len(self.events_and_prob)):
            # список вида [...["событие", нужная вероятность, имеющаяся]...]
            if self.events_and_prob[i][1] <= self.overage_prob:
                self.events_and_prob[i].append(self.overage_prob)
                self.donors.append(self.events_and_prob[i])
            else:
                self.events_and_prob[i].append(self.overage_prob)
                self.recipients.append(self.events_and_prob[i])
        self.build_table()

    def probability_check(self):
        i = 0
        for el in self.events_and_prob:
            i += el[1]
        if i != 1:
            raise ValueError("Вероятности в сумме не дают 1!")

    def build_table(self):
        i = 0
        while self.donors and self.recipients:
            donor = self.donors.pop()
            recipient = self.recipients.pop()

            donor_event, donor_needed_prob, donor_current_prob = donor
            recipient_event, recipient_needed_prob, recipient_current_prob = recipient

            donor_can_give = donor_current_prob - donor_needed_prob

            recipient_current_prob += donor_can_give

            recipient[2] = recipient_current_prob
            if recipient_needed_prob >= recipient_current_prob:
                self.recipients.append(recipient)
            else:
                self.donors.append(recipient)

            barrier = self.overage_prob * i + (self.overage_prob - donor_can_give)

            self.table[i] = [donor_event, recipient_event, barrier]
            i += 1
        self.table[-1] = [recipient_event, 0, 1]

    def printall(self):
        for i in range(len(self.table)):
            print(self.table[i])

    def get_random(self):
        random_number = random.random()
        line = math.floor(random_number * self.quantity_of_lines)
        line = self.table[line]
        rational_part = random_number - int(random_number)
        if rational_part < line[2]:
            return line[0]
        return line[1]
