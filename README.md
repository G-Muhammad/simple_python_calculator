# Simple Calculator

A **Simple Calculator** built using Python and the Tkinter library. This graphical user interface (GUI) calculator supports basic arithmetic operations: addition, subtraction, multiplication, and division. The calculator is designed to handle input restrictions and provide a responsive user experience.

---

## Features

- Perform basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Clear the input using the `C` button.
- Dynamically adjust font size for large numbers.
- Restrict maximum input length to prevent UI overflow.
- Handle invalid inputs gracefully (e.g., division by zero).
- Keyboard shortcuts for enhanced usability.

---

## How to Use

1. Clone the repository or download the code file.
2. Make sure you have Python installed on your system (version 3.x).
3. Run the script in your terminal or Python IDE:
   ```bash
   python calculator.py
   ```
4. Use the GUI to perform calculations.

---

## Keyboard Shortcuts

- Numbers: Use your keyboard to input digits (`0-9`).
- Operators: Press `+`, `-`, `*`, `/` for the respective operations.
- Clear: Press `C` or `c` to clear the screen.
- Equals: Press `Enter` to calculate the result.

---

## Dependencies

This project requires no external dependencies. It uses Python's built-in `tkinter` module.

---

## File Structure

- `calculator.py`: The main Python script containing the calculator logic and GUI.
- `IMG_20241027_230002.ico`: (Optional) Icon file for the application. If not available, the program runs without it.

---

## Code Highlights

1. **Restrict Input Length:**
   ```python
   if len(current) < MAX_DIGITS:  # Restrict input length
       new = current + str(digit)
   ```

2. **Error Handling:**
   - Division by zero displays an `Error` message:
     ```python
     if second_number == 0:
         result_label.config(text='Error')
     ```

3. **Dynamic Font Adjustment:**
   - Dynamically adjusts the font size based on the length of the input or result:
     ```python
     def adjust_font_size():
         text_length = len(result_label['text'])
         font_size = 30 if text_length <= 10 else 20 if text_length <= 15 else 15
         result_label.config(font=('verdana', font_size, 'bold'))
     ```

4. **Keyboard Bindings:**
   ```python
   root.bind("<Key>", key_press)
   ```

---

## Future Improvements

- Add support for advanced mathematical functions (e.g., square root, power).
- Include a history panel to view past calculations.
- Improve error messages for better user understanding.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it.

---

## Acknowledgments

- Built with love using Python and Tkinter.
- Thanks to the Tkinter documentation and Python community for guidance.

---

Enjoy using the Simple Calculator! If you have any questions or suggestions, feel free to reach out.