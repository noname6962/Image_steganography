# Image Steganography

This was a project for my uni cryptography course



Requirements for it were:

- Self-made cryptography method (not implementation of existing method)

- Simple concept

- Quick implementation



## How does it work?
1. First pixel of the photo codes the position of first coding pixel and length of the message via modifying values of RGB channels

2. Move to the first coding pixel

3. Pick between Red, Green or Blue channel based on the surrounding pixel colors so that the change in rgb values isn't noticeable

4. Modify the value of the picked channel to represent the next character of the message in ASCII values

5. Move 4 pixels to the right (if we reach the end of the photo, drop down 4 pixels and subtract the width of the photo from the x value)

6. Repeat steps 3-5 until the end of the message.

For decoding step 4 changes from modifying to reading the value

## Limitations
This system doesnt handle compression of the files, so formats like jpg wouldnt work

Thous the default file format of imported and exported files is PNG
