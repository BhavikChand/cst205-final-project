from PIL import Image
import math
def place_image(bg,subject,bg_manip,s_manip,x_pos,y_pos,bg_w,bg_h,s_w,s_h,b_style,b_strength,corner):
    bg_im = Image.open(bg)
    s_im = Image.open(subject)
    if(s_w == 0):
        s_w = s_im.width
    if(s_h == 0):
        s_h = s_im.height
    if(bg_w == 0):
        bg_w = bg_im.width
    if(bg_h == 0):
        bg_h = bg_im.height

    if(x_pos == -1):
        x_pos = (bg_w//2)-(s_w//2)
    if(x_pos == -2):
        x_pos == bg_w-s_w
    if(y_pos == -1):
        y_pos = (bg_h//2)-(s_h//2)
    if(y_pos == -2):
        y_pos == bg_h - s_h

    bg_im = manipulate(bg_manip,resize(bg_im,bg_w,bg_h))
    s_im = manipulate(s_manip,resize(s_im,s_w,s_h))
    for y in range(0,s_h):
        if y + y_pos < 0:
            continue
        if y + y_pos >= bg_im.height:
            break
        for x in range(0,s_w):
            if x + x_pos < 0:
                continue
            if x + x_pos >= bg_im.width:
                break
            bg_im.putpixel((x+x_pos,y+y_pos),s_im.getpixel((x,y)))
        
    left = x_pos
    right = x_pos + s_w - 1
    top = y_pos
    bottom = y_pos + s_h - 1
    left_ranges = (range(top,bottom+1),range(left,left-b_strength,-1),True)
    right_ranges = (range(top,bottom+1),range(right,right+b_strength),True)
    top_ranges = (range(left,right+1),range(top,top-b_strength,-1),False)
    bottom_ranges = (range(left,right+1),range(bottom,bottom+b_strength),False)

    
    for i in ((left_ranges),(right_ranges),(top_ranges),(bottom_ranges)):
        baseline = 0
        for o in i[1]:
            baseline = o
            break
        for k in i[0]:
            sides = i[2]

            if k < 0 or (sides and (k >= bg_h)) or ((not sides) and (k >= bg_w)):
                continue
            if(sides):
                base = (baseline,k)
            else:
                base = (k,baseline)
            for m in i[1]:
                if m < 0 or (sides and m >= bg_w) or ((not sides) and m >= bg_h):
                    continue
                if(sides):
                    x = m
                    y = k
                else:
                    x = k
                    y = m

                pixel = [0,0,0]
                foo = (baseline + b_strength - m)/b_strength
                bar = -(foo-0.5)+0.5
                if(foo > 1):
                    bar = (baseline - m)/b_strength
                    foo = -(bar-0.5)+0.5
                for n in range(0,3):
                    pixel[n] = int(bar*bg_im.getpixel((x,y))[n] + (bg_im.getpixel(base)[n]*foo))
                pixel = (pixel[0],pixel[1],pixel[2])
                bg_im.putpixel((x,y),pixel)


        
    for (base,x_direction,y_direction) in (((left,top),-1,-1),((right,top),1,-1),((left,bottom),-1,1),((right,bottom),1,1)):
        for x in range(base[0]+x_direction,base[0] + b_strength*x_direction,x_direction):
            if x >= bg_w:
                continue
            for y in range(base[1]+y_direction,base[1] + b_strength*y_direction,y_direction):
                if y >= bg_h or y < 0:
                    continue
                pixel = [0,0,0]
                if(corner == "Diagonal"):
                    bar = (abs(x - base[0]) + abs(y - base[1]))/b_strength
                if(corner == "Rounded"):
                    bar = (math.sqrt(pow(x-base[0],2)+pow(y-base[1],2)))/b_strength
                if(corner == "Sharp"):
                    if (abs(x - base[0]) >= abs(y - base[1])):
                        bar = x_direction * (base[0] + x_direction + (b_strength * x_direction) - x)/b_strength
                        bar = -(bar-0.5)+0.5
                    else:
                        bar = y_direction * (base[1] + y_direction + (y_direction * b_strength) - y)/b_strength
                        bar = -(bar-0.5)+0.5
                if bar > 1:
                    bar = 1
                foo = -(bar-0.5)+0.5
                for n in range(0,3):
                    pixel[n] = int(bar*bg_im.getpixel((x,y))[n] + (bg_im.getpixel(base)[n]*foo))
                pixel = (pixel[0],pixel[1],pixel[2])
                bg_im.putpixel((x,y),pixel)


    bg_im.save("finalimages/result.jpg")

def manipulate(manip,im):
    return im

def resize(im,w,h):
    print("resizing")
    out = Image.new("RGB",(w,h))
    for y in range(0,h):
        for x in range(0,w):
            out.putpixel((x,y),im.getpixel((x*im.width/w,y*im.height/h)))
    return out