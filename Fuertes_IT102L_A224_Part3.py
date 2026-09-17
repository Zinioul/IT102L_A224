# Christina Francesca T. Fuertes
# IT102-L - A224
# Exam Part 3
# YUNA - An Interactive Classroom Survey Game for Resource-Constrained Schools

class Teacher:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.games = []

class Question:
    def __init__(self, text, topic):
        self.text = text
        self.topic = topic
        self.answers = []  # List of tuples: (answer_text, points)
    
    def add_answer(self, text, points):
        self.answers.append((text, points))

class Game:
    def __init__(self, title, created_by):
        self.title = title
        self.created_by = created_by
        self.questions = []
    
    def add_question(self, question):
        self.questions.append(question)

# MAIN APPLICATION CONTROLLER
class YUNAapp:
    def __init__(self):
        self.current_teacher = None
        self.demo_teacher = Teacher("Ms. Christina Fuertes", "teacher@school.edu", "password123")
        self.run()

    def run(self):
        while True:
            if not self.current_teacher:
                self.show_login_screen()
            else:
                self.show_dashboard()

    def print_header(self, title):
        print("\n" + "=" * 50)
        print(f"📱 YUNA: Interactive Classroom Survey Game - {title}")
        print("=" * 50)

    def show_login_screen(self):
        self.print_header("Login")
        email = input("Email (Default: teacher@school.edu): ") or "teacher@school.edu"
        password = input("Password (Default: password123): ") or "password123"

        if email == self.demo_teacher.email and password == self.demo_teacher.password:
            self.current_teacher = self.demo_teacher
            print(f"\n[SUCCESS] Welcome, {self.current_teacher.name}!")
        else:
            print("\n[ERROR] Invalid credentials! Try again.")

    def show_dashboard(self):
        self.print_header("Dashboard")
        print(f"Logged in as: {self.current_teacher.name}")
        print("1. ➕ Create New Game")
        print("2. 📚 Browse Games")
        print("3. 🚪 Logout")
        
        choice = input("\nSelect an option (1-3): ")
        if choice == "1":
            self.show_create_game()
        elif choice == "2":
            self.show_game_library()
        elif choice == "3":
            self.current_teacher = None
            print("\n[INFO] Logged out successfully.")
        else:
            print("\n[ERROR] Invalid choice.")

    def show_create_game(self):
        self.print_header("Create New Game")
        title = input("Game Title (Default: US History - Civil War): ") or "US History - Civil War"
        topic = input("Topic (Default: History): ") or "History"

        new_game = Game(title, self.current_teacher.name)
        
        # Inject sample questions
        q1 = Question("What year did the Civil War begin?", topic)
        q1.add_answer("1861", 25)
        q1.add_answer("1860", 20)
        q1.add_answer("1865", 15)
        new_game.add_question(q1)
        
        q2 = Question("Name a Confederate state.", topic)
        q2.add_answer("Texas", 30)
        q2.add_answer("Virginia", 25)
        q2.add_answer("Georgia", 20)
        new_game.add_question(q2)
        
        self.current_teacher.games.append(new_game)
        print(f"\n[SUCCESS] Game '{title}' created and saved to library!")

    def show_game_library(self):
        self.print_header("Game Library")
        games = self.current_teacher.games
        
        if not games:
            print("No games created yet.")
        else:
            for idx, game in enumerate(games, 1):
                print(f"{idx}. {game.title} (Topic: {game.questions[0].topic if game.questions else 'N/A'})")
                print(f"   Questions count: {len(game.questions)}")
        
        input("\nPress Enter to return to Dashboard...")

# Start the application
if __name__ == "__main__":
    YUNAapp()