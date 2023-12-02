from turtle import*
bgcolor('black')
pensize(2)
color('red','yellow')
begin_fill()
while True:
    forward(380)
    left(160)
    if abs(pos())<1:
        break
end_fill()
done()