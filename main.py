import os, zlib, sys, time, base64

# //////////////////////////////
# ///////GDCC_Comp 2021 ////////
# //////////_BY Brett Palmer_///
#-------------------------------
#Ver 1.....Basic Patern Builder.
#ver 2.....Possitional Notation Matrix (X to Y)
#Ver 3.....64*64*64 Matrix Possition Notation Next Dimention

from typing import TextIO

def processfile(FileE,Size):
   # if FileE: str = (''):
      # raise ValueError ('No_File!')
    return Size

def TimeTakem(ta,tb):
    return tb - ta

if __name__ == '__main__':
    print('World Competition Compression of Data 2021!  By FoldingCircles>AKA(Mince)/aka(BrettPalmer)')
    FCTextCompressStart = time.time()

    try:
        print ('arg=', sys.argv[1])
    except Exception:
        print('No File Suggested use Default Test File.\n')
        print('GDCC Data Compression Competition 2021, By Brett Palmer.\n')
        print('Uses FCCompress',' (filename.ext) Compression Key Reprate MAX')
        print('Arg "FileName"')
        print('Competition Test_!')
        #text = open('test.txt.', 'rb').read()
        text = open('test1_demo', 'rb').read()
        print('Raw Size =', sys.getsizeof(text))
        print('-------------------------------------------------------------------------\n')
        print(text)
    else:
        try:
            t = sys.argv[1]
            text = open(t,'rb').read()
        except FileNotFoundError:
            print('File Not Found.')
        else:
            print('FoldingCircles TM                  GDCC 2021 Comp Entry 1 2 & 3\n')
            print('Mode 2 Active')
            print('Raw Size =', sys.getsizeof(text))

            print(text.read())
            text.close()
            print('FC Compress Active Please Wait!.\n')
            print('File=', t)
    finally:
        print('\n Python Ver> Programmed For GDCC Comp 2021 By Brett Palmer All Rights Reserved')
        print('\nThank you For using FC Software')
        FCTextCompressEnd = time.time()
        print('Time Taken in Seconds=',TimeTakem(FCTextCompressStart,FCTextCompressEnd))

    # compressed = zlib.compress(text)

    #print('Compressed size=', sys.getsizeof(compressed))
    #By Mince (C)
