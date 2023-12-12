from PIL import Image
import math
def place_image(bg,subject,bg_manip,s_manip,x_pos,y_pos,bg_w,bg_h,s_w,s_h,b_style,b_strength,corner,bg_t,bg_b,bg_l,bg_r,s_t,s_b,s_l,s_r):
    bg_im = Image.open(bg)
    s_im = Image.open(subject)
    if(s_w == 0):
        s_w = s_im.width - s_l - s_r
    if(s_h == 0):
        s_h = s_im.height - s_t - s_b
    if(bg_w == 0):
        bg_w = bg_im.width - bg_l - bg_r
    if(bg_h == 0):
        bg_h = bg_im.height - bg_t - bg_b

    if(x_pos == -1):
        x_pos = (bg_w//2)-(s_w//2)
    if(x_pos == -2):
        x_pos == bg_w-s_w
    if(y_pos == -1):
        y_pos = (bg_h//2)-(s_h//2)
    if(y_pos == -2):
        y_pos == bg_h - s_h

    bg_im = manipulate(bg_manip,crop(resize(bg_im,bg_w,bg_h),bg_t,bg_b,bg_l,bg_r))
    s_im = manipulate(s_manip,resize(s_im,s_w,s_h))
    for y in range(0,s_h-s_t-s_b):
        if y + y_pos < 0:
            continue
        if y + y_pos >= bg_im.height:
            break
        for x in range(0,s_w-s_l-s_r):
            if x + x_pos < 0:
                continue
            if x + x_pos >= bg_im.width:
                break
            bg_im.putpixel((x+x_pos-bg_l,y+y_pos-bg_t),s_im.getpixel((x+s_l,y+s_t)))
        
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
                
                if(foo > 1):
                    foo = (baseline - m)/b_strength
                    foo = -(foo-0.5)+0.5
                    
                bar = -(foo-0.5)+0.5
                if(b_style == "Outward"):
                    foo = math.sqrt(abs(pow(b_strength,2) - pow(m-baseline,2))/pow(b_strength,2))
                    bar = -(foo-0.5)+0.5
                if(b_style == "Inward"):
                    foo = math.sqrt(abs(pow(b_strength,2) - pow(b_strength-abs(m-baseline),2))/pow(b_strength,2))
                    foo = -(foo-0.5)+0.5
                    bar = -(foo-0.5)+0.5
                if(b_style == "Wave"):
                    foo = math.sin((abs(m-baseline)*math.pi/b_strength)+math.pi/2)*0.5+0.5
                    bar = -(foo-0.5)+0.5
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
                    bar = (abs(x - base[0] - x_direction) + abs(y - base[1]- y_direction))/b_strength
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
                if(b_style == "Outward"):
                    bar = -(bar-0.5)+0.5
                    bar = math.sqrt(1-math.pow(1-bar,2))
                    bar = -(bar-0.5)+0.5
                if(b_style == "Inward"):
                    bar = math.sqrt(1-math.pow(1-bar,2))
                if(b_style == "Wave"):
                    bar = math.sin((1-bar+0.5)*math.pi)*0.5+0.5
                foo = -(bar-0.5)+0.5
                for n in range(0,3):
                    pixel[n] = int(bar*bg_im.getpixel((x,y))[n] + (bg_im.getpixel(base)[n]*foo))
                pixel = (pixel[0],pixel[1],pixel[2])
                bg_im.putpixel((x,y),pixel)
    bg_im.save("finalimages/result.jpg")

# small wrapper
def grayscale_pixel(pixel):
    gray_value = int((pixel[0] + pixel[1] + pixel[2]) / 3)
    return (gray_value, gray_value, gray_value)

def manipulate(selected_manipulation,image):
    width, height = image.size
    if selected_manipulation == "None":
        return image
    elif selected_manipulation == "Sepia":
        sepia = Image.new('RGB', image.size)
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                sepia.putpixel((x, y), (tr, tg, tb))
        return sepia
    elif selected_manipulation == "Negative":
        negative_image = Image.new('RGB', (width, height))
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                new_r = 255 - r
                new_g = 255 - g
                new_b = 255 - b
                negative_image.putpixel((x, y), (new_r, new_g, new_b))
        return negative_image
    elif selected_manipulation == "Grayscale":
        grayscale_image = Image.new("RGB", (width, height))
        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, y))
                gray_pixel = grayscale_pixel(pixel)
                grayscale_image.putpixel((x, y), gray_pixel)
        return grayscale_image
    elif selected_manipulation == "Thumbnail":
        image = Image.open(image_path)
        width, height = image.size
        thumbnail_width = width // 2
        thumbnail_height = height // 2
        thumbnail = Image.new("RGB", (thumbnail_width, thumbnail_height))

        for y in range(thumbnail_height):
            for x in range(thumbnail_width):
                pixel = image.getpixel((x * 2, y * 2))
                thumbnail.putpixel((x, y), pixel)
        return thumbnail

def resize(im,w,h):
    out = Image.new("RGB",(w,h))
    for y in range(0,h):
        for x in range(0,w):
            out.putpixel((x,y),im.getpixel((x*im.width/w,y*im.height/h)))
    return out

def crop(im,top,bottom,left,right):
    out = Image.new("RGB",(im.width-left-right,im.height-top-bottom))
    for y in range(0,out.height):
        for x in range(0,out.width):
            out.putpixel((x,y),im.getpixel((left+x,top+y)))
    return out