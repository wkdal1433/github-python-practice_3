class shinjoa_quiz:
    def __init__(self,shinjoa,show1,show2,answer):
        self.shinjoa = shinjoa
        self.show1 = show1
        self.show2 = show2
        self.answer = answer
    def show_question(self):
        print(f"{self.shinjoa}의 뜻은?\n")
        print(f"1.{self.show1}\n")
        print(f"2.{self.show2}\n")
        
        
    def check_answer(self):
        x = int(input("=> "))
        if x==self.answer:
            print("정답입니다.")
        else:
            print(f"틀렸습니다. 정답 : {self.answer}")


        


s1 = shinjoa_quiz("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
s1.show_question()
s1.check_answer()

s2 = shinjoa_quiz("혼코노", "혼자서는 코딩 노노", "혼자 코인 노래방", 2)
s2.show_question()
s2.check_answer()

s3 = shinjoa_quiz("애빼시", "애교 빼면 시체", "애들은 빼빼로 시시해", 1)
s3.show_question()
s3.check_answer()



