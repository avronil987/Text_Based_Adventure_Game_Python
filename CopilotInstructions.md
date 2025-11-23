# Copilot Instructions for Python Adventure Game
## Project Overview
This is a modular, text-based adventure game in Python. The user explores either a cave or a forest, making choices at each level. Only specific sequences of choices result in a win; all other choices end the game with a snappy message. The game is designed for easy expansion and clear user feedback.
## Key Files
- `adventure_game.py`: Main entry point, handles user input, path selection, and replay logic.
- `cave.py`: Implements the cave adventure with 6 levels and 2 winning paths.
- `forest.py`: Implements the forest adventure with 5 levels and 2 winning paths.
- `.github/copilot-instructions.md`: This file, for AI agent guidance.
## Developer Workflows
- **Run the game:**
	```bash
	python adventure_game.py
	```
- **Replay:** After each game, user can choose to replay (screen clears and game restarts).
- **Expand paths:** Add new levels or choices by editing `cave.py` or `forest.py`.
- **Add new adventures:** Create new modules and import them in `adventure_game.py`.
## Username Rules
- Must start with an alphabet (A-Z or a-z)
- Can contain alphabets and numbers only
- Length must be greater than 3 characters
- Invalid usernames prompt rules and re-entry
## Cave Path Flow
- 6 levels, binary choices at each
- Two winning paths:
	- Path A: Enter quietly → Left tunnel → Build a raft → Examine crystals → Sneak past dragon → Use crystal to open exit
	- Path B: Enter quietly → Right tunnel → Swim across → Force open door → Take idol → Place idol on pedestal
- All other choices result in a loss with a snappy, relevant message
## Forest Path Flow
- 5 levels, binary choices at each
- Two winning paths:
	- Path A: Trail → Log → Climb → Signal → Wave
	- Path B: Trail → Raft → Paddle → Jump → Enter cave
- All other choices result in a loss with a snappy, relevant message
## Patterns and Conventions
- Each path function starts with a docstring listing the winning paths
- Losses always print a relevant, snappy message before exiting the function
- Replay logic is handled in `adventure_game.py` after a path completes
- Modular structure: each adventure path in its own file
## Guidance for AI Agents
- When expanding, follow the binary choice structure and snappy feedback pattern
- Add new paths as separate modules and import them in the main script
- Update this file with new flows, rules, or conventions as the project evolves

---
*Update this file whenever major changes are made to project structure or workflows.*
