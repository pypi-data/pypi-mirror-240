extention_image = ['.png','.jpg']

#**FASILITE JPG_TO_PNG**
def jpg_to_png (infile, outfile) :
    try:
        with open(infile,'rb') as jpgf:
            jpgd = jpgf.read()
    except FileNotFoundError:
        print(f"Fichier non trouve", {infile})
        return
    except IOError as e:
        print(e)

    pngd = b'\x89PNG\r\n\x1a\n' + jpgd[2:]
    try :
        with open (outfile, 'wb') as pngf:
            pngf.write(pngd)
    except IOError as e:
        print(e)
    




def png_to_jpg(infich,outfich):
    if any(infich.lower().endswith(png)for png in extention_image):
        try:
            with open(infich,'rb') as pngf:
                pngf = pngf.read()
        except FileNotFoundError:
            print(f" nou pa jwen fichier {infich} la")  
        except IOError as e:
            print(e)          

        jpgd=pngf[33:]    

        with open(outfich,'wb') as jpgf:
            jpgf.write(jpgd)
    else:
        print('pa gen fich konsa')