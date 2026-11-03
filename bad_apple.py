import sys
import time
import shutil
import cv2

# ASCII characters ordered from darkest to brightest
ASCII_CHARS = "  ..::--==++**##%%@@"

def frame_to_ascii(frame, width, height):
    # Resize frame to target terminal dimensions
    resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
    # Convert to grayscale
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    
    char_len = len(ASCII_CHARS) - 1
    lines = []
    
    # Map pixel values (0-255) to ASCII character palette
    for row in gray:
        line = "".join(ASCII_CHARS[int((pixel / 255.0) * char_len)] for pixel in row)
        lines.append(line)
        
    return "\n".join(lines)

def play(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open {video_path}")
        return

    # Target frame timing
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    frame_duration = 1.0 / fps

    # Terminal characters are roughly twice as tall as they are wide
    term_cols, term_lines = shutil.get_terminal_size((80, 24))
    render_width = term_cols - 1
    render_height = term_lines - 1

    # ANSI home position code (resets cursor without clearing screen to prevent flicker)
    home_cursor = "\033[H"
    
    # Hide terminal cursor
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        while True:
            start_time = time.perf_counter()
            ret, frame = cap.read()
            if not ret:
                break

            ascii_frame = frame_to_ascii(frame, render_width, render_height)
            sys.stdout.write(home_cursor + ascii_frame)
            sys.stdout.flush()

            elapsed = time.perf_counter() - start_time
            sleep_time = frame_duration - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)

    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        # Restore terminal cursor
        sys.stdout.write("\033[?25h\n")
        sys.stdout.flush()

if __name__ == "__main__":
    video_file = sys.argv[1] if len(sys.argv) > 1 else "bad_apple.mp4"
    play(video_file)