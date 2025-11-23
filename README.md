# Python Adventure Game

A text-based adventure game in Python where you explore mysterious caves and forests, making choices to win or lose. Only the right sequence of choices will lead you to victory!

## Features
- Two adventure paths: Cave and Forest
- Multiple levels with binary choices
- Snappy win/lose messages for every outcome
- Replay option after each game
- Modular code for easy expansion

## How to Play
1. Run the game:
   ```bash
   python adventure_game.py
   ```
2. Enter your username (must start with an alphabet, be alphanumeric, and longer than 3 characters).
3. Choose your adventure path: Cave or Forest.
4. Make choices at each level. Only specific sequences will let you win!
5. Replay as many times as you like.

## File Structure
- `adventure_game.py` — Main game logic and entry point
- `cave.py` — Cave adventure path
- `forest.py` — Forest adventure path
- `.github/copilot-instructions.md` — AI agent instructions

## Example Win Paths
- **Cave:** Enter quietly → Right tunnel → Swim across → Force open door → Take idol → Place idol
- **Forest:** Trail → Raft → Paddle → Jump → Enter cave
