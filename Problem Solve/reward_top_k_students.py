class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Ok we got this, so this is pretty easy, so what we need to do is say the report is matched to the student_id so for example ["good", "bad"] and Id [1,2], so the student ID with good would have postiive feedback, whilst the 2nd student will get a negative feedback, and we sort it via [::k], but also for the points system we have to iterate through the each word in the report
        
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        student = []

        for x, y in zip(report, student_id):
            score = 0
            for word in x.split():
                # feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1
                if word in positive:
                    score += 3
                elif word in negative:
                    score -= 1
            student.append((score, y))
        student.sort(key=lambda item: (-item[0], item[1]))

        return [students for score, students in student[:k]]