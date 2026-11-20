import json


class ReviewList:
    def __init__(self):
        self.file_name = "responses.json"
        self.reviews = [
            {
                "author": "Саодат М",
                "rating": 5,
                "date": "19 июля 2025",
                "comment": (
                    "Мне очень понравились блюда Хорезмской кухни , обслуживание на"
                    " высшем уровне, блюда свежего приготовления, мясные блюда"
                    " приготовлены мягко , без какого либо изъяна👏"
                ),
                "response": "",
            },
            {
                "author": "Эля",
                "rating": 5,
                "date": "4 декабря 2025",
                "comment": (
                    "сервис 5/5 - быстрая подача\n"
                    "еда 4/5 - плов отличный, но тухум борак не сильно зашел\n"
                    "атмосфера 5/5 - спокойно, фоновая легкая музыка"
                ),
                "response": "",
            },
            {
                "author": "",
                "rating": 5,
                "date": "5 дней назад",
                "comment": (
                    "Часто бываю очень хороший плов в Ташкенте именно национальная"
                    " хорезмская кухня"
                ),
                "response": "",
            },
            {
                "author": "Тургун Миноваров",
                "rating": 4,
                "date": "9 января",
                "comment": (
                    "Был несколько раз, всё время разное качество приготовления,"
                    " обслуживание немного долгое, цены не дешёвые"
                ),
                "response": "",
            },
            {
                "author": "Евгения К.",
                "rating": 1,
                "date": "22 марта 2025",
                "comment": (
                    "Не могу оценить кухню, так как не удалось сделать заказ."
                    " Обслуживание на нуле. За столик посадить посадили, а обслужить не"
                    " удосужились. Просидели минут 20, никто так и не подошел."
                    " Развернулись и ушли"
                ),
                "response": "",
            },
            {
                "author": "Адиль",
                "rating": 5,
                "date": "16 декабря 2024",
                "comment": (
                    "Самая лучшая хорезмская кухня в городе, очень вкусно, прекрасное"
                    " обслуживание"
                ),
                "response": "",
            },
        ]
        self.load_responses()

    def load_responses(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                for saved in data:
                    for item in self.reviews:
                        if (
                            item["author"] == saved["author"]
                            and item["date"] == saved["date"]
                            and item["comment"] == saved["comment"]
                        ):
                            item["response"] = saved["response"]
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def save_responses(self):
        responses = []
        for item in self.reviews:
            if item["response"] != "":
                responses.append(item)

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(responses, file, ensure_ascii=False, indent=4)

    def show_reviews(self):
        self.load_responses()
        if not self.reviews:
            print("No reviews yet.")
            print()
            return

        print("==================================================")
        print("         CUSTOMER REVIEW LIST (Khanate)")
        print("==================================================")

        for i, item in enumerate(self.reviews, start=1):
            if item["author"] != "":
                print(f"{i}. {item['author']}")
            else:
                print(f"{i}.")

            print(f"    Rating: {item['rating']} | Date: {item['date']}")

            lines = item["comment"].split("\n")
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

            if item["response"] != "":
                print(f"    -> Response: {item['response']}")

            print("--------------------------------------------------")
        print()

    def respond_menu(self):
        self.show_reviews()
        try:
            review_number = int(input("Enter the review number to respond to: "))
        except ValueError:
            print("Please enter a valid number!")
            print()
            return

        if 1 <= review_number <= len(self.reviews):
            reply_text = input("Enter your response: ")
            self.load_responses()
            self.reviews[review_number - 1]["response"] = reply_text
            self.save_responses()
            print("Response added successfully!")
            print()
        else:
            print("Invalid review number!")
            print()

    def show_responses(self):
        self.load_responses()
        has_response = False
        for item in self.reviews:
            if item["response"] != "":
                has_response = True
                break

        if not has_response:
            print("No responses yet.")
            print()
            return

        print("==================================================")
        print("           CUSTOMER RESPONSES (Khanate)")
        print("==================================================")

        for i, item in enumerate(self.reviews, start=1):
            if item["response"] != "":
                if item["author"] != "":
                    print(f"{i}. {item['author']}")
                else:
                    print(f"{i}.")

                print(f"    Rating: {item['rating']} | Date: {item['date']}")
                print("    Response:")

                lines = item["response"].split("\n")
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

                print("--------------------------------------------------")
        print()

    def choice(self):
        while True:
            print("1. Show Reviews")
            print("2. Respond to Review")
            print("3. Show Responses")
            print("0. Exit")
            try:
                c = int(input("Choose option 0-3: "))
            except ValueError:
                print("Please enter a number (0-3)")
                print()
                continue
            print()

            if c == 1:
                self.show_reviews()
            elif c == 2:
                self.respond_menu()
            elif c == 3:
                self.show_responses()
            elif c == 0:
                break
            else:
                print("Only 4 options (0-3)")
                print()


if __name__ == "__main__":
    app = ReviewList()
    app.choice()