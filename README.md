# Write words from clipboard

A small script to add words from the clipboard to [tldraw](https://www.tldraw.com/).

``` shell
git clone https://github.com/gambhiro/clip-write-words.git
cd clip-write-words
poetry install
poetry run ./clip-write-words.py
```

On the first run, the Terminal will ask for permission to control the computer.

## Usage

1. Copy the text to clipboard.
2. Prepare the browser window to insert the text to.
3. Start the script in the terminal. (It will wait 5s to allow for the next step)
4. Move the mouse to the position of the first word
5. Click on the window to make sure it is in focus
6. **DON'T TOUCH** the mouse or keyboard while the script is writing.

The script will take the clipboard content, split it to words at each space.

For each word:

- it copies it to the clipboard
- activates the "Text" tool with key `t`
- pastes the word with `Ctrl/Cmd + V`
- moves to mouse position for the next word

The script adds the words on tldraw, then you have to arrage them.

It is useful to turn on `Menu > Preferences > Always Snap`.

Select the words, `Right Click > Arrange > Align top`.

To move the words to equal distance, select one, align to the side edge of the previous word, press `Shift + Right Arrow (x5)` to move.

Select the next word, move to a similar distance, the snap guides will help position it at the same distance.

A similar technique can work for vertical positioning. `Shift + Down Arrow (x12)` gives sufficient line spacing.

