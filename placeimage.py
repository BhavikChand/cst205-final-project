from PIL import Image
def place_image(bg,subject,bg_manip,s_manip,x_pos,y_pos,bg_w,bg_h,s_w,s_h,b_style,b_strength,corner):
    bg_im = Image.open(bg)
    s_im = Image.open(subject)
    if(s_w == 0):
        s_w = s_im.width
    if(s_h == 0):
        s_h = s_im.height
    #bg_im = manip(bg_manip,resize(bg_im,bg_w,bg_h))
    #s_im = manip(s_manip,resize(s_im,s_w,s_h))
    for y in (0,s_h):
        if y + y_pos > bg_im.height:
            print()
            break
        for x in (0,s_w):
            if x + x_pos > bg_im.width:
                break
            bg_im.putpixel((x+x_pos,y+y_pos),s_im.getpixel((x,y)))
    bg_im.save("finalimages/result.jpg")