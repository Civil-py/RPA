


HIGHEST =  (5 + 7 + 5 + 7 + 8 + 9 + 5 + 5 + 5 + 7 + 5 + 7 + 5 + 5 + 7 + 7 + 5 + 5 + 7 + 7 + 7)

HIGHEST_LIST_VALUE = [5, 7, 5, 7, 8, 9, 5, 5, 5, 7, 5, 7, 5, 5, 7, 7, 5, 5, 7, 7, 7]

QUESTIONS = ["q1" , "q2" , "q3" , "q4" , "q5" , "q6 " , "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21"]

questions_dict = dict(zip(QUESTIONS, HIGHEST_LIST_VALUE))

class Suitability():

    @staticmethod
    def suitability(answers):
        q1 = Suitability.get_Q1(answers.Qone)
        q2 = Suitability.get_Q2(answers.Qtwo)
        q3 = Suitability.get_Q3(answers.Qthree)
        q4 = Suitability.get_Q4(answers.Qfour)
        q5 = Suitability.get_Q5(answers.Qfive)
        q6 = Suitability.get_Q6(answers.Qsix)
        q7 = Suitability.get_Q7(answers.Qseven)
        q8 = Suitability.get_Q8(answers.Qeight)
        q9 = Suitability.get_Q9(answers.Qnine)
        q10 = Suitability.get_Q10(answers.Qten)
        q11 = Suitability.get_Q11(answers.Qeleven)
        q12 = Suitability.get_Q12(answers.Qtwelve)
        q13 = Suitability.get_Q13(answers.Qthirteen)
        q14 = Suitability.get_Q14(answers.Qfourteen)
        q15 = Suitability.get_Q15(answers.Qfifteen)
        q16 = Suitability.get_Q16(answers.Qsixteen)
        q17 = Suitability.get_Q17(answers.Qseventeen)
        q18 = Suitability.get_Q18(answers.Qeighteen)
        q19 = Suitability.get_Q19(answers.Qnineteen)
        q20 = Suitability.get_Q20(answers.Qtwenty)
        q21 = Suitability.get_Q21(answers.Qtwentyone)
        suitability_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21]
        return suitability_list


    def get_Q1(q1):
            if q1 == 'A':
                return 0
            if q1 == 'B':
                return 2
            if q1 == 'C':
                return 3
            if q1 == 'D':
                return 4
            if q1 == 'E':
                return 5
            else:
                return 0

    def get_Q2(q2):

        if q2 == 'A':
            return 0
        if q2 == 'B':
            return 5
        if q2 == 'C':
            return 2
        if q2 == 'D':
            return 0
        if q2 == 'E':
            return 7
        else:
            return 0

    def get_Q3(q):

        if q == 'A':
            return 0
        if q == 'B':
            return 3
        if q == 'C':
            return 4
        if q == 'D':
            return 5
        else:
            return 0

    def get_Q4(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 1
        if q == 'C':
            return 4
        if q == 'D':
            return 3
        if q == 'E':
            return 2
        if q == 'F':
            return 2
        if q == 'G':
            return 2
        if q == 'H':
            return 7
        if q == 'I':
            return 6
        if q == 'J':
            return 5
        if q == 'K':
            return 4
        else:
            return 0

    def get_Q5(q):
        if q == 'A':
            return 1
        if q == 'B':
            return 2
        if q == 'C':
            return 3
        if q == 'D':
            return 4
        if q == 'E':
            return 5
        if q == 'F':
            return 6
        if q == 'G':
            return 7
        if q == 'H':
            return 5
        else:
            return 0

    def get_Q6(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 1
        if q == 'C':
            return 2
        if q == 'D':
            return 3
        if q == 'E':
            return 4
        if q == 'F':
            return 5
        if q == 'G':
            return 6
        if q == 'H':
            return 7
        if q == 'I':
            return 8
        if q == 'J':
            return 9
        else:
            return 0

    def get_Q7(q):
        if q == 'A':
            return 5
        if q == 'B':
            return 5
        if q == 'C':
            return 4
        if q == 'D':
            return 0
        if q == 'E':
            return 0
        else:
            return 0

    def get_Q8(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 5
        if q == 'C':
            return 5
        if q == 'D':
            return 4
        if q == 'E':
            return 2
        if q == 'F':
            return 2
        else:
            return 0

    def get_Q9(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 3
        if q == 'C':
            return 1
        if q == 'D':
            return 5
        if q == 'E':
            return 2
        else:
            return 0

    def get_Q10(q):
        if q == 'A':
            return 7
        if q == 'B':
            return 5
        if q == 'C':
            return 2
        if q == 'D':
            return 0
        else:
            return 0

    def get_Q11(q):
        if q == 'A':
            return 4
        if q == 'B':
            return 5
        if q == 'C':
            return 3
        if q == 'D':
            return 5
        if q == 'E':
            return 4
        if q == 'F':
            return 5
        else:
            return 0

    def get_Q12(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 1
        if q == 'C':
            return 3
        if q == 'D':
            return 4
        if q == 'E':
            return 5
        if q == 'F':
            return 6
        if q == 'G':
            return 7
        else:
            return 0

    def get_Q13(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 2
        if q == 'C':
            return 3
        if q == 'D':
            return 5
        if q == 'E':
            return 5
        if q == 'F':
            return 5
        else:
            return 0

    def get_Q14(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 3
        if q == 'D':
            return 4
        if q == 'E':
            return 5
        if q == 'F':
            return 6
        if q == 'G':
            return 7
        if q == 'H':
            return 8
        else:
            return 0

    def get_Q15(q):
        if q == 'A':
            return 7
        if q == 'B':
            return 6
        if q == 'C':
            return 5
        if q == 'D':
            return 4
        if q == 'E':
            return 3
        if q == 'F':
            return 2
        if q == 'G':
            return 1
        if q == 'H':
            return 0
        else:
            return 0

    def get_Q16(q):
        if q == 'A':
            return 1
        if q == 'B':
            return 1
        if q == 'C':
            return 2
        if q == 'D':
            return 7
        if q == 'E':
            return 5
        if q == 'F':
            return 4
        if q == 'G':
            return 4
        else:
            return 0

    def get_Q17(q):
        if q == 'A':
            return 1
        if q == 'B':
            return 0
        if q == 'C':
            return 2
        if q == 'D':
            return 3
        if q == 'E':
            return 4
        if q == 'F':
            return 5
        else:
            return 0

    def get_Q18(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 1
        if q == 'C':
            return 3
        if q == 'D':
            return 4
        if q == 'E':
            return 5
        else:
            return 0

    def get_Q19(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 1
        if q == 'D':
            return 2
        if q == 'E':
            return 3
        if q == 'F':
            return 4
        if q == 'G':
            return 5
        if q == 'H':
            return 7
        else:
            return 0

    def get_Q20(q):
        if q == 'A':
            return 3
        if q == 'B':
            return 7
        if q == 'C':
            return 5
        if q == 'D':
            return 2
        if q == 'E':
            return 1
        if q == 'F':
            return 0
        else:
            return 0

    def get_Q21(q):
        if q == 'A':
            return 7
        if q == 'B':
            return 6
        if q == 'C':
            return 5
        if q == 'D':
            return 3
        if q == 'E':
            return 0
        else:
            return 0


class Ready():

    @staticmethod
    def ready(answers):
        q1 = Ready.get_Q1(answers.Qone)
        q2 = Ready.get_Q2(answers.Qtwo)
        q3 = Ready.get_Q3(answers.Qthree)
        q4 = Ready.get_Q4(answers.Qfour)
        q5 = Ready.get_Q5(answers.Qfive)
        q6 = Ready.get_Q6(answers.Qsix)
        q7 = Ready.get_Q7(answers.Qseven)
        q8 = Ready.get_Q8(answers.Qeight)
        q9 = Ready.get_Q9(answers.Qnine)
        q10 = Ready.get_Q10(answers.Qten)
        q11 = Ready.get_Q11(answers.Qeleven)
        q12 = Ready.get_Q12(answers.Qtwelve)
        q13 = Ready.get_Q13(answers.Qthirteen)
        q14 = Ready.get_Q14(answers.Qfourteen)
        q15 = Ready.get_Q15(answers.Qfifteen)
        q16 = Ready.get_Q16(answers.Qsixteen)
        q17 = Ready.get_Q17(answers.Qseventeen)
        q18 = Ready.get_Q18(answers.Qeighteen)
        q19 = Ready.get_Q19(answers.Qnineteen)
        q20 = Ready.get_Q20(answers.Qtwenty)
        q21 = Ready.get_Q21(answers.Qtwentyone)
        ready_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21]
        suit_list = Suitability.suitability(answers)
        questions = QUESTIONS
        highest = HIGHEST_LIST_VALUE
        combined_dict = {
            question: {
                'suitability': suit,
                'v': ready
            }
            for question, suit, ready in zip(questions, suit_list, ready_list)
        }
        d_dict = {
            question: {
                'highest': high,
                'v': ready
            }
            for question, high, ready in zip(questions, highest, ready_list)
        }
        ready_score = sumproduct(combined_dict)
        deno = sumif(d_dict)
        return round(ready_score/deno*100)

    def get_Q1(q1):

        if q1 == 'A':
            return 0
        if q1 == 'B':
            return 0
        if q1 == 'C':
            return 0
        if q1 == 'D':
            return 0
        if q1 == 'E':
            return 0
        else:
            return 0

    def get_Q2(q2):

        if q2 == 'A':
            return 0
        if q2 == 'B':
            return 0
        if q2 == 'C':
            return 0
        if q2 == 'D':
            return 0
        if q2 == 'E':
            return 0
        else:
            return 0

    def get_Q3(q):

        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 0
        if q == 'D':
            return 0
        else:
            return 0

    def get_Q4(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 0
        if q == 'D':
            return 0
        if q == 'E':
            return 0
        if q == 'F':
            return 0
        if q == 'G':
            return 0
        if q == 'H':
            return 0
        if q == 'I':
            return 0
        if q == 'J':
            return 0
        if q == 'K':
            return 0
        else:
            return 0

    def get_Q5(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 0
        if q == 'D':
            return 0
        if q == 'E':
            return 0
        if q == 'F':
            return 0
        if q == 'G':
            return 0
        if q == 'H':
            return 0
        else:
            return 0

    def get_Q6(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 0
        if q == 'D':
            return 0
        if q == 'E':
            return 0
        if q == 'F':
            return 0
        if q == 'G':
            return 0
        if q == 'H':
            return 0
        if q == 'I':
            return 0
        if q == 'J':
            return 0
        else:
            return 0

    def get_Q7(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 0
        if q == 'D':
            return 0
        if q == 'E':
            return 0
        else:
            return 0

    def get_Q8(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 0
        if q == 'D':
            return 0
        if q == 'E':
            return 0
        if q == 'F':
            return 0
        else:
            return 0

    def get_Q9(q):
        if q == 'A':
            return 1
        if q == 'B':
            return 1
        if q == 'C':
            return 1
        if q == 'D':
            return 1
        if q == 'E':
            return 1
        else:
            return 0

    def get_Q10(q):
        if q == 'A':
            return 1
        if q == 'B':
            return 1
        if q == 'C':
            return 1
        if q == 'D':
            return 1
        else:
            return 0

    def get_Q11(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 0
        if q == 'D':
            return 0
        if q == 'E':
            return 0
        if q == 'F':
            return 0
        else:
            return 0

    def get_Q12(q):
        if q == 'A':
            return 1
        if q == 'B':
            return 1
        if q == 'C':
            return 1
        if q == 'D':
            return 1
        if q == 'E':
            return 1
        if q == 'F':
            return 1
        if q == 'G':
            return 1
        else:
            return 0

    def get_Q13(q):
        if q == 'A':
            return 1
        if q == 'B':
            return 1
        if q == 'C':
            return 1
        if q == 'D':
            return 1
        if q == 'E':
            return 1
        if q == 'F':
            return 1
        else:
            return 0

    def get_Q14(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 0
        if q == 'D':
            return 0
        if q == 'E':
            return 0
        if q == 'F':
            return 0
        if q == 'G':
            return 0
        if q == 'H':
            return 0
        else:
            return 0

    def get_Q15(q):
        if q == 'A':
            return 1
        if q == 'B':
            return 1
        if q == 'C':
            return 1
        if q == 'D':
            return 1
        if q == 'E':
            return 1
        if q == 'F':
            return 1
        if q == 'G':
            return 1
        if q == 'H':
            return 1
        else:
            return 0

    def get_Q16(q):
        if q == 'A':
            return 1
        else:
            return 0

    def get_Q17(q):
        if q == 'Z':
            return 0
        else:
            return 1

    def get_Q18(q):
        if q == 'Z':
            return 0
        else:
            return 1

    def get_Q19(q):
        if q == 'Z':
            return 0
        else:
            return 1

    def get_Q20(q):
        if q == 'Z':
            return 0
        else:
            return 1

    def get_Q21(q):
        if q == 'Z':
            return 0
        else:
            return 1


class Benefit():

    @staticmethod
    def benefit(answers):
        q1 = Benefit.get_Q1(answers.Qone)
        q2 = Benefit.get_Q2(answers.Qtwo)
        q3 = Benefit.get_Q3(answers.Qthree)
        q4 = Benefit.get_Q4(answers.Qfour)
        q5 = Benefit.get_Q5(answers.Qfive)
        q6 = Benefit.get_Q6(answers.Qsix)
        q7 = Benefit.get_Q7(answers.Qseven)
        q8 = Benefit.get_Q8(answers.Qeight)
        q9 = Benefit.get_Q9(answers.Qnine)
        q10 = Benefit.get_Q10(answers.Qten)
        q11 = Benefit.get_Q11(answers.Qeleven)
        q12 = Benefit.get_Q12(answers.Qtwelve)
        q13 = Benefit.get_Q13(answers.Qthirteen)
        q14 = Benefit.get_Q14(answers.Qfourteen)
        q15 = Benefit.get_Q15(answers.Qfifteen)
        q16 = Benefit.get_Q16(answers.Qsixteen)
        q17 = Benefit.get_Q17(answers.Qseventeen)
        q18 = Benefit.get_Q18(answers.Qeighteen)
        q19 = Benefit.get_Q19(answers.Qnineteen)
        q20 = Benefit.get_Q20(answers.Qtwenty)
        q21 = Benefit.get_Q21(answers.Qtwentyone)
        benefit_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21]
        suit_list = Suitability.suitability(answers)
        questions = QUESTIONS
        highest = HIGHEST_LIST_VALUE
        combined_dict = {
            question: {
                'suitability': suit,
                'v': benefit
            }
            for question, suit, benefit in zip(questions, suit_list, benefit_list)
        }
        d_dict = {
            question: {
                'highest': high,
                'v': benefit
            }
            for question, high, benefit in zip(questions, highest, benefit_list)
        }
        benefit_score = sumproduct(combined_dict)
        deno = sumif(d_dict)
        return round(benefit_score/deno*100)

    def get_Q1(q):
        if q == 'Z':
            return 0
        else:
            return 1

    def get_Q2(q):
        if q == 'Z':
            return 1
        else:
            return 0

    def get_Q3(q):
        if q == 'Z':
            return 0
        else:
            return 1

    def get_Q4(q):
        if q == 'Z':
            return 0
        else:
            return 1

    def get_Q5(q):
        if q == 'Z':
            return 0
        else:
            return 1

    def get_Q6(q):
        if q == 'Z':
            return 0
        else:
            return 1

    def get_Q7(q):
        if q == 'Z':
            return 1
        else:
            return 0

    def get_Q8(q):
        if q == 'Z':
            return 1
        else:
            return 0

    def get_Q9(q):
        if q == 'Z':
            return 0
        else:
            return 1

    def get_Q10(q):
        if q == 'Z':
            return 1
        else:
            return 0

    def get_Q11(q):
        if q == 'Z':
            return 1
        else:
            return 0

    def get_Q12(q):
        if q == 'Z':
            return 1
        else:
            return 0

    def get_Q13(q):
        if q == 'Z':
            return 1
        else:
            return 0

    def get_Q14(q):
        if q == 'Z':
            return 1
        else:
            return 0

    def get_Q15(q):
        if q == 'Z':
            return 1
        else:
            return 0

    def get_Q16(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q17(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q18(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q19(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q20(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q21(q):
        if q == 'Z':
            return 1
        else:
            return 1


class RPAVP():

    @staticmethod
    def rpa_vp(answers):
        q1 = RPAVP.get_Q1(answers.Qone)
        q2 = RPAVP.get_Q2(answers.Qtwo)
        q3 = RPAVP.get_Q3(answers.Qthree)
        q4 = RPAVP.get_Q4(answers.Qfour)
        q5 = RPAVP.get_Q5(answers.Qfive)
        q6 = RPAVP.get_Q6(answers.Qsix)
        q7 = RPAVP.get_Q7(answers.Qseven)
        q8 = RPAVP.get_Q8(answers.Qeight)
        q9 = RPAVP.get_Q9(answers.Qnine)
        q10 = RPAVP.get_Q10(answers.Qten)
        q11 = RPAVP.get_Q11(answers.Qeleven)
        q12 = RPAVP.get_Q12(answers.Qtwelve)
        q13 = RPAVP.get_Q13(answers.Qthirteen)
        q14 = RPAVP.get_Q14(answers.Qfourteen)
        q15 = RPAVP.get_Q15(answers.Qfifteen)
        q16 = RPAVP.get_Q16(answers.Qsixteen)
        q17 = RPAVP.get_Q17(answers.Qseventeen)
        q18 = RPAVP.get_Q18(answers.Qeighteen)
        q19 = RPAVP.get_Q19(answers.Qnineteen)
        q20 = RPAVP.get_Q20(answers.Qtwenty)
        q21 = RPAVP.get_Q21(answers.Qtwentyone)
        rpa_vp_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21]
        suit_list = Suitability.suitability(answers)
        questions = QUESTIONS
        highest = HIGHEST_LIST_VALUE
        combined_dict = {
            question: {
                'suitability': suit,
                'v': rpa
            }
            for question, suit, rpa in zip(questions, suit_list, rpa_vp_list)
        }
        d_dict = {
            question: {
                'highest': high,
                'v': rpa
            }
            for question, high, rpa in zip(questions, highest, rpa_vp_list)
        }
        rpa_score = sumproduct(combined_dict)
        deno = sumif(d_dict)
        return round(rpa_score/deno*100)

    def get_Q1(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q2(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q3(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q4(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q5(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q6(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q7(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q8(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q9(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q10(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q11(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q12(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q13(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q14(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q15(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q16(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 0
        else:
            return 1

    def get_Q17(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q18(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q19(q):
        if q == 'Z':
            return 1
        else:
            return 1

    def get_Q20(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q21(q):
        if q == 'Z':
            return 1
        else:
            return 1


class Blockers():

    @staticmethod
    def blockers(answers):
        q1 = Blockers.get_Q1(answers.Qone)
        q2 = Blockers.get_Q2(answers.Qtwo)
        q3 = Blockers.get_Q3(answers.Qthree)
        q4 = Blockers.get_Q4(answers.Qfour)
        q5 = Blockers.get_Q5(answers.Qfive)
        q6 = Blockers.get_Q6(answers.Qsix)
        q7 = Blockers.get_Q7(answers.Qseven)
        q8 = Blockers.get_Q8(answers.Qeight)
        q9 = Blockers.get_Q9(answers.Qnine)
        q10 = Blockers.get_Q10(answers.Qten)
        q11 = Blockers.get_Q11(answers.Qeleven)
        q12 = Blockers.get_Q12(answers.Qtwelve)
        q13 = Blockers.get_Q13(answers.Qthirteen)
        q14 = Blockers.get_Q14(answers.Qfourteen)
        q15 = Blockers.get_Q15(answers.Qfifteen)
        q16 = Blockers.get_Q16(answers.Qsixteen)
        q17 = Blockers.get_Q17(answers.Qseventeen)
        q18 = Blockers.get_Q18(answers.Qeighteen)
        q19 = Blockers.get_Q19(answers.Qnineteen)
        q20 = Blockers.get_Q20(answers.Qtwenty)
        q21 = Blockers.get_Q21(answers.Qtwentyone)
        blockers_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21]
        suit_list = Suitability.suitability(answers)
        questions = QUESTIONS
        highest = HIGHEST_LIST_VALUE
        combined_dict = {
            question: {
                'suitability': suit,
                'v': block
            }
            for question, suit, block in zip(questions, suit_list, blockers_list)
        }
        d_dict = {
            question: {
                'highest': high,
                'v': block
            }
            for question, high, block in zip(questions, highest, blockers_list)
        }
        block_score = sumproduct(combined_dict)
        deno = sumif(d_dict)
        return round(block_score/deno*100)

    def get_Q1(q):
        if q == 'B':
            return 1
        else:
            return 0

    def get_Q2(q):
        if q == 'A':
            return 0
        else:
            return 1

    def get_Q3(q):
        if q == 'A':
            return 1
        else:
            return 0

    def get_Q4(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q5(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q6(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q7(q):
        if q == 'D':
            return 1
        else:
            return 0

    def get_Q8(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q9(q):
        if q == 'C':
            return 1
        else:
            return 0

    def get_Q10(q):
        if q == 'C':
            return 1
        if q == 'D':
            return 1
        else:
            return 0

    def get_Q11(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q12(q):
        if q == 'B':
            return 1
        if q == 'D':
            return 1
        else:
            return 0

    def get_Q13(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q14(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q15(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q16(q):
        if q == 'A':
            return 0
        if q == 'B':
            return 0
        if q == 'C':
            return 0
        else:
            return 0

    def get_Q17(q):
        if q == 'A':
            return 1
        else:
            return 0

    def get_Q18(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q19(q):
        if q == 'B':
            return 1
        else:
            return 0

    def get_Q20(q):
        if q == 'D':
            return 1
        else:
            return 0

    def get_Q21(q):
        if q == 'Z':
            return 0
        else:
            return 0

class HumanInputs():

    @staticmethod
    def inputs(answers):
        q1 = HumanInputs.get_Q1(answers.Qone)
        q2 = HumanInputs.get_Q2(answers.Qtwo)
        q3 = HumanInputs.get_Q3(answers.Qthree)
        q4 = HumanInputs.get_Q4(answers.Qfour)
        q5 = HumanInputs.get_Q5(answers.Qfive)
        q6 = HumanInputs.get_Q6(answers.Qsix)
        q7 = HumanInputs.get_Q7(answers.Qseven)
        q8 = HumanInputs.get_Q8(answers.Qeight)
        q9 = HumanInputs.get_Q9(answers.Qnine)
        q10 = HumanInputs.get_Q10(answers.Qten)
        q11 = HumanInputs.get_Q11(answers.Qeleven)
        q12 = HumanInputs.get_Q12(answers.Qtwelve)
        q13 = HumanInputs.get_Q13(answers.Qthirteen)
        q14 = HumanInputs.get_Q14(answers.Qfourteen)
        q15 = HumanInputs.get_Q15(answers.Qfifteen)
        q16 = HumanInputs.get_Q16(answers.Qsixteen)
        q17 = HumanInputs.get_Q17(answers.Qseventeen)
        q18 = HumanInputs.get_Q18(answers.Qeighteen)
        q19 = HumanInputs.get_Q19(answers.Qnineteen)
        q20 = HumanInputs.get_Q20(answers.Qtwenty)
        q21 = HumanInputs.get_Q21(answers.Qtwentyone)
        human_input_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21]
        suit_list = Suitability.suitability(answers)
        questions = QUESTIONS
        highest = HIGHEST_LIST_VALUE
        combined_dict = {
            question: {
                'suitability': suit,
                'v': human
            }
            for question, suit, human in zip(questions, suit_list, human_input_list)
        }
        d_dict = {
            question: {
                'highest': high,
                'v': human
            }
            for question, high, human in zip(questions, highest, human_input_list)
        }
        human_input_score = sumproduct(combined_dict)
        deno = sumif(d_dict)
        return round(human_input_score/deno*100)

    def get_Q1(q):
        if q == 'A':
            return 1
        else:
            return 0

    def get_Q2(q):
        if q == 'E':
            return 0
        else:
            return 1

    def get_Q3(q):
        if q == 'A':
            return 0
        else:
            return 0

    def get_Q4(q):
        if q == 'A':
            return 1
        else:
            return 0

    def get_Q5(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q6(q):
        if q == 'A':
            return 1
        else:
            return 0

    def get_Q7(q):
        if q == 'E':
            return 1
        else:
            return 0

    def get_Q8(q):
        if q == 'A':
            return 1
        else:
            return 0

    def get_Q9(q):
        if q == 'A':
            return 1
        else:
            return 0

    def get_Q10(q):
        if q == 'D':
            return 1
        else:
            return 0

    def get_Q11(q):
        if q == 'Z':
            return 0
        else:
            return 0

    def get_Q12(q):
        if q == 'A':
            return 1
        if q == 'D':
            return 1
        if q == 'C':
            return 1
        else:
            return 0

    def get_Q13(q):
        if q == 'E':
            return 0
        if q == 'F':
            return 0
        else:
            return 1

    def get_Q14(q):
        if q == 'A':
            return 1
        if q == 'B':
            return 1
        else:
            return 0

    def get_Q15(q):
        if q == 'H':
            return 1
        else:
            return 0

    def get_Q16(q):
        if q == 'A':
            return 1
        if q == 'B':
            return 1
        else:
            return 0

    def get_Q17(q):
        if q == 'B':
            return 1
        else:
            return 0

    def get_Q18(q):
        if q == 'A':
            return 1
        else:
            return 0

    def get_Q19(q):
        if q == 'B':
            return 1
        if q == 'A':
            return 1
        if q == 'C':
            return 1
        else:
            return 0

    def get_Q20(q):
        if q == 'E':
            return 1
        if q == 'F':
            return 1
        if q == 'C':
            return 1
        else:
            return 0

    def get_Q21(q):
        if q == 'E':
            return 1
        else:
            return 0


def sumproduct(data_dict):
    return sum(
        value['suitability'] * value['v']
        for value in data_dict.values()
    )

def sumif(data_dict):
    return sum(
        value['highest']
        for value in data_dict.values()
        if value['v'] == 1
    )
