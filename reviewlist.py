# Customer review data exactly as shown in the screenshots
authors = [
    "Саодат М",
    "Эля",
    "",
    "Тургун Миноваров",
    "Евгения К.",
    "Адиль",
]

ratings = [5, 5, 5, 4, 1, 5]

dates = [
    "19 июля 2025",
    "4 декабря 2025",
    "5 дней назад",
    "9 января",
    "22 марта 2025",
    "16 декабря 2024",
]

comments = [
    (
        "Мне очень понравились блюда Хорезмской кухни , обслуживание на"
        " высшем уровне, блюда свежего приготовления, мясные блюда"
        " приготовлены мягко , без какого либо изъяна👏"
    ),
    """сервис 5/5 - быстрая подача
еда 4/5 - плов отличный, но тухум борак не сильно зашел
атмосфера 5/5 - спокойно, фоновая легкая музыка""",
    (
        "Часто бываю очень хороший плов в Ташкенте именно национальная"
        " хорезмская кухня"
    ),
    (
        "Был несколько раз, всё время разное качество приготовления,"
        " обслуживание немного долгое, цены не дешёвые"
    ),
    (
        "Не могу оценить кухню, так как не удалось сделать заказ."
        " Обслуживание на нуле. За столик посадить посадили, а обслужить не"
        " удосужились. Просидели минут 20, никто так и не подошел."
        " Развернулись и ушли"
    ),
    (
        "Самая лучшая хорезмская кухня в городе, очень вкусно, прекрасное"
        " обслуживание"
    ),
]

# Empty list to store responses for each review
responses = ["", "", "", "", "", ""]

while True:
    print("\n==================================================")
    print("         CUSTOMER REVIEW LIST (Khanate)")
    print("==================================================")

    # Display all reviews one by one
    for i in range(len(comments)):
        if authors[i] != "":
            print(str(i + 1) + ".", authors[i])
        else:
            print(str(i + 1) + ".")

        print("    Rating:", ratings[i], "| Date:", dates[i])

        # Split long comments so every line fits neatly inside 50 characters
        lines = comments[i].split("\n")
        for line in lines:
            words = line.split(" ")
            current_line = ""
            for word in words:
                if current_line == "":
                    current_line = word
                elif len(current_line) + len(word) + 1 <= 46:
                    current_line = current_line + " " + word
                else:
                    print("   ", current_line)
                    current_line = word
            if current_line != "":
                print("   ", current_line)

        # Show the response if one has been added
        if responses[i] != "":
            print("    -> Response:", responses[i])

        print("--------------------------------------------------")

    print("1. Respond")
    print("0. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        review_number = int(input("Enter the review number to respond to: "))

        if review_number >= 1 and review_number <= len(comments):
            reply_text = input("Enter your response: ")
            responses[review_number - 1] = reply_text
            print("Response added successfully!")
        else:
            print("Invalid review number!")

    elif choice == "0":
        print("Exited the review section.")
        break

    else:
        print("Invalid choice! Please enter 1 or 0.")