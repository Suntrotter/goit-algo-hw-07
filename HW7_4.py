class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "This comment has been deleted."
        self.is_deleted = True

    def display(self, indent=0):
        if not self.is_deleted:
            print("  " * indent + f"{self.author}: {self.text}")
            for reply in self.replies:
                reply.display(indent + 1)


# Example usage:
root_comment = Comment("What a wonderful book!", "Bod")
reply1 = Comment("This book is a disappointment :(", "Andrew")
reply2 = Comment("What's so great about it?", "Marina")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("It's not a book, it's a bunch of paper translated into nothing...", "Sergei")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
