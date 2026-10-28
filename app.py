import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boba the Cute Virtual Pet 🐾✨")

# Colors
PASTEL_PINK = (255, 218, 224)
PASTEL_BLUE = (200, 230, 255)
PASTEL_YELLOW = (255, 250, 205)
PASTEL_GREEN = (210, 245, 210)
WHITE = (255, 255, 255)
DARK_GRAY = (60, 60, 60)
BROWN = (180, 110, 60)
LIGHT_BROWN = (220, 160, 110)
PINK = (255, 150, 170)
GOLD = (255, 200, 50)
NIGHT_BG = (40, 40, 70)

# Clock
clock = pygame.time.Clock()

# Fonts
font_title = pygame.font.SysFont("comicsansms", 32, bold=True)
font_btn = pygame.font.SysFont("comicsansms", 18, bold=True)
font_ui = pygame.font.SysFont("comicsansms", 20)

# Pet Stats (Max 100)
stats = {
    "Hunger": 70,
    "Happiness": 80,
    "Energy": 90,
    "Cleanliness": 85
}

is_sleeping = False
message = "Boba is happy to see you! 💕"

# UI Buttons
buttons = [
    {"label": "🍎 Feed", "x": 60, "y": 480, "action": "feed", "color": (255, 140, 140)},
    {"label": "🎾 Play", "x": 230, "y": 480, "action": "play", "color": (140, 200, 255)},
    {"label": "🧼 Bath", "x": 400, "y": 480, "action": "clean", "color": (160, 240, 200)},
    {"label": "😴 Sleep", "x": 570, "y": 480, "action": "sleep", "color": (210, 170, 240)}
]

def draw_pet():
    # Tail animation wiggling
    tail_y = 350
    pygame.draw.ellipse(screen, BROWN, (480, tail_y, 40, 20))

    # Body
    pygame.draw.ellipse(screen, LIGHT_BROWN, (310, 280, 180, 140))
    # Belly
    pygame.draw.ellipse(screen, WHITE, (340, 310, 120, 90))

    # Paws
    pygame.draw.ellipse(screen, BROWN, (325, 390, 40, 30))
    pygame.draw.ellipse(screen, BROWN, (435, 390, 40, 30))

    # Head
    pygame.draw.circle(screen, LIGHT_BROWN, (400, 230), 80)
    pygame.draw.circle(screen, WHITE, (400, 245), 40)  # Snout area

    # Ears
    pygame.draw.ellipse(screen, BROWN, (300, 160, 45, 90))  # Left Ear
    pygame.draw.ellipse(screen, BROWN, (455, 160, 45, 90))  # Right Ear

    # Nose
    pygame.draw.ellipse(screen, DARK_GRAY, (390, 225, 20, 14))

    # Eyes
    if is_sleeping:
        # Sleeping eyes (curved lines)
        pygame.draw.arc(screen, DARK_GRAY, (360, 205, 25, 20), 3.14, 0, 3)
        pygame.draw.arc(screen, DARK_GRAY, (415, 205, 25, 20), 3.14, 0, 3)
    else:
        # Open shiny eyes
        pygame.draw.circle(screen, DARK_GRAY, (370, 210), 12)
        pygame.draw.circle(screen, DARK_GRAY, (430, 210), 12)
        # Eye shine
        pygame.draw.circle(screen, WHITE, (366, 206), 4)
        pygame.draw.circle(screen, WHITE, (426, 206), 4)

    # Blush cheeks
    pygame.draw.circle(screen, PINK, (345, 235), 12)
    pygame.draw.circle(screen, PINK, (455, 235), 12)

    # Mouth / Smile
    if not is_sleeping:
        pygame.draw.arc(screen, DARK_GRAY, (385, 235, 15, 15), 3.14, 0, 2)
        pygame.draw.arc(screen, DARK_GRAY, (400, 235, 15, 15), 3.14, 0, 2)

    # Sleeping Zzz
    if is_sleeping:
        zzz = font_title.render("Z z z...", True, WHITE)
        screen.blit(zzz, (490, 140))

def draw_stat_bar(name, value, x, y):
    # Label
    txt = font_ui.render(f"{name}:", True, DARK_GRAY)
    screen.blit(txt, (x, y))

    # Outer Bar
    pygame.draw.rect(screen, WHITE, (x + 130, y + 5, 150, 20), border_radius=10)
    # Fill Bar
    fill_width = int((value / 100) * 150)
    bar_color = PASTEL_GREEN if value > 50 else (255, 180, 100) if value > 20 else (255, 100, 100)
    if fill_width > 0:
        pygame.draw.rect(screen, bar_color, (x + 130, y + 5, fill_width, 20), border_radius=10)

    # Percentage Text
    pct = font_ui.render(f"{int(value)}%", True, DARK_GRAY)
    screen.blit(pct, (x + 290, y))

# Stat decrease timer event
STAT_DECAY = pygame.USEREVENT + 1
pygame.time.set_timer(STAT_DECAY, 3000)  # Every 3 seconds

# Game Loop
running = True
while running:
    # Change background depending on sleeping state
    bg_color = NIGHT_BG if is_sleeping else PASTEL_PINK
    screen.fill(bg_color)

    # Header Banner
    pygame.draw.rect(screen, WHITE if not is_sleeping else (60, 60, 90), (0, 0, WIDTH, 70))
    title_color = DARK_GRAY if not is_sleeping else WHITE
    title_txt = font_title.render("🐾 Boba's Virtual Pet Care 🐾", True, title_color)
    screen.blit(title_txt, (WIDTH // 2 - title_txt.get_width() // 2, 15))

    # Draw Pet Room
    floor_color = (60, 50, 80) if is_sleeping else PASTEL_YELLOW
    pygame.draw.rect(screen, floor_color, (0, 420, WIDTH, 180))

    # Draw Pet
    draw_pet()

    # Draw Status Panel (Top Left / Right)
    draw_stat_bar("Hunger", stats["Hunger"], 40, 90)
    draw_stat_bar("Happiness", stats["Happiness"], 40, 125)
    draw_stat_bar("Energy", stats["Energy"], 430, 90)
    draw_stat_bar("Cleanliness", stats["Cleanliness"], 430, 125)

    # Draw Message Box
    pygame.draw.rect(screen, WHITE, (100, 430, 600, 35), border_radius=10)
    msg_txt = font_ui.render(message, True, DARK_GRAY)
    screen.blit(msg_txt, (WIDTH // 2 - msg_txt.get_width() // 2, 433))

    # Draw Action Buttons
    mouse_pos = pygame.mouse.get_pos()
    for btn in buttons:
        btn_rect = pygame.Rect(btn["x"], btn["y"], 150, 50)
        
        # Hover effect
        color = btn["color"]
        if btn_rect.collidepoint(mouse_pos):
            color = (min(color[0] + 30, 255), min(color[1] + 30, 255), min(color[2] + 30, 255))
        
        pygame.draw.rect(screen, color, btn_rect, border_radius=15)
        txt = font_btn.render(btn["label"], True, DARK_GRAY)
        screen.blit(txt, (btn["x"] + 30, btn["y"] + 12))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == STAT_DECAY:
            if is_sleeping:
                stats["Energy"] = min(100, stats["Energy"] + 10)
                if stats["Energy"] >= 100:
                    is_sleeping = False
                    message = "Boba woke up feeling fully refreshed! ☀️"
            else:
                stats["Hunger"] = max(0, stats["Hunger"] - 3)
                stats["Happiness"] = max(0, stats["Happiness"] - 2)
                stats["Energy"] = max(0, stats["Energy"] - 2)
                stats["Cleanliness"] = max(0, stats["Cleanliness"] - 2)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons:
                btn_rect = pygame.Rect(btn["x"], btn["y"], 150, 50)
                if btn_rect.collidepoint(event.pos):
                    if btn["action"] == "feed":
                        if is_sleeping:
                            message = "Shh! Boba is sleeping... 🤫"
                        else:
                            stats["Hunger"] = min(100, stats["Hunger"] + 25)
                            message = "Yum! Boba enjoyed a tasty snack! 🍎"

                    elif btn["action"] == "play":
                        if is_sleeping:
                            message = "Wake Boba up first before playing!"
                        elif stats["Energy"] < 20:
                            message = "Boba is too tired to play... 💤"
                        else:
                            stats["Happiness"] = min(100, stats["Happiness"] + 20)
                            stats["Energy"] = max(0, stats["Energy"] - 15)
                            stats["Cleanliness"] = max(0, stats["Cleanliness"] - 10)
                            message = "Yay! Boba had so much fun! 🎾"

                    elif btn["action"] == "clean":
                        if is_sleeping:
                            message = "Don't wash Boba while he's sleeping!"
                        else:
                            stats["Cleanliness"] = 100
                            message = "Squeaky clean! Boba smells wonderful! 🧼✨"

                    elif btn["action"] == "sleep":
                        is_sleeping = not is_sleeping
                        if is_sleeping:
                            message = "Goodnight Boba! Rest well... 🌙"
                        else:
                            message = "Good morning! Boba is awake! ☀️"

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()