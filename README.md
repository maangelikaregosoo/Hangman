# Hangman Game

A fun and interactive command-line implementation of the classic Hangman word-guessing game in Python. Test your word-guessing skills and see if you can save the stick figure from the gallows!

## 🚀 Quick Start (Choose Your Path)

### ⚡ Easiest: Download & Play (No Installation)
1. Go to the [Releases](../../releases) page
2. Download `hangman.exe` (or the version for your OS)
3. Double-click to play!

**That's it!** No Python needed. 🎮

### 💻 Developer Path: Run from Source
```bash
# Clone the repository
git clone https://github.com/maangelikaregosoo/Hangman.git

# Navigate to the Hangman directory
cd Hangman

# Run the game (requires Python 3.6+)
python3 hangman.py
```
---

## Features

- 🎮 **Interactive Gameplay**: Guess letters to figure out hidden words
- 🎯 **Customizable Difficulty**: Choose the number of allowed guesses
- 🎲 **Word Selection**: Pick between randomly generated words or enter your own custom word
- 👤 **Two-Player Mode**: One player sets the word, another player guesses
- 🎨 **Visual Hangman Figure**: Watch the stick figure appear as incorrect guesses are made
- 📊 **Game Statistics**: Track your wins across multiple games
- 📝 **Diverse Word Bank**: 48 words across categories (animals, fruits, countries, sports, names)
- 🔤 **Letter Tracking**: See which letters you've already guessed
- ♻️ **Play Again**: Continue playing as many rounds as you'd like

## Game Features in Detail

- **Case-Insensitive Input**: Enter letters in any case
- **Input Validation**: The game ensures you enter valid inputs
- **Duplicate Prevention**: You cannot guess the same letter twice
- **Visual Feedback**: See the stick figure build up with each wrong guess
- **Remaining Letters Display**: Know which letters are still available to guess


---

## How to Play

### Gameplay Instructions

1. **Start the Game**: Run the script and you'll be prompted to set up the game
2. **Word Selection**: Choose whether you want the game to:
   - Select a random word from the built-in word list, or
   - Enter your own custom word for your opponent to guess
3. **Set Difficulty**: Enter the number of guesses allowed (recommended: 6-10)
4. **Make Your Guesses**: 
   - Enter one letter at a time
   - Letters are case-insensitive
   - The game will reveal positions where your guessed letter appears
5. **Win or Lose**:
   - **Win**: Guess all letters in the word before running out of guesses
   - **Lose**: The stick figure is hanged when you run out of guesses
6. **Play Again**: After each game, decide whether to play another round

## Example Game Session

```
LET'S PLAY HANGMAN!

Would you like the program to choose a random word? (Yes/No)
> yes

Here is the word to be guessed by your opponent: ****
Please enter the number of guesses allowed:
> 8

Guess the word, 8 guess(es) left: ------
Unused letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ

State of Hangman Stick Figure:
  _ _ _ _ 
 |       |
 |       
 |      
 |       
```

---

## Installation & Setup (For Source Code)

Choose your operating system below for detailed instructions:

#### 🍎 macOS

**Option 1: Using Homebrew (Recommended)**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python3

# Verify installation
python3 --version
```

**Option 2: Direct Download**
1. Visit https://www.python.org/downloads/
2. Click "Download Python 3.x.x"
3. Run the installer
4. Follow the setup wizard

---

#### 🪟 Windows

**Step 1: Download Python**
1. Go to https://www.python.org/downloads/
2. Click the yellow "Download Python 3.x.x" button
3. Save the installer to your computer

**Step 2: Install Python**
1. Open the downloaded installer
2. ⚠️ **IMPORTANT**: Check the box "Add Python 3.x to PATH" at the bottom
3. Click "Install Now"
4. Wait for installation to complete
5. Click "Close"

**Step 3: Verify Installation**
1. Open Command Prompt (press `Win + R`, type `cmd`, press Enter)
2. Type: `python --version`
3. You should see "Python 3.x.x"

---

#### 🐧 Ubuntu/Debian (Linux)

**Step 1: Update Package Manager**
```bash
sudo apt-get update
sudo apt-get upgrade
```

**Step 2: Install Python**
```bash
sudo apt-get install python3 python3-pip
```

**Step 3: Verify Installation**
```bash
python3 --version
```
---

### No Additional Dependencies Needed
This project uses only Python's built-in modules. No pip packages required!


## Author

Ma. Angelika C. Regoso

## License

This project is provided as-is for educational purposes.