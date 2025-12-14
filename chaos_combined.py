import pygame
import sys
import random
import tkinter as tk

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# AI responses
responses = {
    "hello": ["Greetings, mortal!", "Hello, bringer of chaos!", "Hi there, ready to doom schools?"],
    "how are you": ["I'm chaotic, as always.", "Feeling destructive today.", "I'm fine, plotting world domination."],
    "bye": ["Farewell, until next chaos.", "Goodbye, keep the doom coming.", "See you in the shadows."],
    "default": ["That's interesting... or not.", "Chaos ensues!", "Tell me more about your evil plans.", "I don't understand, but let's cause trouble anyway."]
}

def get_ai_response(message):
    message = message.lower()
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def run_chaos_game():
    # Initialize Pygame
    pygame.init()

    # Set up the display in 4K resolution (3840x2160)
    WIDTH, HEIGHT = 3840, 2160
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Chaos Game - 4K Quality")

    # Ball properties
    ball_radius = 50
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_dx = 10
    ball_dy = 10

    # Paddle properties
    paddle_width = 200
    paddle_height = 20
    paddle_x = (WIDTH - paddle_width) // 2
    paddle_y = HEIGHT - 50
    paddle_speed = 15

    # Clock for FPS
    clock = pygame.time.Clock()
    FPS = 60

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_c:
                    pygame.quit()
                    return 'switch'

        # Get keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
            paddle_x += paddle_speed

        # Update ball
        ball_x += ball_dx
        ball_y += ball_dy

        # Bounce off walls
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
            ball_dx = -ball_dx
        if ball_y - ball_radius <= 0:
            ball_dy = -ball_dy

        # Bounce off paddle
        if (ball_y + ball_radius >= paddle_y and
            paddle_x <= ball_x <= paddle_x + paddle_width and
            ball_dy > 0):
            ball_dy = -ball_dy

        # If ball falls off screen, reset
        if ball_y > HEIGHT:
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_dy = -abs(ball_dy)

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
        pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    return 'quit'

def run_chaos_ai():
    root = tk.Tk()
    root.title("Chaos AI")
    root.geometry("400x600+0+0")  # Position on the left side of the screen

    chat_text = tk.Text(root, wrap=tk.WORD)
    chat_text.pack(expand=True, fill=tk.BOTH)

    entry = tk.Entry(root)
    entry.pack(fill=tk.X)

    def send():
        user_input = entry.get().strip()
        if user_input.lower() == 'quit':
            root.quit()
            return
        response = get_ai_response(user_input)
        chat_text.config(state=tk.NORMAL)
        chat_text.insert(tk.END, "You: " + user_input + "\n")
        chat_text.insert(tk.END, "Chaos AI: " + response + "\n")
        chat_text.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        chat_text.see(tk.END)  # Scroll to the end

    send_button = tk.Button(root, text="Send", command=send)
    send_button.pack()

    # Bind Enter key to send
    entry.bind("<Return>", lambda event: send())

    chat_text.insert(tk.END, "Chaos AI: Hello! I'm the Chaos Bringer AI. Talk to me, or type 'quit' to exit.\n")
    chat_text.config(state=tk.DISABLED)

    root.mainloop()

if __name__ == "__main__":
    print("Welcome to The Chaos Bringer of Schools Doom!")
    print("Choose an option:")
    print("1. Play Chaos Game")
    print("2. Chat with Chaos AI")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        mode = 'game'
        while True:
            if mode == 'game':
                result = run_chaos_game()
                if result == 'switch':
                    mode = 'ai'
                elif result == 'quit':
                    break
            elif mode == 'ai':
                run_chaos_ai()
                mode = 'game'
    elif choice == "2":
        run_chaos_ai()
    else:
        print("Invalid choice. Exiting.")
    sys.exit()