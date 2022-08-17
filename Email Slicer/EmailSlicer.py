def EmailSlicer(s):
    a = s.split("@")
    return "Your username is " + a[0] + " & domain is " + a[1]
