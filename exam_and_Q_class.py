

class exam:
    qlist = []

    def __init__(self, id):
        self.id = id


    def add(self, question):
        self.qlist.append(question)

    def remove(self,question):
        if(self.find(question)):
            for q in self.qlist:
                if q.id == question.id:
                    saved = q
                    self.qlist.remove(q)
                    return saved
            '''self.qlist.remove(question)
            return question'''
        else:
            return None

    def find(self, question):
        found = False
        for q in self.qlist:
            if q.id == question.id:
                found = True
                return found

        '''if question in self.qlist:
            found = True'''
        return found

    def str(self):
        string = ""
        for q in self.qlist:
            string += (q.str() + "   ||||   ")
        return string

class question:
    def __init__(self, id, text, points):
        self.id = id
        self.text = text
        self.points = points

    def str(self):
        return ("id: " + str(self.id) + "; text: " + self.text + "; points: " + str(self.points))


if __name__ == "__main__":
    test = exam(123)
    q1 = question(1, "How Long is a Chinese name.", 5)
    q2 = question(2, "Are you sure?", 3)
    q3 = question(3, "What is your name?", 2)
    q4 = question(4, "What is your quest?", 4)
    q5 = question(5, "What is your favorite color?", 6)
    q6 = question(2, "Are you sure?", 3)

    test.add(q1)
    test.add(q2)
    print(test.str())
    test.add(q3)
    a = test.remove(q6)
    print(test.str())
    test.add(q4)
    b = test.remove(q1)
    print(test.str())
    c = test.remove(q4)
    test.add(q5)
    print(test.str())
    print("\n" + a.str() + '\n' + b.str() + '\n' + c.str() + '\n')
