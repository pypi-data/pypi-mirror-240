import marimo

__generated_with = "0.1.0"
app = marimo.App()


@app.cell
def one():
    type = 1
    return type,


@app.cell
def two(type):
    type
    return


if __name__ == "__main__":
    app.run()
