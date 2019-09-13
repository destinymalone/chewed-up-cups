name = input("Name: ")

grad_class = int(input("Graduating Class: "))

hometown = input("Hometown: ")

html_str = f"""
    <h1 style="color: yellow"><strong>{name}</strong></h1>
    <h2 style="color: pink"><strong>{grad_class}</strong></h2>
    <h3 style="color: lightblue"><strong>{hometown}</strong></h3>
"""

Html_file = open("kid_day.html", "w")
Html_file.write(html_str)
Html_file.close()
