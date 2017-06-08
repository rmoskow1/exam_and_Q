#exam class, question's - add(),remove(),
import unittest
from exam_and_Q_class import exam,question

class ExamTesting(unittest.testcase()):
    #test that if a question is added, it can then be found
    def test_find(self): 
        q = question(question,id,text,points)
        exam.add(exam,q)
        self.assertEquals(exam.find(exam,q),True)
    
    #check if adding puts it in the exam's list
    def test_add(self):
        q = question(question,id,text,points)
        exam.add(exam,q)
        self.assertTrue(q in exam.qlist)
    
    #check that when removed, a question is no longer in the exam's list
    def test_remove(self):
        q = question(question,id,text,points)
        exam.add(exam,q)
        exam.remove(exam,q)
        self.assertFalse(q in exam.qlist)

if __name__=="__main__":
    unittest.main()
        