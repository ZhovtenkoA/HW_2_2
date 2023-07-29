from Bot import Bot
from visualization import MyView

if __name__ == "__main__":
    bot = Bot()
    view = MyView()
    bot.book.load("auto_save")
    view.display_hello()
    while True:
        bot.book.load("auto_save")
        action = (
            input("Type help for list of commands or enter your command\n")
            .strip()
            .lower()
        )
        if action:
            if action == "help":
                view.display_commands()
                action = input().strip().lower()
                bot.handle(action)
                if action in ["add", "remove", "edit"]:
                    bot.book.save("auto_save")
            else:
                bot.handle(action)
                if action in ["add", "remove", "edit"]:
                    bot.book.save("auto_save")
            if action == "exit":
                view.display_bye()
                break
        else:
            print("No input provided. Please enter a command.")
