from libxmp import XMPFiles, consts
xmpfile = XMPFiles( file_path="Pong.jpg" )
xmp = xmpfile.get_xmp()
print(xmp)
xmpfile = XMPFiles( file_path="William.jpg" )
xmp = xmpfile.get_xmp()
print(xmp)
