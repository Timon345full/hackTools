import pyscreenshot 

def screenShot():
    # To capture the screen 
    image = pyscreenshot.grab() 
    
    # To display the captured screenshot 
    image.show() 
    
    # To save the screenshot 
    image.save("static/GeeksforGeeks.png") 

def screenRead():
    pass