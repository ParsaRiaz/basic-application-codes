import time
import random as r

def mistakes(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except IndexError:
            error += 1
    return error

def speed(time_s, time_e, userinput):
    time_delay = (time_e - time_s) / 60  # Convert time to minutes
    time_R = round(time_delay, 2)
    speed = userinput / time_R
    return round(speed)

test = [
    "Medical transcription, also known as MT, is an allied health profession dealing with the process of transcribing voice-recorded medical reports that are dictated by physicians, nurses and other healthcare practitioners. Medical reports can be voice files, notes taken during a lecture, or other spoken material. These are dictated over the phone or uploaded digitally via the Internet or through smart phone apps.",
    "Words per minute (WPM) is a measure of typing speed, commonly used in recruitment. For the purposes of WPM measurement a word is standardized to five characters or keystrokes. Therefore, 'brown' counts as one word, but 'accounted' counts as two. The benefits of a standardized measurement of input speed are that it enables comparison across language and hardware boundaries. The speed of an Afrikaans-speaking operator in Cape Town can be compared with a French-speaking operator in Paris.",
    "While academic success is important, it's equally important to prioritize your well-being. Taking care of your physical and mental health is essential for optimal academic performance. This includes getting enough sleep, eating nutritious meals, exercising regularly, and managing stress effectively. Taking breaks from studying to relax and recharge can actually improve your focus and productivity. Don't neglect your social life and hobbies; these activities can provide a much-needed outlet for stress and help you maintain a healthy balance between academics and personal life.",
    "A diverse team, one that encompasses individuals with different backgrounds, experiences, and perspectives, is a rich source of creativity and innovation. When people from different walks of life come together, they bring a wide range of ideas, skills, and knowledge to the table. This diversity can lead to more creative problem-solving, better decision-making, and a deeper understanding of complex issues. Embracing diversity within a team requires an inclusive and respectful environment where everyone feels valued and empowered to contribute their unique strengths.",
    "Web designers are expected to have an awareness of usability and if their role involves creating mark up then they are also expected to be up to date with web accessibility guidelines. The different areas of web design include web graphic design; interface design; authoring, including standardised code and proprietary software; user experience design; and search engine optimization.",
    "While academic success is important, it's equally important to prioritize your well-being. Taking care of your physical and mental health is essential for optimal academic performance. This includes getting enough sleep, eating nutritious meals, exercising regularly, and managing stress effectively. Taking breaks from studying to relax and recharge can actually improve your focus and productivity. Don't neglect your social life and hobbies; these activities can provide a much-needed outlet for stress and help you maintain a healthy balance between academics and personal life."
]

test1 = r.choice(test)

print("--------------Welcome to the typing speed calculator!--------------")
print()
print(test1)
print()
print()
time1 = time.time()
test_input = input("Enter: ")
time2 = time.time()

def split_and_combine(test_input):
    combined_letters = ""
    for char in test_input:
        if char != " ":
            combined_letters += char
    return combined_letters

result = split_and_combine(test_input)

print('Speed:', speed(time1, time2, len(result)), 'WPM')
print('Error:', mistakes(test1, test_input))
