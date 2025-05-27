# # 타입힌트 연습문제
# # [1, 2, 3] * 3 => [1, 2, 3, 1, 2, 3, 1, 2, 3]가 나오는 solution 함수를 만들어주세요.

# def solution():
#     pass

# solution([1, 2, 3], 3)


# def solution():
#     print((a: int, b: int, c: int)) * 3

    
# solution([1, 2, 3], 3)


# def solution(data: list[int], times: int)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, subject, score):
        self.scores.append((subject, score))

    def get_average(self):
        if not self.scores:
            return 0
        return sum([s for _, s in self.scores]) / len(self.scores)

    def get_highest_subject(self):
        if not self.scores:
            return ("없음", 0)
        return max(self.scores, key=lambda x: x[1])

    def show_scores(self):
        for sub, sc in self.scores:
            print(f"{sub}: {sc}점")
        print(f"평균 점수: {self.get_average()}점")