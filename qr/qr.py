import qrcode as qr
img = qr.make("https://www.youtube.com/@florist_crafts")
img.save("florist_crafts.png")
