# pettalk
Pettalk is a Raspberry Pi based device with buttons that trigger recorded voices for pets to press, telling their owner what they want.  It's based on stories like https://www.boredpanda.com/custom-soundboard-dog-talk-christina-hunger/?utm_source=google&utm_medium=organic&utm_campaign=organic , https://people.com/pets/dog-learning-to-talk-by-using-a-custom-soundboard-to-speak-im-in-constant-amazement/ 

There's no details on how those are built, but it looks like each button is independent.  However, I'm a software person, and wanted to reduce costs, so in my design, there's a matrix of just buttons connected to the Raspberry Pi, and the sound files are all on the SD card.

Requires
- Python
- pydub (pip install pydub)
