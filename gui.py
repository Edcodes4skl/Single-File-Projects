import flet as ft
def main(page:ft.Page):
    def maker(e):
        content = str(textbox.value)
        with open("thing.txt" , "w") as file:
            file.write(content)
            
    def opener(e):
        content = str(textbox.value)
        try:
            with open("text" , "r") as file:
                inside  = file.read()
            textbox.value = inside
            counter()
        except FileNotFoundError:
            print("Not found")

    def recorder(e):
        content = str(textbox.value)
        with open("thing.txt" , "w") as file:
            file.write(content)

    def counter(e):
        numb = len(textbox.value.split())
        count.value=(str(f"Words: {numb}"))
        page.update()
    textbox = ft.TextField(
        value = "",
        hint_text="Enter text here",
        multiline= True,
        on_change = counter
    )
    count = ft.Text(value=f"Current Words: 0")
    openerer = ft.ElevatedButton(text="Open File" , on_click= opener)
    save = ft.ElevatedButton(text="Save File" , on_click= recorder)
    create = ft.ElevatedButton(text="Create File" , on_click= maker)
    page.add(openerer,save,create,textbox,count)
ft.app(target=main)