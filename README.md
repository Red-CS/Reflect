# Reflect Programming Language

## Overview

**Reflect** is an esoteric programming language that translates normal text into executable instructions based on their casing, punctuation, and sentence length. All data is stored as an unsigned byte, and is tracked using a pointer reference.
What makes **Reflect** special is that these operations are performed in one of two modes:

- _Navigation_ mode, where the word count moves the cursor in the current direction.
- _Mutate_ mode, where the word count increments/decrements the curosr in the current direction.

Each sentence has its own properties, defined by the punctuation. Despite that, the words themselves don't matter, so programs are free to be as plain as needed (although the original idea was a program encoded as a journal entry).

## Punctuation Operations

| Syntax | Description                                                                  |
| ------ | ---------------------------------------------------------------------------- |
| .      | Marks the end of a sentence                                                  |
| ,      | Reads input from stdin                                                       |
| -      | A sentence in _Mutate_ mode will decrement the value instead of incrementing |
| '      | Used to write comments                                                       |
| (      | Starts a loop                                                                |
| )      | Ends a loop                                                                  |
| ?      | Changes direction to Left, and ends the sentence.                            |
| !      | Changes direction to Right, and ends the sentence.                           |

## Sentence Operations

- **Capital Letters:** If a sentence starts with Captal Letters, then the sentence is in Navigation mode. ? and ! still take effect.
- **Lowercase Letters:** If a sentence starts with Lowercase Letters, then the sentence is in Mutate mode. ? and ! still take effect.
- **Sentence Word Count** the number of words in the sentence, the pointer will move that many cells in the current direction OR increments/decrements that cell value that many spaces
