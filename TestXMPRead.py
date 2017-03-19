from libxmp import XMPFiles, consts
xmpfile = XMPFiles( file_path="Pong.jpg" )
xmp = xmpfile.get_xmp()
print(xmp)
