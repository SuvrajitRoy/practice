import qrcode

# text= input("Enter the text or url to be converted in Qrcode:")

# filename= input("Enter filename to save the qrcode image:")

# def generate_qrcode(text, filename):

#     #convert text or url to qrcode
#     image_qrcode = qrcode.make(text)

#     #save the qrcode image
#     image_qrcode.save(filename) 

# generate_qrcode(text, filename)

def generate_qrcode(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()

    text = lines[0].strip()
    filename = lines[1].strip()

    #qrcode make() 
    image_qrcode = qrcode.make(text)

    #save qrcode 
    image_qrcode.save(filename) 

generate_qrcode('input/a.txt')