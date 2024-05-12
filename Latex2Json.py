import re
import json

def parse_questions(text):
    questions = []

    # Split the text into individual questions
    question_texts = re.split(r'\n{0,2}Question ID: (\d+)\n{1,2}', text)[1:]
    # If the number of elements in question_texts is odd, append an empty string
    if len(question_texts) % 2 != 0:
        question_texts.append("")

    for i in range(0, len(question_texts), 2):
        question_data = {}

        # Extract question number and ID
        question_data["questionNumber"] = i // 2 + 1
        question_data["questionId"] = int(question_texts[i])
        # Extract question body
        match = re.search(r'If (.+?)(?=Answer)|The (.+?)(?=Answer)', question_texts[i + 1], re.DOTALL)
        print(match)
        if match:
            question_data["questionText"] = match.group(0).strip()
        else:
            continue
        # Extract options and correct answer
        options = re.findall(r'\(([A-D])\) (.+?)\n', question_texts[i + 1])
        correct_answer = re.search(r'Answer \(([A-D])\)', question_texts[i + 1]).group(1)

        question_data["options"] = [{"optionNumber": ord(option[0]) - 64, "optionText": option[1], "isCorrect": option[0] == correct_answer} for option in options]

        # Extract solution body
        solution_text_match = re.search(r'Sol\. (.+?)(?=Question ID|\Z)', question_texts[i + 1], re.DOTALL)
        if solution_text_match:
            question_data["solutionText"] = solution_text_match.group(1).strip()
        else:
            question_data["solutionText"] = ""

        questions.append(question_data)

    return questions

# Example text
text = """
{Choose the correct answer :}

Question ID: 481221

If $\Delta=\left|\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right|$ and $A_{i j}$ is co-factor of $a_{i j}$, then

value of $\Delta$ is equal to

(A) $a_{11} A_{31}+a_{12} A_{32}+a_{13} A_{33}$

(B) $a_{11} A_{11}+a_{12} A_{21}+a_{13} A_{31}$

(C) $a_{21} A_{11}+a_{22} A_{12}+a_{23} A_{13}$

(D) $a_{11} A_{11}+a_{21} A_{21}+a_{31} A_{31}$

Answer (D)

Sol. $\Delta=a_{11} A_{11}+a_{21} A_{21}+a_{31} A_{31}$

Question ID: 481222

If the matrix $\left[\begin{array}{ccc}0 & -1 & 3 x \\ 1 & y & -5 \\ -6 & 5 & 0\end{array}\right]$ is skew symmetric, then

$6 x+y$ is equal to

(A) 6

(B) 12

(C) 18

(D) 2

Answer (B)

Sol. $y=0$ and $3 x=6$

So, $6 x+y=12$

Question ID: 481223

If $\left|\begin{array}{cc}3 & -4 \\ 2 & 1\end{array}\right|=\left|\begin{array}{cc}2 x & 5 \\ 1 & x\end{array}\right|$ then $|x|$ is equal to
(A) $\sqrt{\frac{5}{2}}$
(B) 4
(C) $2 \sqrt{2}$
(D) 2

Answer (C)

Sol. $\left|\begin{array}{cc}3 & -4 \\ 2 & 1\end{array}\right|=\left|\begin{array}{cc}2 x & 5 \\ 1 & x\end{array}\right|$

$\Rightarrow 11=2 x^{2}-5$

$\Rightarrow x^{2}=8$

$\Rightarrow|x|=2 \sqrt{2}$

Question ID: 481224

Which of the following statements are true?

A. A square matrix $A$ is said to be non-singular if $|A|=0$

B. A square matrix $A$ is invertible if and only if $A$ is non-singular matrix.

C. If elements of a row are multiplied with cofactors of any other row, then their sum is zero.
D. $A$ is square matrix of order 3 then $|A d j .(A)|$ $=|A|^{3}$

Choose the correct answer from the options given below
(A) A and C only
(B) B and C only
(C) C and D only
(D) B and D only

Answer (B)

Sol. Statement $A$ is incorrect as for singular matrices $|A|=0$

Statement $B$ is correct as $A$ is invertible if $|A| \neq 0$

Statement $C$ is correct

Statement $D$ is incorrect as $|A d j(A)|=|A|^{2}$

Question ID: 481225

The interval in which $y=x^{2} e^{2 x}$ is increasing is

(A) $(-\infty,-1)$

(B) $(-1, \infty)$

(C) $(-\infty,-1) \cup(0, \infty)$

(D) $(-\infty, 0) \cup(1, \infty)$

Answer (C)

Sol. $\frac{d y}{d x}=x^{2} \cdot 2 e^{2 x}+2 x \cdot e^{2 x}=2 x e^{2 x}(x+1)$

$\frac{d y}{d x}>0$ for $x \in(-\infty,-1) \cup(0, \infty)$

Question ID: 481226

If $x=t^{3}, y=t^{4}$ then $\frac{d^{2} y}{d x^{2}}$ at $t=2$ is
(A) $\frac{8}{3}$
(B) $\frac{1}{9}$
(C) $\frac{2}{9}$
(D) $\frac{9}{16}$

Answer (B)


"""

# Parse the text
parsed_questions = parse_questions(text)
# Convert to JSON format
json_output = json.dumps(parsed_questions, indent=2)
print(json_output)

with open(f'output.json', 'w') as fp:
            json.dump(parsed_questions, fp, indent=1,ensure_ascii=False)