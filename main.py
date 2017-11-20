print "Hello, I'm your assistant. I can convert kilometers into miles :)"

x = int (raw_input( "Please, enter the number you want converted: " ) )
y = 0.62
print x * y

while True:
    question = str ( raw_input( "Do you want to make another calculation? " ) ).lower()

    if question == "yes":
        x = int(raw_input("Please, enter the number you want converted: "))
        y = 0.62
        result = x * y
        print result

    elif question == "no":
        print "Thanks for using me. Bye-bye."
        break

    else:
        print "Please answer with yes or no."
