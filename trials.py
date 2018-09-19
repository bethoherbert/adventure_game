from shapes import Paper, Oval

test_circle = Oval()
test_circle.randomize(smallest=15, largest=150)
test_circle.draw()

Paper.display()

print('Can I write on the Paper?')