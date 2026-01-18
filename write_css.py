# Write enhanced CSS file
css = """/* LARK LABS INSPIRED DARK THEME */
* { margin: 0; padding: 0; box-sizing: border-box; }
"""

# Add the rest in parts
css += """
:root {
    --primary-blue: #3498db;
    --primary-dark: #2c3e50;
    --pure-black: #1a1a1a;
    --charcoal: #2c3e50;
    --success-green: #27ae60;
    --success-light: #2ecc71;
    --warning-orange: #f39c12;
    --warning-dark: #e67e22;
    --alert-red: #e74c3c;
    --gold: #ffd700;
    --text-white: #ffffff;
    --text-light: #ecf0f1;
    --text-gray: #bdc3c7;
    --text-dark: #95a5a6;
    --glass-bg: rgba(255, 255, 255, 0.1);
    --glass-border: rgba(255, 255, 255, 0.2);
    --card-bg: rgba(44, 62, 80, 0.8);
}
"""

with open('styles.css', 'w') as f:
    f.write(css)
print("Started CSS file")
